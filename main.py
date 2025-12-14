import streamlit as st
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

st.set_page_config(layout="wide")
st.title("🌍 Mapa Olist - Arquivos Locais")

# Carregar direto do arquivo local
try:
    geolocation_df = pd.read_csv("olist_geolocation_dataset.csv")
    st.success(f"✅ {len(geolocation_df):,} linhas carregadas localmente!")
    
    # Seu mapa original
    mapa = folium.Map(
        location=[geolocation_df['geolocation_lat'].mean(), 
                 geolocation_df['geolocation_lng'].mean()], 
        zoom_start=5, 
        tiles='CartoDB dark_matter'
    )
    
    # Limitar pontos para performance
    sample = geolocation_df.dropna().head(5000)
    data = list(zip(sample['geolocation_lat'], sample['geolocation_lng']))
    FastMarkerCluster(data).add_to(mapa)
    
    # Mostrar mapa
    st.components.v1.html(mapa.get_root().render(), width=1300, height=700)
    
except FileNotFoundError:
    st.error("Arquivo 'olist_geolocation_dataset.csv' não encontrado")
    st.info("""
    **Faça isso:**
    1. Baixe de: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
    2. Extraia o arquivo CSV
    3. Suba para esta pasta no GitHub
    4. Recarregue o app
    """)
