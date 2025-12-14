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

dataframes = {}
    
    # Lista todos os arquivos no diretório
    for file_name in os.listdir(dataset_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(dataset_dir, file_name)
            print(f"  Carregando: {file_name}")
            
            # Carrega o CSV
            df = pd.read_csv(file_path, encoding='utf-8')
            
            # Armazena no dicionário
            dataframes[file_name] = df
    
    print(f"✅ {len(dataframes)} arquivos carregados com sucesso!")
    return dataset_dir, dataframes

# Carrega todos os dados
dataset_path, dfs = load_olist_data()

# Acessa cada DataFrame individualmente pelos nomes dos arquivos
# Clientes
customers_df = dfs.get('olist_customers_dataset.csv')
print(f"Clientes: {customers_df.shape if customers_df is not None else 'Não encontrado'}")

# Geolocalização
geolocation_df = dfs.get('olist_geolocation_dataset.csv')
print(f"Geolocalização: {geolocation_df.shape if geolocation_df is not None else 'Não encontrado'}")

# Pedidos
orders_df = dfs.get('olist_orders_dataset.csv')
print(f"Pedidos: {orders_df.shape if orders_df is not None else 'Não encontrado'}")

# Itens dos pedidos
order_items_df = dfs.get('olist_order_items_dataset.csv')
print(f"Itens de Pedidos: {order_items_df.shape if order_items_df is not None else 'Não encontrado'}")

# Pagamentos
payments_df = dfs.get('olist_order_payments_dataset.csv')
print(f"Pagamentos: {payments_df.shape if payments_df is not None else 'Não encontrado'}")

# Reviews
reviews_df = dfs.get('olist_order_reviews_dataset.csv')
print(f"Reviews: {reviews_df.shape if reviews_df is not None else 'Não encontrado'}")

# Produtos
products_df = dfs.get('olist_products_dataset.csv')
print(f"Produtos: {products_df.shape if products_df is not None else 'Não encontrado'}")

# Vendedores
sellers_df = dfs.get('olist_sellers_dataset.csv')
print(f"Vendedores: {sellers_df.shape if sellers_df is not None else 'Não encontrado'}")

# Mostra informações básicas
print("\n📊 RESUMO DO DATASET:")
for file_name, df in dfs.items():
    if df is not None:
        print(f"{file_name}: {df.shape[0]} linhas, {df.shape[1]} colunas")

st.title('Análise Geral')
