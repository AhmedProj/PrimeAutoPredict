import streamlit as st
from PIL import Image
import torch
import numpy as np
from model_functions import predict


def load_image(image_file):
    img = Image.open(image_file)
    return img


def upload_predict_page():
    st.title("👋 **Hello**! Entrez votre image")
    st.header("**Et** on évaluera les dégâts de votre véhicule")

    uploaded_file = st.file_uploader(
        "Choisissez une image à uploader", type=["jpg"]
    )
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        st.image(image, caption="Image téléchargée.", use_column_width=True)
        if st.button("Prédire"):
            prediction = predict(uploaded_file)
            prediction_list = prediction.numpy().tolist()[0]
            col1, col2, col3 = st.columns(3)

            with col1:
                st.success(
                    f"Votre vehicule est à **{prediction_list[0]*100:.1f}%** de dégâts mineures."
                )
            with col2:
                st.warning(
                    f"Votre vehicule est à **{prediction_list[1]*100:.1f}%** de dégâts modérés."
                )
            with col3:
                st.error(
                    f"Votre vehicule est à **{prediction_list[2]*100:.1f}%** de dégâts sévères"
                )
    else:
        st.warning("Veuillez télécharger une image avant de prédire.", icon="⚠️")
