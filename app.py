import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Kualitas Udara", layout="wide")
st.title("Dashboard Pemantauan Kualitas Udara")
st.caption("Demo antarmuka; data PM2.5 bersifat sintetis, bukan pengukuran real-time.")
@st.cache_data
def data():
    rng=np.random.default_rng(8)
    dates=pd.date_range("2026-01-01", periods=90, freq="D")
    rows=[]
    for loc, base in [("Lokasi A",22),("Lokasi B",35),("Lokasi C",16)]:
        vals=np.maximum(2, rng.normal(base, 7, len(dates)))
        rows.extend({"tanggal":d,"lokasi":loc,"PM2.5 (simulasi)":round(v,1)} for d,v in zip(dates,vals))
    return pd.DataFrame(rows)
df=data()
locations=st.multiselect("Pilih lokasi", df.lokasi.unique().tolist(), default=df.lokasi.unique().tolist())
start,end=st.date_input("Rentang tanggal", (df.tanggal.min().date(), df.tanggal.max().date()))
view=df[df.lokasi.isin(locations) & df.tanggal.dt.date.between(start,end)]
if view.empty:
    st.warning("Tidak ada data untuk filter tersebut. Pilih lokasi atau rentang tanggal lain.")
else:
    a,b=st.columns(2)
    a.metric("Rata-rata PM2.5 simulasi", f"{view['PM2.5 (simulasi)'].mean():.1f}")
    b.metric("Jumlah pengamatan", len(view))
    fig,ax=plt.subplots()
    for loc,part in view.groupby("lokasi"):
        ax.plot(part.tanggal,part["PM2.5 (simulasi)"],label=loc)
    ax.set_ylabel("PM2.5 (simulasi)"); ax.set_xlabel("Tanggal"); ax.legend()
    plt.xticks(rotation=30); st.pyplot(fig)
    st.dataframe(view, use_container_width=True)
st.info("Sebelum digunakan untuk keputusan kesehatan atau kebijakan, dashboard perlu memakai data terverifikasi, satuan dan standar yang jelas, serta evaluasi kegunaan dengan pengguna.")
