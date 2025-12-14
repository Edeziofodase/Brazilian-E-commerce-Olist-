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

# PASSO 2: Listar arquivos
print("Arquivos encontrados:")
for f in os.listdir(dataset_dir):
    if '.csv' in f:
        print(f" - {f}")

# PASSO 3: Carregar cada arquivo (copie e cole no seu código)
customers = pd.read_csv(os.path.join(dataset_dir, 'olist_customers_dataset.csv'))
geolocation = pd.read_csv(os.path.join(dataset_dir, 'olist_geolocation_dataset.csv'))
orders = pd.read_csv(os.path.join(dataset_dir, 'olist_orders_dataset.csv'))
order_items = pd.read_csv(os.path.join(dataset_dir, 'olist_order_items_dataset.csv'))
payments = pd.read_csv(os.path.join(dataset_dir, 'olist_order_payments_dataset.csv'))
reviews = pd.read_csv(os.path.join(dataset_dir, 'olist_order_reviews_dataset.csv'))
products = pd.read_csv(os.path.join(dataset_dir, 'olist_products_dataset.csv'))
sellers = pd.read_csv(os.path.join(dataset_dir, 'olist_sellers_dataset.csv'))

print("\n✅ PRONTO! Comece sua análise.")
