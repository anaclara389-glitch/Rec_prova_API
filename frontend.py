import streamlit as st
from consumidor_api import consultar_clima

st.set_page_config(
    page_title="Estação Meteorológica",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Estação Meteorológica")
st.write("Monitoramento das condições ambientais")
st.caption("São Paulo - SP")

st.divider()

try:
    with st.spinner("Obtendo informações meteorológicas..."):
        dados = consultar_clima()

    st.success("Consulta realizada com sucesso!")

    st.subheader("🌡️ Clima São Paulo")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5 = st.columns(1)

    col1.metric(
        "Temperatura do ar",
        f"{dados["current"]['temperature_2m']:.1f} °C"
    )

    col2.metric(
        "Sensação térmica",
        f"{dados["current"]['apparent_temperature']:.1f} °C"
    )

    col3.metric(
        "Precipitação",
        f"{dados["current"]['precipitation']:.1f} mm"
    )

    col4.metric(
        "Velocidade do vento",
        f"{dados["current"]['wind_speed_10m']:.1f} km/h"
    )

    st.divider()

except:
    print("Tente novamente")
