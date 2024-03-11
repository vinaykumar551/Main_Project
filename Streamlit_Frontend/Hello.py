import streamlit as st
from PIL import Image
# Set page config
st.set_page_config(
    page_title="MAIN PROJECT",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Header with image
# st.image("image2.jpg", use_column_width=True)  # Replace "your_image.png" with the path to your image file
st.write("## 🌟 Welcome to Diet recommendation system! 🌟")
st.write("---")

# Sidebar
st.sidebar.success("Select a recommendation app ☝️")

# Main content
st.write("### About Our Project")
st.write("Where we have done a diet recommendation web application using a content-based approach with Scikit-Learn, FastAPI, and Streamlit.")
st.write("---")

st.image("image.jpg", width=600)

# Styling with CSS
st.markdown(
    """
    <style>
    .st-c7 {
        color: #FF0000; /* Set color for title (red) */
    }
    .st-b1 {
        background-color: #000000; /* Set background color for sidebar (black) */
        color: #FFFFFF; /* Set text color for sidebar (white) */
    }
    .st-da {
        color: #000000; /* Set text color for main content (black) */
    }
    </style>
    """,
    unsafe_allow_html=True
)
