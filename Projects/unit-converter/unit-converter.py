import streamlit as st

def convert_unit(value, unit_form, unit_to):

    conversions = {
        "meter_kilometer" : 0.001,      # 1 meter = 0.001 kilometer
        "kilometer_meter" : 1000,       # 1 kilometer = 1000 meter
        "gram_kilogram" : 0.001,        # 1 gram = 0.001 kilogram
        "kilogram_gram" : 1000,         # 1 kilogram = 1000 gram
    }

    key = f"{unit_form}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else: 
        return "Conversion not supported"
    
st.title("Unit Converter - Kashan Malik")

value = st.number_input("Enter the value to convert:")

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted Value:{result}")
