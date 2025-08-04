import streamlit as st
from embajadores import embajadores
import urllib.parse

st.set_page_config(page_title="Sumate como socio aportante", layout="centered")

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

st.markdown("Más de 600 chicos entrenan y estudian en el club gracias al aporte de personas como vos. Hacé posible que un joven siga disfrutando del rugby. Con tu aporte ayudás a cubrir parte de la cuota de quien hoy no puede afrontarla y promovés su formación deportiva y personal.")
st.markdown("## Elegí un monto para donar")
st.markdown('<div class="footer">El link redirige al sitio de donación segura a través de Mercado Pago. Podés cancelarla cuando quieras.</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.link_button("$20K", data["links"]["20000"])
    st.link_button("$60.000", data["links"]["60000"])
with col2:
    st.link_button("$40.000", data["links"]["40000"])
    st.link_button("Monto libre", data["links"]["libre"])

st.caption("Gracias por confiar en lo que hacemos ❤️")

st.markdown(
    f"<div style='text-align: center; margin-top: 2rem;'>"
    f"<img src='logovrc.png' width='100'>"
    f"</div>",
    unsafe_allow_html=True
)



