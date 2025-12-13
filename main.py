import streamlit as st
import pandas as pd
import math as m
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster
import kagglehub

# Download latest version
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

print("Path to dataset files:", path)
st.title('Análise Geral')


print("Arquivos no dataset:")
for file in os.listdir(path):
    print(f" - {file}")

dadosv = pd.read_csv(os.path.join(path, 'olist_sellers_dataset.csv'))


dadosc = pd.read_csv(os.path.join(path, 'olist_customers_dataset.csv'))


dadosg = pd.read_csv(os.path.join(path, 'olist_geolocation_dataset.csv'))


dadospag = pd.read_csv(os.path.join(path, 'olist_order_payments_dataset.csv'))

