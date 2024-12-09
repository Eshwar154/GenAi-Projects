from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Configure the Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the updated Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to load the new Gemini model and get response
def get_gemini_response(input_text, image):
    """Get response from Gemini model."""
    # Ensure the input_text is non-empty
    if not input_text:
        input_text = "Describe the uploaded image."

    # Prepare request with the text parameter
    if image:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(input_text)

    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Application")
st.header("Gemini Application")

input_text = st.text_input("Input Prompt: ", key="input", placeholder="Enter a prompt (e.g., 'Describe this image').")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None  # Initialize the image as None

if uploaded_file is not None:
    # Convert the uploaded file to a PIL image
    image = Image.open(io.BytesIO(uploaded_file.read()))
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the image")

# If submit is clicked
if submit:
    try:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")


