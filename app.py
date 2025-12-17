import streamlit as st
from datetime import datetime

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(page_title="Pengaduan Kampus", layout="wide")

st.title("🏫 Aplikasi Pengaduan Kampus")
st.caption("Simulasi sistem pengaduan mahasiswa dengan dashboard")

# =========================
# SESSION STATE
# =========================
if "pengaduan_list" not in st.session_state:
    st.session_state.pengaduan_list = []

# =========================
# MENU SIDEBAR
# =========================
menu = st.sidebar.radio(
    "Menu",
    ["Form Pengaduan", "Dashboard", "Daftar Pengaduan", "Tentang"]
)

# =========================
# FORM PENGADUAN
# =========================
if menu == "Form Pengaduan":
    st.subheader("📝 Form Pengaduan")

    nama = st.text_input("Nama Mahasiswa")
    nim = st.text_input("NIM")

    prodi = st.selectbox(
        "Program Studi",
        [
            "Akuntansi Keuangan Publik",
            "Administrasi Bisnis Internasional",
            "Teknik Sipil",
            "Teknik Perencanaan Jalan dan Jembatan",
            "Teknik Informatika",
            "Keamanan Sistem Informasi",
            "Teknik Mesin",
            "Perkapalan",
            "Maritim",
            "Bahasa Inggris",
        ],
    )

    kategori = st.selectbox(
        "Kategori Pengaduan",
        ["Akademik", "Fasilitas", "Administrasi", "Keuangan", "Lainnya"],
    )

    isi = st.text_area("Isi Pengaduan")
    anonim = st.checkbox("Kirim sebagai anonim")

    if st.button("Kirim Pengaduan"):
        if nim.isdigit() and len(isi) >= 10:
            data = {
                "Nama": "Anonim" if anonim else nama,
                "NIM": nim,
                "Program Studi": prodi,
                "Kategori": kategori,
                "Isi": isi,
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Status": "Diterima",
            }
            st.session_state.pengaduan_list.append(data)
            st.success("✅ Pengaduan berhasil dikirim")
        else:
            st.warning("⚠️ NIM harus angka dan isi pengaduan minimal 10 karakter")

# =========================
# DASHBOARD
# =========================
elif menu == "Dashboard":
    st.subheader("📊 Dashboard Pengaduan")

    total = len(st.session_state.pengaduan_list)
    akademik = len([p for p in st.session_state.pengaduan_list if p["Kategori"] == "Akademik"])
    fasilitas = len([p for p in st.session_state.pengaduan_list if p["Kategori"] == "Fasilitas"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pengaduan", total)
    col2.metric("Pengaduan Akademik", akademik)
    col3.metric("Pengaduan Fasilitas", fasilitas)

    st.divider()
    st.subheader("📌 Ringkasan per Program Studi")

    prodi_count = {}
    for p in st.session_state.pengaduan_list:
        prodi_count[p["Program Studi"]] = prodi_count.get(p["Program Studi"], 0) + 1

    if prodi_count:
        for k, v in prodi_count.items():
            st.write(f"- {k}: {v} pengaduan")
    else:
        st.info("Belum ada data untuk ditampilkan")

# =========================
# DAFTAR PENGADUAN
# =========================
elif menu == "Daftar Pengaduan":
    st.subheader("📋 Daftar Pengaduan")

    if st.session_state.pengaduan_list:
        for i, p in enumerate(st.session_state.pengaduan_list, start=1):
            with st.expander(f"Pengaduan #{i} - {p['Kategori']}"):
                st.write(f"**Nama**: {p['Nama']}")
                st.write(f"**NIM**: {p['NIM']}")
                st.write(f"**Program Studi**: {p['Program Studi']}")
                st.write(f"**Kategori**: {p['Kategori']}")
                st.write(f"**Isi**: {p['Isi']}")
                st.write(f"**Waktu**: {p['Waktu']}")
                st.write(f"**Status**: {p['Status']}")
    else:
        st.info("Belum ada pengaduan masuk")

# =========================
# TENTANG
# =========================
elif menu == "Tentang":
    st.subheader("ℹ️ Tentang Aplikasi")
    st.write(
        "Aplikasi Pengaduan Kampus ini merupakan simulasi sistem pengaduan mahasiswa "
        "dengan fitur dashboard sederhana. Cocok untuk tugas kuliah dan portofolio GitHub."
    )

