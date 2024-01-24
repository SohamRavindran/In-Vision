import streamlit as st
import time
import en_plat
signed=True
def authenticate(username, password):
    valid_username = "admin"
    valid_password = "soham"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def login():
    st.title("Shoppers Central Login")

    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            signed=True
            st.write(signed)
            st.success("Logged in!")
            time.sleep(10)
            
        else:
            st.error("Invalid username or password")
            signed=False

def app():
    login()
