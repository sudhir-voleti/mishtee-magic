# High-End Minimalist CSS for MishTee-Magic
mishtee_css = """
/* Import Premium Typography */
@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400&display=swap');

/* Main Container: Off-White & High Whitespace */
.gradio-container {
    background-color: #FAF9F6 !important;
    font-family: 'Inter', sans-serif !important;
    padding: 40px !important;
}

/* Headings: Spaced-out Serif (Bodoni) */
h1, h2, h3 {
    font-family: 'Bodoni Moda', serif !important;
    color: #333333 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.15em !important;
    font-weight: 400 !important;
    margin-bottom: 30px !important;
    border-bottom: 1px solid #333333;
    display: inline-block;
    padding-bottom: 5px;
}

/* Dataframes/Tables: Lightweight Sans-Serif & Sharp Lines */
table {
    border-collapse: collapse !important;
    width: 100% !important;
    margin-top: 20px !important;
    background-color: transparent !important;
    border: 1px solid #333333 !important; /* Sharp thin border */
}

table th {
    background-color: #FAF9F6 !important;
    color: #333333 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    font-size: 0.75rem !important;
    padding: 15px !important;
    border-bottom: 1px solid #333333 !important;
}

table td {
    font-family: 'Inter', sans-serif !important;
    font-weight: 300 !important;
    padding: 12px 15px !important;
    color: #333333 !important;
    border-bottom: 1px solid #EEEEEE !important;
}

/* Buttons: Sober Terracotta & Sharp Rectangles */
button.primary {
    background-color: #C06C5C !important; /* Sober Terracotta */
    color: #FAF9F6 !important;
    border: 1px solid #C06C5C !important;
    border-radius: 0px !important; /* Sharp lines, no rounding */
    padding: 12px 30px !important;
    font-family: 'Inter', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 0.2em !important;
    font-size: 0.8rem !important;
    transition: all 0.4s ease !important;
    box-shadow: none !important; /* No shadows per constraint */
}

button.primary:hover {
    background-color: #FAF9F6 !important;
    color: #C06C5C !important;
    border: 1px solid #C06C5C !important;
}

/* Input Fields: Minimalist Underline Style */
input, textarea {
    background-color: transparent !important;
    border: none !important;
    border-bottom: 1px solid #333333 !important; /* Only bottom border for professional feel */
    border-radius: 0px !important;
    padding: 10px 0px !important;
    box-shadow: none !important;
}

/* Remove default Gradio component shadows */
.form, .gradio-group {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}

/* Layout Padding */
.gap {
    gap: 40px !important;
}
"""
