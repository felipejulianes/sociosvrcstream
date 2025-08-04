import streamlit as st
from embajadores import embajadores
import urllib.parse

st.set_page_config(page_title="Sumate como socio aportante", layout="centered")

st.markdown("""
    <style>
        body, .stApp {
            background-color: #237d33 !important;
            color: white !important;
        }

        h1, h2, h3, h4, h5, h6, p, div, span {
            color: white !important;
        }

        /* Forzar botones horizontales iguales */
        .stButton button {
            background-color: white !important;
            color: black !important;
            font-weight: bold !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.2rem !important;
            width: 100% !important;
            height: 3rem !important;
            font-size: 1.1rem !important;
        }

        .stButton button:hover {
            background-color: #fbca0c !important;
            color: black !important;
        }

        /* Extra: prevenir que el texto blanco sobrescriba botones */
        a, .stLinkButton {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)



# Leer parámetro de la URL

query_params = st.query_params
embajador_key = query_params.get("embajador", None)

if not embajador_key or embajador_key not in embajadores:
    st.error("Embajador no encontrado. Agregá `?embajador=marcos` al link.")
    st.stop()

data = embajadores[embajador_key]

st.title("Sumate como socio aportante")
st.image(data["imagen"], use_container_width=True)
st.subheader(data["nombre"])
st.write(data["mensaje"])

st.markdown("Hacé posible que un joven siga disfrutando del rugby. Con tu aporte ayudás a cubrir parte de la cuota de quien hoy no puede afrontarla y promovés su formación deportiva y personal.")
st.markdown("## Elegí un monto para donar")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("$20K", data["links"]["20000"])
with col2:
    st.link_button("$40.000", data["links"]["40000"])
with col3:
    st.link_button("$60.000", data["links"]["60000"])
with col4:
    st.link_button("Monto libre", data["links"]["libre"])


st.caption("Gracias por confiar en lo que hacemos ❤️")
