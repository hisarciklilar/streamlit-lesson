import streamlit as st

class MultiPage:
    """
    A class to manage multiple pages in a Streamlit app.
    """
    
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name
        st.set_page_config(
            page_title=self.app_name, 
            page_icon = "💻"
            )
        
    def app_page(self, title, func) -> None:
        """
        Add a new page to the app.
        
        :param title: Title of the page.
        :param func: Function that renders the page content.
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Run the app and display the selected page.
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page["title"])
        page["function"]()
