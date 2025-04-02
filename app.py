import streamlit as st

from scripts.calculation import price_per_kg, get_exchange_rate
from config import CURRENCY_TO_FLAG

# Titles
st.title("Price Converter")
st.write("Convert into price per kilo & currencies")
st.write("__________")

currency_list = [f"{CURRENCY_TO_FLAG[currency]} {currency}"
    for currency in CURRENCY_TO_FLAG.keys()]

# App layout
col1, col2 = st.columns(2)

# User inputs
with col1:
    from_currency = st.selectbox(
                "Select your currency",
                currency_list
                )
    input_price = st.number_input(f"Enter price in {from_currency}:", min_value=0)

with col2:
    to_currency = st.selectbox(
                "Select your destination currency",
                currency_list
                )
    input_weight = st.number_input("Enter weight in grams:", min_value=1)


# Calculate button
if st.button("Calculate"):

    price_per_kg = price_per_kg(input_price, input_weight)

    # Currency conversion
    rate = get_exchange_rate(from_currency, to_currency)
    converted_currency = input_price * rate
    st.success(f"The price per kilo is {price_per_kg} {from_currency}.")
    st.success(f"{converted_currency}")

# add archive
#archive = pd.DataFrame(columns=['Price per Kilo'])
#if price_kg_mxn != None:
#   archive = archive._append({'Price per Kilo': price_kg_mxn}, ignore_index=True)
#    st.session_state['list'] = archive

#st.write(archive)
