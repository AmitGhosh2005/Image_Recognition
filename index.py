import streamlit as st


st.set_page_config(
    page_title="AI Image Captioning",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

st.markdown("""
    <style>
        .main {
            background-color: #f2f4f7;
            color: #333;
            padding: 2rem;
        }
        .title {
            font-size: 2.5rem;
            text-align: center;
            font-weight: bold;
            color: #1a1a1a;
        }
        .caption {
            font-size: 1.3rem;
            text-align: center;
            margin-top: 20px;
            color: #004d40;
            background-color: #e0f2f1;
            padding: 15px;
            border-radius: 10px;
        }
        .footer {
            font-size: 0.8rem;
            text-align: center;
            margin-top: 3rem;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .gradient-text {
            font-size: 2.7rem;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    <div class='gradient-text'>🖼️ AI-Powered Image Caption Generator</div>
""", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)


    with st.spinner("Generating caption..."):
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

    st.markdown(f"<div class='caption'>📣 <b>Generated Caption:</b><br>{caption}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Built with ❤️ by team TechNerds</div>", unsafe_allow_html=True)
