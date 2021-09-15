import streamlit as st
import page
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        '''
        Constructor is a dictionary object where:
        key = title of page
        value = page object
        '''
        self.pages = {} 
    
    def add_page(self, title:str, page:page.Page) -> None: 
        self.pages[title] = page
        
    def run(self):
        # Dropdown to select the page to run  
        st.sidebar.title('App Navigation')
        selected_title = st.sidebar.radio("Go to", list(self.pages.keys()))
        
        # run the app function 
        self.pages[selected_title].load_page()