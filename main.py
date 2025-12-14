import streamlit as st
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

# CONFIGURAÇÃO DA PÁGINA (SEMPRE NO TOPO)
st.set_page_config(layout="wide", page_title="Olist E-commerce")
st.title("🌍 Mapa de Geolocalização Olist")

# 1. CARREGAR DADOS (versão simplificada que funciona)
@st.cache_data
def load_olist_data():
    """Carrega dados do Olist - versão segura"""
    try:
        import kagglehub
        # Baixa UMA VEZ
        dataset_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
        
        # Carrega apenas o necessário para o mapa
        geolocation_df = pd.read_csv(f"{dataset_path}/olist_geolocation_dataset.csv")
        
        return geolocation_df
    except Exception as e:
        st.error(f"Erro: {e}")
        # Fallback: dados de exemplo
        return pd.DataFrame({
            'geolocation_lat': [-23.5505, -22.9068, -19.9167, -15.7939, -3.7319],
            'geolocation_lng': [-46.6333, -43.1729, -43.9333, -47.8828, -38.5267],
            'geolocation_city': ['São Paulo', 'Rio', 'BH', 'Brasília', 'Fortaleza']
        })

# 2. CARREGAR (com indicador visual)
with st.spinner("📥 Carregando dados..."):
    geolocation_df = load_olist_data()

st.success(f"✅ {len(geolocation_df):,} localizações carregadas")

# 3. LIMPAR DADOS (CRUCIAL!)
geolocation_clean = geolocation_df.dropna(subset=['geolocation_lat', 'geolocation_lng'])
geolocation_clean = geolocation_clean[
    (geolocation_clean['geolocation_lat'].between(-35, 5)) &  # Brasil
    (geolocation_clean['geolocation_lng'].between(-75, -30))
]

# 4. CRIAR MAPA
if len(geolocation_clean) > 0:
    mapa = folium.Map(
        location=[geolocation_clean['geolocation_lat'].mean(), 
                 geolocation_clean['geolocation_lng'].mean()],
        zoom_start=5,
        tiles='CartoDB dark_matter'
    )
    
    # Adicionar clusters
    data = list(zip(geolocation_clean['geolocation_lat'], geolocation_clean['geolocation_lng']))
    FastMarkerCluster(data).add_to(mapa)
    
    # 5. EXIBIR MAPA (MÉTODO QUE FUNCIONA)
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
        mapa.save(f.name)
        with open(f.name, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        import os
        os.unlink(f.name)
    
    # Exibir mapa largo
    st.components.v1.html(html_content, width=1200, height=600)
    
else:
    st.warning("Sem dados válidos para o mapa")
