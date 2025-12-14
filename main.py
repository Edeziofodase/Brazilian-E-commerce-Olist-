import streamlit as st
import pandas as pd
import math as m
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster
from streamlit_folium import st_folium
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


dataset_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

# PASSO 2 - Depois adicione estas linhas
customers_df = pd.read_csv(f"{dataset_path}/olist_customers_dataset.csv")
orders_df = pd.read_csv(f"{dataset_path}/olist_orders_dataset.csv")

# PASSO 3 - Verifique se funcionou
print("Funcionou! Shapes:")
print(f"Customers: {customers_df.shape}")
print(f"Orders: {orders_df.shape}")

# PASSO 4 - Se funcionar, carregue os outros
geolocation_df = pd.read_csv(f"{dataset_path}/olist_geolocation_dataset.csv")
order_items_df = pd.read_csv(f"{dataset_path}/olist_order_items_dataset.csv")
payments_df = pd.read_csv(f"{dataset_path}/olist_order_payments_dataset.csv")
reviews_df = pd.read_csv(f"{dataset_path}/olist_order_reviews_dataset.csv")
products_df = pd.read_csv(f"{dataset_path}/olist_products_dataset.csv")
sellers_df = pd.read_csv(f"{dataset_path}/olist_sellers_dataset.csv")


mapa = folium.Map(location=[geolocation_df['geolocation_lat'].mean(), geolocation_df['geolocation_lng'].mean()], zoom_start=5, tiles='CartoDB dark_matter');

data = list(zip(geolocation_df['geolocation_lat'], geolocation_df['geolocation_lng']))

FastMarkerCluster(data).add_to(mapa)
mapa.save('mapa_clusters.html') ;
st_data = st_folium(mapa, width=10)
