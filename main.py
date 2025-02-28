import streamlit as st

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
    </style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🔄 Advanced Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px;'>Developed By Ahmed Memon</p>", unsafe_allow_html=True)

# Conversion dictionary (multipliers to base unit)
conversion_factors = {
    "Length": {
        "meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001,
        "micrometer": 1e-6, "nanometer": 1e-9, "mile": 1609.34, "yard": 0.9144,
        "foot": 0.3048, "inch": 0.0254, "nautical_mile": 1852
    },
    "Mass": {
        "kilogram": 1, "gram": 0.001, "milligram": 1e-6, "microgram": 1e-9,
        "ton": 1000, "pound": 0.453592, "ounce": 0.0283495
    },
    "Temperature": {
        "celsius": lambda x: x, "fahrenheit": lambda x: (x - 32) * 5/9,
        "kelvin": lambda x: x - 273.15
    },
    "Time": {
        "second": 1, "minute": 60, "hour": 3600, "day": 86400
    },
    "Speed": {
        "meter_per_second": 1, "kilometer_per_hour": 0.277778,
        "mile_per_hour": 0.44704, "knot": 0.514444
    },
    "Area": {
        "square_meter": 1, "square_kilometer": 1e6, "square_mile": 2.59e6,
        "square_yard": 0.836127, "square_foot": 0.092903,
        "square_inch": 0.00064516, "hectare": 10000, "acre": 4046.86
    },
    "Volume": {
        "liter": 1, "milliliter": 0.001, "cubic_meter": 1000,
        "cubic_foot": 28.3168, "cubic_inch": 0.0163871,
        "gallon": 3.78541, "quart": 0.946353, "pint": 0.473176,
        "cup": 0.24, "fluid_ounce": 0.0295735
    },
    "Energy": {
        "joule": 1, "kilojoule": 1000, "calorie": 4.184, "kilocalorie": 4184,
        "watt_hour": 3600, "kilowatt_hour": 3.6e6
    },
    "Pressure": {
        "pascal": 1, "bar": 100000, "psi": 6894.76, "atmosphere": 101325
    },
    "Power": {
        "watt": 1, "kilowatt": 1000, "horsepower": 745.7
    },
    "Digital Storage": {
        "bit": 1, "byte": 8, "kilobyte": 8000, "megabyte": 8e6,
        "gigabyte": 8e9, "terabyte": 8e12, "petabyte": 8e15
    },
    "Fuel Economy": {
        "kilometers_per_liter": 1, "miles_per_gallon": 0.425144
    }
}

# Select category
category = st.selectbox("📂 Select a Category", list(conversion_factors.keys()))

# Select units
units = list(conversion_factors[category].keys())
col1, col2 = st.columns(2)
from_unit = col1.selectbox("🔹 Convert From", units)
to_unit = col2.selectbox("🔸 Convert To", units)

# Input value
value = st.number_input("🔢 Enter Value", min_value=0.0, step=0.1, value=1.0)

# Convert function
def convert(value, from_unit, to_unit, category):
    try:
        if category == "Temperature":
            base_value = conversion_factors[category][from_unit](value)
            return base_value if to_unit == "celsius" else (
                base_value * 9/5 + 32 if to_unit == "fahrenheit" else base_value + 273.15
            )
        else:
            base_value = value * conversion_factors[category][from_unit]  # Convert to base unit
            return base_value / conversion_factors[category][to_unit]  # Convert to target unit
    except:
        return None

# Convert button
if st.button("🔄 Convert Now"):
    result = convert(value, from_unit, to_unit, category)
    if result is not None:
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
    else:
        st.error("❌ Invalid conversion! Units must be from the same category.")
