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
            "Profession du conducteur ",
            ["Employed", "Self-employed", "Housewife", "Unemployed", "Retired"],
            key="occupation1",
        )
        age = st.number_input(
            "Age", min_value=0, max_value=100, value=25, step=1, key="age1"
        )

    with col2:
        bonus = st.number_input(
            "Réduction",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.5,
            key="bonus1",
        )
        data_type = st.selectbox(
            "Type : Type du véhicule", ["A", "B", "C", "D", "E", "F"], key="type1"
        )
        indtpbi = st.number_input(
            "Coût total des dommages corporels",
            min_value=None,
            max_value=None,
            value=0.0,
            step=0.01,
            format="%.2f",
            key="indtpbi",
        )

    submit1 = st.button("Prédire votre fréquence corporel", key="predict1")

    prediction1 = None
    if submit1:
        model1 = load_model("model_frequence_corporel.joblib")
        df1 = pd.DataFrame(
            [[gender, occupation, age, bonus, data_type, indtpbi]],
            columns=["Gender", "Occupation", "Age", "Bonus", "Type", "Indtpbi"],
        )
        prediction1 = model1.predict(df1)
        st.success(f"Résultat de la prédiction : {int(prediction1[0])}")

    indtppd = st.number_input(
        "Coût total des réclamations matérielles",
        min_value=None,
        max_value=None,
        value=0.0,
        step=0.01,
        format="%.2f",
        key="indtppd",
    )

    submit2 = st.button("Prédire votre fréquence materiel", key="predict2")

    prediction2 = None
    if submit2:
        model2 = load_model("model_frequence_materiel.joblib")
        df2 = pd.DataFrame(
            [[gender, occupation, age, bonus, data_type, indtpbi]],
            columns=["Gender", "Occupation", "Age", "Bonus", "Type", "Indtppd"],
        )
        prediction2 = model2.predict(df2)
        st.success(f"Résultat de la prédiction : {int(prediction2[0])}")

    st.header("Prédiction des coûts")
    col3, col4 = st.columns(2)

    with col3:
        category = st.selectbox(
            "Categorie de la voiture", ["Large", "Medium", "Small"], key="category2"
        )
        polNum = st.number_input(
            "Numero de contrat",
            min_value=1900,
            max_value=2100,
            value=2020,
            step=1,
            key="ploNum2",
        )
        calYear = st.number_input(
            "Souscription annuelle",
            min_value=1900,
            max_value=2100,
            value=2020,
            step=1,
            key="calYear2",
        )
        adind = st.selectbox("Adind", [0, 1], key="adind2")

    with col4:
        density = st.number_input(
            "Densité de la population",
            min_value=None,
            max_value=None,
            value=0.0,
            step=0.01,
            format="%.2f",
            key="density2",
        )
        exppdays = st.number_input(
            "Exposition au risque (en jours)",
            min_value=None,
            max_value=None,
            value=0.0,
            step=0.01,
            format="%.2f",
            key="exppdays2",
        )
        numtpbi = st.number_input(
            "Nombre de sinistres corporels de tiers",
            min_value=0,
            value=0,
            key="numtpbi2",
        )
        numtppd = st.number_input(
            "Nombre de réclamations matérielles de tiers",
            min_value=0,
            value=0,
            key="numtppd2",
        )
    group1 = st.number_input(
        "Groupe de la voiture",
        min_value=1,
        max_value=20,
        value=10,
        step=1,
        key="group1",
    )

    submit3 = st.button("Prédire les coûts corporels", key="predict3")

    prediction3 = None
    if submit3:
        model3 = load_model("model_couts_corporels.joblib")
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
        st.success(f"Résultat de la prédiction : {int(prediction3[0])}")

    submit4 = st.button("Prédire les couts materiels", key="predict4")

    prediction4 = None
    if submit4:
        model4 = load_model("model_couts_materiels.joblib")
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
        st.success(f"Résultat de la prédiction : {int(prediction4[0])}")

    st.header("Prédiction des Primes 💰")
    st.warning("N'oubliez pas de renseigner les bonnes valeurs avant", icon="⚠️")
    submit5 = st.button("Prédire les primes materielles", key="predict5")
    submit6 = st.button("Prédire les primes corporelles", key="predict6")
    if submit5 or submit6:
        if (
            (prediction4 is not None)
            and (prediction3 is not None)
            and (prediction2 is not None)
            and (prediction1 is not None)
        ):
            st.success(f"Prime corporelle : **{prediction4[0]* prediction1[0]}** euros")
            st.success(f"Prime materielle : **{prediction3[0]* prediction2[0]}** euros")
        else:
            st.error("Veuillez d'abord remplir les valeurs avant", icon="⚠️")
