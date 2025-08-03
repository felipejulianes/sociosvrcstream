import streamlit as st
from embajadores import embajadores
import urllib.parse

st.set_page_config(page_title="Sumate como socio aportante", layout="centered")

# Leer parámetro de la URL

query_params = st.query_params
embajador_key = query_params.get("embajador", [None])[0]

if not embajador_key or embajador_key not in embajadores:
    st.error("Embajador no encontrado. Agregá `?embajador=marcos` al link.")
    st.stop()

data = embajadores[embajador_key]

st.title("Sumate como socio aportante")
st.image(data["imagen"], use_column_width=True)
st.subheader(data["nombre"])
st.write(data["mensaje"])

st.markdown("Tu aporte mensual nos permite seguir entrenando, alimentando y acompañando.")
st.markdown("## Elegí un monto para donar")

col1, col2 = st.columns(2)
with col1:
    st.link_button("$20.000", data["links"]["20000"])
    st.link_button("$60.000", data["links"]["60000"])
with col2:
    st.link_button("$40.000", data["links"]["40000"])
    st.link_button("Monto libre", data["links"]["libre"])

st.caption("Gracias por confiar en lo que hacemos ❤️")
