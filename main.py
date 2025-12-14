# NOVO CÓDIGO para quando o arquivo estiver no GitHub
import pandas as pd
import streamlit as st

@st.cache_data
def load_local_data():
    """Carrega dados do arquivo local no GitHub"""
    try:
        # Tenta carregar do arquivo local
        df = pd.read_csv('olist_geolocation_dataset.csv', encoding='utf-8')
        return df
    except:
        # Fallback para dados de exemplo
        return pd.DataFrame({
            'geolocation_lat': [-23.5505, -22.9068],
            'geolocation_lng': [-46.6333, -43.1729]
        })

# Uso
geolocation_df = load_local_data()
st.write(f"Dados carregados: {len(geolocation_df)} linhas")
