import streamlit as st
from PIL import Image

with st.expander("Start camera"):
# Start camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pilloe image to grayscale 
    grary_img = img.convert("L")

    # Render the grayscale image on the webpag
    st.image(grary_img)