
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Pemetaan Fasilitas GIS",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Pemetaan dan Visualisasi Lokasi Fasilitas")
st.write(
    "Aplikasi sederhana untuk melihat persebaran fasilitas "
    "menggunakan konsep Geographic Information System (GIS)."
)

# Data simulasi lokasi fasilitas
data = pd.DataFrame({
    "Fasilitas": [
        "Rumah Sakit Contoh",
        "Sekolah Contoh",
        "Taman Contoh",
        "Perpustakaan Contoh"
    ],
    "Kategori": [
        "Kesehatan",
        "Pendidikan",
        "Ruang Publik",
        "Pendidikan"
    ],
    "Latitude": [
        -0.9147,
        -0.9220,
        -0.9080,
        -0.9300
    ],
    "Longitude": [
        100.3630,
        100.3550,
        100.3700,
        100.3650
    ]
})

kategori = st.selectbox(
    "Pilih kategori fasilitas",
    ["Semua"] + sorted(data["Kategori"].unique().tolist())
)

if kategori != "Semua":
    data_tampil = data[data["Kategori"] == kategori]
else:
    data_tampil = data

kolom1, kolom2 = st.columns(2)
kolom1.metric("Jumlah fasilitas", len(data_tampil))
kolom2.metric("Jumlah kategori", data_tampil["Kategori"].nunique())

st.subheader("Peta Persebaran Fasilitas")

peta = folium.Map(
    location=[-0.9210, 100.3630],
    zoom_start=14
)

for _, baris in data_tampil.iterrows():
    folium.Marker(
        location=[baris["Latitude"], baris["Longitude"]],
        popup=(
            f'{baris["Fasilitas"]}<br>'
            f'Kategori: {baris["Kategori"]}'
        ),
        tooltip=baris["Fasilitas"]
    ).add_to(peta)

st_folium(peta, width=None, height=450)

st.subheader("Data Lokasi")
st.dataframe(data_tampil, use_container_width=True)

st.caption(
    "Catatan: nama fasilitas dan koordinat merupakan data "
    "simulasi untuk demonstrasi, bukan lokasi yang telah diverifikasi."
)
