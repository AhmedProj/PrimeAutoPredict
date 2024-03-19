import streamlit as st
import CaptureDegats, Home, PredictAuto


def main():
    st.sidebar.title("Menu")
    PAGES = {
        "🏠 Home": Home,
        "🔍 PredictAuto": PredictAuto,
        "📷 CaptureDégats": CaptureDegats,
    }


    page_name = st.sidebar.radio("", list(PAGES.keys()))
    page = PAGES[page_name]
    with st.spinner(f"Chargement de {page_name} ..."):
        page.upload_predict_page()


if __name__ == "__main__":
    main()
