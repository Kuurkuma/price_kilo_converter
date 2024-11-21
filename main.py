import streamlit as st
import pandas as pd
import requests

# Titles
st.title("Price Converter")
st.write("Convert weight & currencies")
st.write("~~*-*-~~")

# app layout

col1, col2 = st.columns(2)

# Function to calculate price per kilogram
def price_per_kg(price: float, weight: float) -> float:
    if weight > 0 and price > 0:
        price_per_gram = price / weight
        return round(price_per_gram * 1000, 2)
    else:
        return None

# Function to convert MXN to EUR
def mxn_to_euro(price_kg_mxn, eur_rate):
    return round(price_kg_mxn * eur_rate, 2)


# User inputs
price = st.number_input("Enter price in MXN:", min_value=0)
weight = st.number_input("Enter weight in grams:", min_value=1)

# Fetch exchange rate
if 'eur_rate' not in st.session_state:  # Cache the exchange rate to avoid repeated API calls
    response = requests.get('https://api.exchangerate-api.com/v4/latest/MXN')
    if response.status_code == 200:
        data = response.json()
        st.session_state['eur_rate'] = data['rates']['EUR']
    else:
        st.error("Failed to fetch exchange rate.")
        st.stop()

eur_rate = st.session_state['eur_rate']

# Calculate button
if st.button("Calculate"):

    price_kg_mxn = price_per_kg(price, weight)
    st.success(f"The price per kilo is {price_kg_mxn} MXN.")
    
    # Convert price to EUR
    price_kg_euro = mxn_to_euro(price_kg_mxn, eur_rate)
    st.success(f"The price per kilo in EUR is €{price_kg_euro}.")

    # add archive 
# add archive 
archive = pd.DataFrame(columns=['Price per Kilo'])
if price_kg_mxn != None:
    archive = archive._append({'Price per Kilo': price_kg_mxn}, ignore_index=True)
    st.session_state['list'] = archive

st.write(archive)

