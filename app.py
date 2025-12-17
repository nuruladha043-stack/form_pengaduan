import streamlit as st
from datetime import datetime

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Form Pengaduan Kampus",
    layout="centered"
)

# =========================
# HEADER
# =========================
st.title("🏫 Aplikasi Form Pengaduan Kampus")
st.caption("Simulasi sistem pengaduan mahasiswa (tanpa penyimpanan data)")

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Form Pengaduan", "Cek Status Pengaduan", "FAQ", "Tentang Aplikasi"]
)

# =========================
# INISIALISASI SESSION STATE
# =========================
if "pengaduan" not in st.session_state:
    st.session_state.pengaduan = None

# =========================
# FORM PENGADUAN
# =========================
if menu == "Form Pengaduan":
    st.subheader("📝 Form Pengaduan Mahasiswa")

    nama = st.text_input("Nama Mahasiswa")
    nim = st.text_input("NIM")
    fakultas = st.selectbox(
        "Fakultas",
        [
            "Fakultas Ekonomi",
            "Fakultas Teknik",
            "Fakultas Hukum",
            "Fakultas Keguruan",
            "Lainnya",
        ],
    )
    kategori = st.selectbox(
        "Kategori Pengaduan",
        [
            "Akademik",
            "Fasilitas",
            "Pelayanan Administrasi",
            "Keuangan",
            "Lainnya",
        ],
    )
    tingkat_urgensi = st.radio(
        "Tingkat Urgensi",
        ["Rendah", "Sedang", "Tinggi"],
        horizontal=True,
    )
    pengaduan = st.text_area("Isi Pengaduan")

    anonim = st.checkbox("Kirim sebagai anonim")

    if st.button("Kirim Pengaduan"):
        if nim and pengaduan:
            st.session_state.pengaduan = {
                "Nama": "Anonim" if anonim else nama,
                "NIM": nim,
                "Fakultas": fakultas,
                "Kategori": kategori,
                "Urgensi": tingkat_urgensi,
                "Isi": pengaduan,
                "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Status": "Sedang Diproses",
            }
            st.success("✅ Pengaduan berhasil dikirim (simulasi).")
        else:
            st.warning("⚠️ NIM dan isi pengaduan wajib diisi.")

# =========================
# CEK STATUS PENGADUAN
# =========================
elif menu == "Cek Status Pengaduan":
    st.subheader("📌 Cek Status Pengaduan")

    if st.session_state.pengaduan:
        p = st.session_state.pengaduan
        st.info("Berikut adalah status pengaduan terakhir Anda:")

        st.write(f"**Nama**: {p['Nama']}")
        st.write(f"**NIM**: {p['NIM']}")
        st.write(f"**Fakultas**: {p['Fakultas']}")
        st.write(f"**Kategori**: {p['Kategori']}")
        st.write(f"**Urgensi**: {p['Urgensi']}")
        st.write(f"**Waktu Pengaduan**: {p['Waktu']}")
        st.write(f"**Status**: {p['Status']}")
    else:
        st.warning("Belum ada pengaduan yang dikirim.")

# =========================
# FAQ
# =========================
elif menu == "FAQ":
    st.subheader("❓ Pertanyaan yang Sering Diajukan")

    with st.expander("Apakah pengaduan ini benar-benar dikirim?"):
        st.write("Tidak. Ini hanya aplikasi simulasi tanpa penyimpanan data.")

    with st.expander("Apakah saya bisa mengirim pengaduan secara anonim?"):
        st.write("Ya. Tersedia fitur pengaduan anonim.")

    with st.expander("Siapa yang memproses pengaduan?"):
        st.write("Pada aplikasi ini, proses pengaduan hanya simulasi.")

# =========================
# TENTANG APLIKASI
# =========================
elif menu == "Tentang Aplikasi":
    st.subheader("ℹ️ Tentang Aplikasi")
    st.write(
        "Aplikasi Form Pengaduan Kampus ini dibuat sebagai project sederhana "
        "berbasis Streamlit untuk kebutuhan tugas kuliah dan portofolio GitHub. "
        "Aplikasi tidak terhubung dengan database dan hanya menampilkan simulasi "
        "alur sistem pengaduan mahasiswa."
    )
