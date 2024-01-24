import streamlit as st
from langchain_helper import get_few_shot_db_chain
from streamlit_option_menu import option_menu
import time
import en_plat
import login_page
import about_page
import visualizer



def main():
     with st.sidebar:        
            app = option_menu(
                menu_title='In-vision',
                options=['Login','enquiry platform','visualizer','about'],
                icons=['house-fill','archive','bar-chart-fill','info-circle-fill'],
                menu_icon='store-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
     if app == "Login":
        login_page.app()
     if app == "enquiry platform":
        en_plat.app()
     if app == "visualizer":
        visualizer.app()
     if app == "about":
        about_page.app()

# Run the application
if __name__ == "__main__":
    main()