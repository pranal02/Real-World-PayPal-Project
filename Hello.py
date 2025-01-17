import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load Lottie animation
lottie_animation = load_lottie_url("https://assets6.lottiefiles.com/packages/lf20_jv3fpaxx.json")  # Replace with your preferred animation URL

# Page Configurations
st.set_page_config(
    page_title="Welcome to PayPal Reviews",
    page_icon="👋",
    layout="centered",
)

# Add a banner or logo
image = Image.open('https://cdn-icons-png.flaticon.com/512/5932/5932535.png')  # Replace with your banner/logo path
st.image(image, use_column_width=True)

# Title
st.title("Welcome to PayPal Reviews 🎉")

# Animation Section
if lottie_animation:
    st_lottie(lottie_animation, height=300, key="intro")

# Introduction Section
st.markdown(
    """
    <div style="background-color:#f4f4f9; padding: 20px; border-radius: 8px;">
    <h3 style="color:#0d6efd;">📊 Explore Our Applications</h3>
    <p style="font-size:16px;">These two applications (Transactions and Graphs) are designed to help you review PayPal-related customer transactions with ease and efficiency.</p>
    <h4 style="color:#0d6efd;">👈 Select an app from the sidebar to get started.</h4>
    </div>
    """, 
    unsafe_allow_html=True
)

# Info Message with Enhancements
st.info(
    """
    **⚠️ Notice: Application May Take a Few Moments to Load**

    Thank you for accessing this application! Please note that the server hosting this app 
    is currently in a **sleep mode** due to resource optimizations. When the app is not 
    actively used, it temporarily enters a hibernation state to conserve resources.

    As a result, the app may take **10–30 seconds** to wake up and fully load after you access it. 
    Once active, it will run smoothly without further delays.

    We appreciate your patience and understanding. If you experience any issues, 
    feel free to refresh the page or try again later.
    """
)

# Add More Engagement Options
st.markdown(
    """
    <div style="background-color:#e9ecef; padding: 20px; border-radius: 8px; margin-top: 20px;">
    <h4 style="color:#0d6efd;">📚 Want to Learn More?</h4>
    <ul style="font-size:16px;">
        <li>Watch the [YouTube Video](https://youtube.com)</li>
        <li>Follow on [Twitter](https://twitter.com/RyanNolanData)</li>
        <li>Discover our [Documentation](https://docs.streamlit.io)</li>
    </ul>
    </div>
    """, 
    unsafe_allow_html=True
)


