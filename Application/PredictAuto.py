import streamlit as st
from joblib import load
import pandas as pd


def load_model(file):
    model = load(file)
    return model


def upload_predict_page():
    st.title("Prédire la prime que vous pouvez recevoir")

    st.header("Prédiction des fréquences")
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender1")
        occupation = st.selectbox(
            "Occupation",
            ["Employed", "Self-employed", "Housewife", "Unemployed", "Retired"],
            key="occupation1",
        )
        age = st.number_input(
            "Age", min_value=0, max_value=100, value=25, step=1, key="age1"
        )

    with col2:
        bonus = st.number_input(
            "Bonus", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="bonus1"
        )
        data_type = st.selectbox("Type", ["A", "B", "C", "D", "E", "F"], key="type1")
        indtpbi = st.number_input(
            "Indtpbi",
            min_value=None,
            max_value=None,
            value=0.0,
            step=0.01,
            format="%.2f",
            key="indtpbi",
        )

    submit1 = st.button("Prédire votre fréquence corporel", key="predict1")

    if submit1:
        model1 = load_model("Models/model_frequence_corporel.joblib")
        df1 = pd.DataFrame(
            [[gender, occupation, age, bonus, data_type, indtpbi]],
            columns=["Gender", "Occupation", "Age", "Bonus", "Type", "Indtpbi"],
        )
        prediction1 = model1.predict(df1)
        st.success(f"Résultat de la prédiction : {prediction1[0]}")

    indtppd = st.number_input(
        "Indtppd",
        min_value=None,
        max_value=None,
        value=0.0,
        step=0.01,
        format="%.2f",
        key="indtppd",
    )

    submit2 = st.button("Prédire votre fréquence materiel", key="predict2")

    if submit2:
        model2 = load_model("Models/model_frequence_materiel.joblib")
        df2 = pd.DataFrame(
            [[gender, occupation, age, bonus, data_type, indtpbi]],
            columns=["Gender", "Occupation", "Age", "Bonus", "Type", "Indtppd"],
        )
        prediction2 = model2.predict(df2)
        st.success(f"Résultat de la prédiction : {prediction2[0]}")

    st.header("Prédiction des coûts")
    col3, col4 = st.columns(2)

    with col3:
        category = st.selectbox(
            "Category", ["Large", "Medium", "Small"], key="category2"
        )
        polNum = st.number_input(
            "PolNum", min_value=1900, max_value=2100, value=2020, step=1, key="ploNum2"
        )
        calYear = st.number_input(
            "CalYear",
            min_value=1900,
            max_value=2100,
            value=2020,
            step=1,
            key="calYear2",
        )
        adind = st.selectbox("Adind", [0, 1], key="adind2")

    with col4:
        density = st.number_input(
            "Density",
            min_value=None,
            max_value=None,
            value=0.0,
            step=0.01,
            format="%.2f",
            key="density2",
        )
        exppdays = st.number_input(
            "Exppdays",
            min_value=None,
            max_value=None,
            value=0.0,
            step=0.01,
            format="%.2f",
            key="exppdays2",
        )
        numtpbi = st.number_input("Numtpbi", min_value=0, value=0, key="numtpbi2")
        numtppd = st.number_input("Numtppd", min_value=0, value=0, key="numtppd2")
    group1 = st.number_input(
        "Group1", min_value=1, max_value=20, value=10, step=1, key="group1"
    )

    submit3 = st.button("Prédire les coûts corporels", key="predict3")

    if submit3:
        model3 = load_model("Models/model_couts_corporels.joblib")
        df3 = pd.DataFrame(
            [
                [
                    gender,
                    data_type,
                    category,
                    occupation,
                    polNum,
                    calYear,
                    age,
                    adind,
                    density,
                    bonus,
                    exppdays,
                    numtpbi,
                    indtppd,
                    numtppd,
                ]
            ],
            columns=[
                "Gender",
                "Type",
                "Category",
                "Occupation",
                "PolNum",
                "CalYear",
                "Age",
                "Adind",
                "Density",
                "Bonus",
                "Exppdays",
                "Numtpbi",
                "Indtppd",
                "Numtppd",
            ],
        )
        prediction3 = model3.predict(df3)
        st.success(f"Résultat de la prédiction : {prediction3[0]}")

    submit4 = st.button("Prédire les couts materiels", key="predict4")

    if submit4:
        model4 = load_model("Models/model_couts_materiels.joblib")
        df4 = pd.DataFrame(
            [
                [
                    data_type,
                    category,
                    polNum,
                    calYear,
                    age,
                    adind,
                    density,
                    bonus,
                    exppdays,
                    group1,
                    numtpbi,
                    indtppd,
                    numtppd,
                ]
            ],
            columns=[
                "Type",
                "Category",
                "PolNum",
                "CalYear",
                "Age",
                "Adind",
                "Density",
                "Bonus",
                "Exppdays",
                "Group1",
                "Numtpbi",
                "Indtpbi",
                "Numtppd",
            ],
        )
        prediction4 = model4.predict(df4)
        st.success(f"Résultat de la prédiction : {prediction4[0]}")
