import streamlit as st
import requests

st.title("Number Sign Checker")

number = st.number_input("Enter a number", step=1.0)

if st.button("Submit"):
    try:
        res = requests.post("http://localhost:5000/set_number", json={"number": number})
        if res.ok:
            st.success(f"Number saved: {number}")
    except requests.exceptions.ConnectionError:
        st.error("Flask API not running. Please start the server.")

if st.button("Check if Negative"):
    try:
        res = requests.get("http://localhost:5000/is_negative")
        if res.ok:
            is_neg = res.json()['is_negative']
            st.info(f"Is the number negative? {'Yes' if is_neg else 'No'}")
    except requests.exceptions.ConnectionError:
        st.error("Flask API not running. Please start the server.")
