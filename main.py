import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Apply Full Black Background & White Text
dark_style = """
    <style>
    body, .stApp {
        background-color: black !important;
                }
    .stTextInput, .stNumberInput, .stSelectbox, .stButton {
        background-color: #222 !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background-color: black !important;
        color: white !important;
        border: 2px solid white !important;
        padding: 8px;
        border-radius: 8px;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
    }
    .stMarkdown, .stSuccess, .stError, .stAlert {
        color: white !important;
    }
    </style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🔄 Advanced Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px;'>Developed By Ahmed Memon</p>", unsafe_allow_html=True)

# Categories
categories = {
    "Length": ["kilometer", "meter", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch", "nautical_mile"],
    "Mass": ["kilogram", "gram", "milligram", "microgram", "ton", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour", "knot"],
    "Area": ["square_meter", "square_kilometer", "square_mile", "square_yard", "square_foot", "square_inch", "hectare", "acre"],
    "Volume": ["liter", "milliliter", "cubic_meter", "cubic_foot", "cubic_inch", "gallon", "quart", "pint", "cup", "fluid_ounce"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "kilowatt_hour"],
    "Pressure": ["pascal", "bar", "psi", "atmosphere"],
    "Power": ["watt", "kilowatt", "horsepower"],
    "Digital Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"],
    "Fuel Economy": ["kilometers_per_liter", "miles_per_gallon"]
}

# Select category
category = st.selectbox("📂 Select a Category", list(categories.keys()))

# Select units
units = categories[category]
col1, col2 = st.columns(2)
from_unit = col1.selectbox("🔹 Convert From", units)
to_unit = col2.selectbox("🔸 Convert To", units)

# Input value
value = st.number_input("🔢 Enter Value", min_value=0.0, step=0.1, value=1.0)

# Convert button
if st.button("🔄 Convert Now"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"✅ {value} {from_unit} = {result.magnitude:.4f} {to_unit}")
    except Exception as e:
        st.error("❌ Invalid conversion! Units must be from the same category.")
