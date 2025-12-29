 mishtee_css = """
.gradio-container {
    background-color: #FDF5E6 !important;
    font-family: 'Lora', serif; /* Fallback serif for general text; headings will inherit */
    color: #4A3728; /* Deep warm brown for good contrast on cream background */
    max-width: 100% !important; /* Optional: fuller width for modern feel */
}

h1, h2, h3, h4, h5, .block.title, .gradio-container .label, .block-label {
    font-family: 'Playfair Display', serif !important;
    color: #E2725B !important; /* Terracotta for headings */
    font-weight: 600;
}

body, p, div, span, input, textarea, .gradio-container .prose, table {
    font-family: 'Poppins', system-ui, sans-serif !important; /* Clean modern sans-serif for body and table data */
}

/* Inputs and text areas */
input, textarea, .gradio-container .form {
    background-color: #FFFFFF !important;
    border: 1px solid #E2725B !important; /* Terracotta border */
    border-radius: 8px !important;
    box-shadow: 0 2px 8px rgba(178, 134, 11, 0.1) !important; /* Subtle gold-tinted shadow */
}

/* Primary buttons (submit/run/generate) */
button.primary, .gradio-container button[type="submit"], .gradio-container .button.primary {
    background: linear-gradient(to bottom, #E2725B, #D15A40) !important; /* Terracotta gradient */
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(226, 114, 91, 0.3) !important;
    transition: all 0.3s ease !important;
}

button.primary:hover, .gradio-container button[type="submit"]:hover {
    background: linear-gradient(to bottom, #D15A40, #C04F35) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 16px rgba(226, 114, 91, 0.4) !important;
}

/* Secondary/accent buttons */
button.secondary, .gradio-container button:not(.primary) {
    background: #B8860B !important; /* Burnished Gold */
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    font-weight: 500 !important;
    box-shadow: 0 4px 12px rgba(184, 134, 11, 0.3) !important;
}

button.secondary:hover {
    background: #A67B0A !important;
    transform: translateY(-1px) !important;
}

/* Blocks and panels */
.gradio-container .panel, .gradio-container .block {
    background-color: #FFFFFF !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 20px rgba(184, 134, 11, 0.15) !important; /* Artisanal gold shadow for premium depth */
    border: 1px solid #E2725B22 !important; /* Very subtle terracotta tint */
}

/* Table styling */
table {
    border-collapse: separate !important;
    border-spacing: 0 8px !important;
}

th, td {
    background-color: #FDF5E6 !important; /* Cream for table cells */
    padding: 12px !important;
    border-radius: 8px !important;
}

/* Load Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@400;500;600&family=Lora:wght@400;500&display=swap');
"""
