import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(page_title="Form Pengaduan Kampus", layout="wide")

st.title("🏫 Sistem Pengaduan Kampus")
st.caption("Simulasi sistem pengaduan mahasiswa berbasis Streamlit")

# =========================
# SESSION STATE INIT
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

if "counter" not in st.session_state:
    st.session_state.counter = 1

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Menu")
role = st.sidebar.selectbox("Login sebagai:", ["Mahasiswa", "Admin"])
menu = st.sidebar.radio("Pilih Halaman:", ["Form Pengaduan", "Cek Status", "Dashboard", "Tentang"])

# =========================
# FORM PENGADUAN (MAHASISWA)
# =========================
if role == "Mahasiswa" and menu == "Form Pengaduan":
    st.subheader("📝 Form Pengaduan Mahasiswa")

    nama = st.text_input("Nama Mahasiswa")
    nim = st.text_input("NIM")
    fakultas = st.selectbox("Fakultas", ["Ekonomi", "Teknik", "Hukum", "Keguruan", "Lainnya"])
    kategori = st.selectbox("Kategori", ["Akademik", "Fasilitas", "Administrasi", "Keuangan", "Lainnya"])
    urgensi = st.radio("Tingkat Urgensi", ["Rendah", "Sedang", "Tinggi"], horizontal=True)
    isi = st.text_area("Isi Pengaduan")
    anonim = st.checkbox("Kirim sebagai anonim")

    if st.button("Kirim Pengaduan"):
        if nim.isdigit() and len(isi) >= 10:
            tiket = f"PGD-{datetime.now().year}-{st.session_state.counter:03d}"
            st.session_state.counter += 1

            st.session_state.data.append({
                "Tiket": tiket,
                "Nama": "Anonim" if anonim else nama,
                "NIM": nim,
                "Fakultas": fakultas,
                "Kategori": kategori,
                "Urgensi": urgensi,
                "Isi": isi,
                "Status": "Diterima",
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M")
            })
            st.success(f"✅ Pengaduan berhasil dikirim. Nomor Tiket: {tiket}")
        else:
            st.warning("⚠️ NIM harus angka dan isi pengaduan minimal 10 karakter")

# =========================
# CEK STATUS (MAHASISWA)
# =========================
elif role == "Mahasiswa" and menu == "Cek Status":
    st.subheader("📌 Cek Status Pengaduan")
    kode = st.text_input("Masukkan Nomor Tiket")

    if kode:
        hasil = [d for d in s
