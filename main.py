import streamlit as st
import requests

st.title("Price per Kg calculator")
st.write("Buy smarter by knowing the price per kilo")

price = st.number_input("Enter the price of the product (in MXN)")
weight = st.number_input("Enter the weight of the product")

# create a converter function to price per kilo
def converter_kg(price,weight):
    result = round(price/weight,2)
    return result

price_kg_mxn = st.button("Calculate")
if price_kg_mxn:
    result = converter_kg(price, weight)
    st.success(f"The price per kilo is {result}, MXN")

# converter mxn to euro
response = requests.get('https://api.exchangerate-api.com/v4/latest/MXN')
data = response.json()

eur_rate = data['rates']['EUR']

def mxn_to_euro(price_kg_mxn):
    r= price_kg_mxn/eur_rate
    
price_kg_euro = mxn_to_euro(price_kg_mxn)


