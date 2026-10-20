
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Analisis Produktivitas Belajar",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Analisis Produktivitas Belajar Mahasiswa")
st.write(
    "Dashboard sederhana untuk mengeksplorasi hubungan "
    "antara kebiasaan belajar dan produktivitas."
)

# Membuat data simulasi agar aplikasi dapat dicoba
@st.cache_data
def buat_data():
    np.random.seed(42)
    jumlah = 100

    data = pd.DataFrame({
        "Jam Tidur": np.random.uniform(4, 9, jumlah).round(1),
        "Durasi Belajar": np.random.uniform(1, 8, jumlah).round(1),
        "Kehadiran (%)": np.random.randint(50, 101, jumlah)
    })

    noise = np.random.normal(0, 8, jumlah)
    data["Indeks Produktivitas"] = (
        30
        + data["Durasi Belajar"] * 5
        + data["Jam Tidur"] * 2
        + data["Kehadiran (%)"] * 0.2
        + noise
    ).clip(0, 100).round(1)

    return data

df = buat_data()

st.subheader("Ringkasan Data")
col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Data", len(df))
col2.metric(
    "Rata-rata Durasi Belajar",
    f"{df['Durasi Belajar'].mean():.1f} jam"
)
col3.metric(
    "Rata-rata Produktivitas",
    f"{df['Indeks Produktivitas'].mean():.1f}/100"
)

st.subheader("Data Mahasiswa Simulasi")
st.dataframe(df, use_container_width=True)

st.subheader("Visualisasi Data")
pilihan = st.selectbox(
    "Pilih faktor yang ingin dibandingkan:",
    ["Jam Tidur", "Durasi Belajar", "Kehadiran (%)"]
)

fig, ax = plt.subplots()
ax.scatter(df[pilihan], df["Indeks Produktivitas"])
ax.set_xlabel(pilihan)
ax.set_ylabel("Indeks Produktivitas")
ax.set_title(f"{pilihan} dan Indeks Produktivitas")
ax.grid(True, alpha=0.3)

st.pyplot(fig)
plt.close(fig)

korelasi = df[pilihan].corr(df["Indeks Produktivitas"])
st.write(f"Korelasi antara {pilihan} dan indeks produktivitas: **{korelasi:.3f}**")

st.caption(
    "Catatan: Data bersifat sintetis untuk demonstrasi, "
    "bukan data mahasiswa nyata."
)
