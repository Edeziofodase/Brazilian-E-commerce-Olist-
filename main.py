import streamlit as st
import pandas as pd
import math as m
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster
import kagglehub

@st.cache_data
def load_kaggle_dataset():
    """
    Carrega o dataset Olist Brazilian E-commerce do Kaggle
    """
    dataset_path = "olistbr/brazilian-ecommerce"  # Aqui você define o valor
    
    try:
        # Usando kagglehub para baixar o dataset
        path = kagglehub.dataset_download(dataset_path)
        return path
    except Exception as e:
        st.error(f"Erro ao baixar dataset: {e}")
        return None

st.title('Análise Geral')
mapa = folium.Map(location=[dadosg['geolocation_lat'].mean(), dadosg['geolocation_lng'].mean()], zoom_start=5, tiles='CartoDB dark_matter');

data = list(zip(dadosg['geolocation_lat'], dadosg['geolocation_lng']))

FastMarkerCluster(data).add_to(mapa)
mapa.save('mapa_clusters.html') ;

st_mapa = st_folium(m, width = 10)
