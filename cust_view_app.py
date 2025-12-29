import gradio as gr
import pandas as pd
import requests
from supabase import create_client, Client

# --- 1. CONFIGURATION & ASSETS ---
SUPABASE_URL = "https://rgpofziwsnusdloivgea.supabase.co"
SUPABASE_KEY = "sb_publishable_JAHrbPskQV-deLRLtkUNbw_dlBACLKq"
LOGO_URL = "https://raw.githubusercontent.com/sudhir-voleti/mishtee-magic/main/mishTee_logo.png"
STYLE_URL = "https://raw.githubusercontent.com/sudhir-voleti/mishtee-magic/main/style.py"
BRAND_URL = "https://raw.githubusercontent.com/sudhir-voleti/mishtee-magic/main/brand.txt"

# Initialize Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fetch CSS and Brand Slogan
try:
    style_res = requests.get(STYLE_URL)
    mishtee_css = style_res.text if style_res.status_code == 200 else ""
    
    brand_res = requests.get(BRAND_URL)
    brand_slogan = brand_res.text.strip() if brand_res.status_code == 200 else "Authentic Ahmedabad Treats"
except Exception:
    mishtee_css = ""
    brand_slogan = "Authentic Ahmedabad Treats"

# --- 2. CORE FUNCTIONS ---

def get_customer_portal_data(phone_number):
    """Retrieves customer greeting and order history."""
    if not phone_number or len(phone_number) < 10:
        return "Please enter a valid phone number.", pd.DataFrame()

    # Fetch Customer Name
    cust_res = supabase.table("customers").select("full_name").eq("phone", phone_number).execute()
    
    if not cust_res.data:
        return "Welcome! We couldn't find your profile. Please register at our store.", pd.DataFrame()
    
    cust_name = cust_res.data[0]['full_name']
    greeting = f"### Namaste, {cust_name} ji! Great to see you again."
    
    # Fetch Order History with joined product name
    order_res = supabase.table("orders").select(
        "order_id, order_date, qty_kg, status, products(sweet_name)"
    ).eq("cust_phone", phone_number).execute()
    
    if not order_res.data:
        return greeting, pd.DataFrame(columns=["Order ID", "Date", "Product", "Qty (kg)", "Status"])

    df = pd.DataFrame(order_res.data)
    # Flatten product name
    df['Product'] = df['products'].apply(lambda x: x['sweet_name'] if x else "MishTee Sweet")
    df = df[['order_id', 'order_date', 'Product', 'qty_kg', 'status']]
    df.columns = ["Order ID", "Date", "Product", "Qty (kg)", "Status"]
    
    return greeting, df

def get_trending_products():
    """Retrieves the top 4 best-selling products."""
    res = supabase.table("orders").select("qty_kg, products(sweet_name, variant_type, price_per_kg)").execute()
    
    if not res.data:
        return pd.DataFrame(columns=["Product", "Type", "Price", "Total Sold"])

    raw_df = pd.DataFrame(res.data)
    raw_df['Product'] = raw_df['products'].apply(lambda x: x['sweet_name'])
    raw_df['Type'] = raw_df['products'].apply(lambda x: x['variant_type'])
    raw_df['Price'] = raw_df['products'].apply(lambda x: x['price_per_kg'])
    
    trending = raw_df.groupby(['Product', 'Type', 'Price'])['qty_kg'].sum().reset_index()
    trending = trending.sort_values(by='qty_kg', ascending=False).head(4)
    trending.columns = ["Product", "Type", "₹/kg", "Total Sold (kg)"]
    
    return trending

# --- 3. GRADIO UI LAYOUT ---

with gr.Blocks(css=mishtee_css, title="MishTee-Magic | Customer Portal") as demo:
    
    # Header Section
    with gr.Column(elem_id="header-container"):
        gr.Image(LOGO_URL, show_label=False, container=False, width=200, interactive=False)
        gr.Markdown(f"<div style='text-align: center; font-style: italic; color: #555;'>{brand_slogan}</div>")
    
    gr.HTML("<br>")

    # Welcome & Login Logic
    with gr.Row(variant="panel"):
        with gr.Column(scale=2):
            phone_input = gr.Textbox(
                label="Enter Registered Phone Number", 
                placeholder="e.g., 98250XXXXX",
                max_lines=1
            )
            login_btn = gr.Button("🔓 Access My Portal", variant="primary")
        with gr.Column(scale=3):
            greeting_output = gr.Markdown("### Welcome to MishTee-Magic")

    gr.HTML("<br>")

    # Data Display (Tabbed View for Minimalist Look)
    with gr.Tabs():
        with gr.TabItem("📜 My Order History"):
            history_table = gr.Dataframe(interactive=False)
            
        with gr.TabItem("🔥 Trending Today"):
            trending_table = gr.Dataframe(interactive=False)

    # Trigger Logic
    def on_login(phone):
        greeting, history_df = get_customer_portal_data(phone)
        trending_df = get_trending_products()
        return greeting, history_df, trending_df

    login_btn.click(
        fn=on_login,
        inputs=phone_input,
        outputs=[greeting_output, history_table, trending_table]
    )

if __name__ == "__main__":
    demo.launch()
