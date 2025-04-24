# 🤖 AI Chatbot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License](https://img.shields.io/github/license/AmitGhosh2005/Ai_chatbot)

A smart and interactive **AI-powered chatbot** that uses simple Natural Language Processing (NLP) techniques to understand and respond to user input. This project is designed as a beginner-friendly Python chatbot and can be extended with advanced NLP or machine learning models.

---

## 🚀 Features

- ✨ Engages in basic human-like conversations
- 🧠 Rule-based NLP approach
- 📁 Easily customizable response patterns
- ⚙️ Lightweight with minimal dependencies
- 💬 Console-based interaction

---

## 📁 Project Structure

1. Backend Technology:
Python: The primary programming language for this project.

2. Machine Learning / AI:
Transformers: The BlipProcessor and BlipForConditionalGeneration models are from the Transformers library by Hugging Face, which is used for vision-and-language tasks (image captioning in this case).

PyTorch: You are using PyTorch as the deep learning framework for model inference (BLIP model).

BLIP (Bootstrapping Language-Image Pretraining): This is the model that generates captions based on the input image.

3. Image Processing:
Pillow (PIL): Used for image loading, conversion, and displaying in the Streamlit interface.

4. Web Framework:
Streamlit: A framework for building interactive web apps. In your project, it provides the user interface (uploading images, displaying results) and serves the app in the browser.

5. Frontend Technology:
HTML/CSS (via Streamlit’s markdown): Used for styling the app’s UI. The styling is injected using Streamlit markdown with custom CSS for layout, buttons, and fonts.

6. Caching:
Streamlit Caching (@st.cache_resource): Used to cache the model loading function, so the model isn’t reloaded every time the user interacts with the app.

In Summary:
Programming Language: Python

AI/ML Libraries: Transformers, PyTorch

Image Processing: Pillow (PIL)

Web Framework: Streamlit

Styling: HTML/CSS (via Streamlit)

These are the main technology stacks you've used in your project!