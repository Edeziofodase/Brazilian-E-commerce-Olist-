import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("✅ PRIMEIRO: Verifique se o básico funciona")

st.write("1. Streamlit funciona? ✅")
st.write("2. Vamos testar um gráfico simples:")

# Dados mínimos
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 15, 25, 30]
})

st.line_chart(data.set_index('x'))

st.success("Se você vê o gráfico acima, o Streamlit está funcionando!")

# Só então tente o mapa
if st.button("Agora sim, mostrar mapa simples"):
    import folium
    
    # Mapa mínimo
    m = folium.Map(location=[-15, -55], zoom_start=4)
    folium.Marker([-23.55, -46.63], popup='São Paulo').add_to(m)
    folium.Marker([-22.90, -43.17], popup='Rio').add_to(m)
    
    st.components.v1.html(m.get_root().render(), width=800, height=500)
