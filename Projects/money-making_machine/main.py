import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 100)

st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustle?apiKey=101")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return("Freelancing")

    except:
        return(st.warning("Something went wrong !!!"))
    
st.subheader("Side Hustle Ideas")

if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.info(idea)

def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quote?apiKey=101")
        if response.status_code == 200:
            quote = response.json()
            return quote["money_quote"]
        else:
            return("I'm not rich enough to buy anything")

    except:
        return(st.warning("Something went wrong !!!"))

st.subheader("Money Making Motivation")

if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.info(quote)