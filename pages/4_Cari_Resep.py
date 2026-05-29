import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Cari Resep", page_icon="📖", layout="wide")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📖 Cari Resep")
st.write("Cari resep berdasarkan nama masakan atau bahan yang Anda miliki.")

st.divider()

mode = st.radio(
    "Cara Pencarian",
    ["🔍 Cari berdasarkan nama masakan", "🥦 Cari berdasarkan bahan yang dimiliki"],
    horizontal=True
)

st.divider()

if mode == "🔍 Cari berdasarkan nama masakan":
    kata_kunci = st.text_input(
        "Nama Masakan",
        placeholder="Contoh: rendang, gado-gado, soto ayam"
    )
else:
    kata_kunci = st.text_area(
        "Bahan yang Anda Miliki",
        placeholder="Contoh:\n- Ayam\n- Kentang\n- Wortel\n- Bawang putih\n- Kecap",
        height=150
    )

col1, col2 = st.columns(2)

with col1:
    porsi = st.number_input("Jumlah Porsi", min_value=1, max_value=20, value=2)

with col2:
    preferensi = st.multiselect(
        "Preferensi",
        ["Halal", "Vegetarian", "Rendah Kalori", "Rendah Lemak", "Tinggi Protein"],
        default=["Halal"]
    )

if st.button("Cari Resep"):
    if not kata_kunci:
        st.warning("Mohon isi kolom pencarian terlebih dahulu.")
    else:
        with st.spinner("AI sedang mencari resep untuk Anda..."):

            preferensi_info = ", ".join(preferensi) if preferensi else "tidak ada preferensi khusus"

            if mode == "🔍 Cari berdasarkan nama masakan":
                prompt_context = f"Berikan resep lengkap untuk masakan: {kata_kunci}"
            else:
                prompt_context = f"""Berikan 2-3 rekomendasi resep masakan berdasarkan bahan-bahan berikut:
{kata_kunci}

ATURAN PENTING:
- Tidak harus menggunakan SEMUA bahan dari list, boleh pilih sebagian saja
- Boleh menambahkan bahan lain di luar list untuk melengkapi resep
- Sebutkan bahan mana dari list yang digunakan dan bahan tambahan apa yang perlu disiapkan
- Rekomendasikan resep yang BERBEDA-BEDA satu sama lain
- Setiap resep harus memiliki bahan dan cara memasak yang lengkap"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah chef profesional dan ahli nutrisi yang membantu menemukan resep masakan."
                    },
                    {
                        "role": "user",
                        "content": f"""
                        {prompt_context}
                        
                        Jumlah porsi: {porsi}
                        Preferensi: {preferensi_info}
                        
                        Berikan resep dalam format berikut:
                        
                        ## [Nama Masakan]
                        
                        ### Deskripsi Singkat
                        (cerita singkat tentang masakan ini)
                        
                        ### Bahan-bahan (untuk {porsi} porsi)
                        (daftar bahan lengkap dengan takaran yang sudah disesuaikan untuk {porsi} porsi)
                        
                        ### Cara Memasak
                        (langkah-langkah memasak yang jelas)
                        
                        ### Informasi Nutrisi per Porsi
                        - Kalori: ... kkal
                        - Protein: ... gram
                        - Lemak: ... gram
                        - Karbohidrat: ... gram
                        - Serat: ... gram
                        
                        ### Tingkat Kesulitan
                        (Mudah / Sedang / Sulit) — dan estimasi waktu memasak
                        
                        ### Tips Chef
                        (1-2 tips untuk hasil terbaik)
                        """
                    }
                ]
            )

            st.success("Resep ditemukan!")
            st.markdown(response.choices[0].message.content)