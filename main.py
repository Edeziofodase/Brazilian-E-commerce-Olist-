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
def load_data():
    return pd.read_csv("leilão/dados/tabela.csv")

df = load_data()

import kagglehub

# Download latest version
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

print("Path to dataset files:", path)

print("Arquivos no dataset:")
for file in os.listdir(path):
    print(f" - {file}")

dadosv = pd.read_csv(os.path.join(path, 'olist_sellers_dataset.csv'))
dadosv.head()

dadosc = pd.read_csv(os.path.join(path, 'olist_customers_dataset.csv'))
dadosc.head()

dadosg = pd.read_csv(os.path.join(path, 'olist_geolocation_dataset.csv'))
dadosg.head()

dadospag = pd.read_csv(os.path.join(path, 'olist_order_payments_dataset.csv'))
dadospag.head()

mapa = folium.Map(location=[dadosg['geolocation_lat'].mean(), dadosg['geolocation_lng'].mean()], zoom_start=5, tiles='CartoDB dark_matter');

data = list(zip(dadosg['geolocation_lat'], dadosg['geolocation_lng']))

FastMarkerCluster(data).add_to(mapa)
mapa.save('mapa_clusters.html') ; mapa
