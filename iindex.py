import streamlit as st
import streamlit.components.v1 as components

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Volume": {"Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001, "Gallon": 0.264172, "Pint": 2.11338}
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value  # If same units
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Streamlit UI with Advanced Styling
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-color: black;
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
        }
        .stButton>button {
            background-color: #FFD700;
            color: black;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #FFC107;
        }
        .stSelectbox label, .stNumberInput label {
            color: #FFD700;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

categories = ["Length", "Weight", "Temperature", "Volume"]
category = st.selectbox("Select Category", categories)

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Pint"]
}

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", units[category])
with col2:
    to_unit = st.selectbox("To Unit", units[category])

value = st.number_input("Enter Value", value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.markdown(f"<h3 style='text-align: center; color: #FFD700;'>{value} {from_unit} = {result:.2f} {to_unit}</h3>", unsafe_allow_html=True)
    st.success(f"Conversion successful: {value} {from_unit} = {result:.2f} {to_unit}")
