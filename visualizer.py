import streamlit as st
import login_page
import webbrowser
def app():
    
    if(login_page.signed==True):
        st.subheader('Analytical View')
        if st.button("view"):
            webbrowser.open('https://app.powerbi.com/groups/me/reports/5df383ea-aaad-4b01-b149-ddefc3bae9fb/ReportSection?experience=power-bi')
            #https://app.powerbi.com/groups/me/reports/5df383ea-aaad-4b01-b149-ddefc3bae9fb/ReportSection?experience=power-bi
    else:
        st.subheader('Login First!')