import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Jelajah Nusantara", page_icon="🗺️", layout="wide")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🗺️ Jelajah Nusantara")
st.write("Temukan resep masakan khas daerah Indonesia lengkap dengan informasi nutrisi dan budayanya.")

st.divider()

provinsi_list = [
    "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Kepulauan Riau",
    "Jambi", "Bengkulu", "Sumatera Selatan", "Kepulauan Bangka Belitung",
    "Lampung", "Banten", "DKI Jakarta", "Jawa Barat", "Jawa Tengah",
    "DI Yogyakarta", "Jawa Timur", "Bali", "Nusa Tenggara Barat",
    "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
    "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara",
    "Sulawesi Utara", "Gorontalo", "Sulawesi Tengah", "Sulawesi Barat",
    "Sulawesi Selatan", "Sulawesi Tenggara", "Maluku", "Maluku Utara",
    "Papua Barat", "Papua"
]

col1, col2 = st.columns(2)

with col1:
    provinsi = st.selectbox("Pilih Provinsi", provinsi_list)

with col2:
    bahan_utama = st.text_input(
        "Bahan Utama (opsional)",
        placeholder="Contoh: ayam, ikan, daging, tahu"
    )

jenis_masakan = st.multiselect(
    "Jenis Masakan",
    ["Makanan Utama", "Sup & Soto", "Sambal & Bumbu", "Kue & Jajanan", "Minuman Tradisional"],
    default=["Makanan Utama"]
)

jumlah_resep = st.slider("Jumlah Resep yang Ditampilkan", min_value=1, max_value=5, value=3)

if st.button("Jelajahi Resep"):
    with st.spinner(f"AI sedang mencari resep khas {provinsi}..."):
        
        bahan_info = f"dengan bahan utama {bahan_utama}" if bahan_utama else ""
        jenis_info = ", ".join(jenis_masakan) if jenis_masakan else "semua jenis masakan"
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Kamu adalah pakar kuliner dan budaya Indonesia yang menguasai masakan tradisional dari seluruh provinsi di Indonesia."
                },
                {
                    "role": "user",
                    "content": f"""
                    Berikan {jumlah_resep} resep masakan khas provinsi {provinsi} {bahan_info}.
                    Jenis masakan: {jenis_info}
                    
                    Untuk setiap resep, berikan informasi dalam format berikut:
                    
                    ---
                    ## [Nama Masakan]
                    
                    ### Tentang Masakan Ini
                    (cerita singkat tentang masakan ini, asal usul, dan maknanya dalam budaya {provinsi})
                    
                    ### Bahan-bahan (untuk 4 porsi)
                    (daftar bahan lengkap dengan takarannya)
                    
                    ### Cara Memasak
                    (langkah-langkah memasak yang jelas dan mudah diikuti)
                    
                    ### Informasi Nutrisi per Porsi
                    - Kalori: ... kkal
                    - Protein: ... gram
                    - Lemak: ... gram
                    - Karbohidrat: ... gram
                    - Serat: ... gram
                    
                    ### Tips
                    (1-2 tips memasak atau penyajian)
                    ---
                    """
                }
            ]
        )
        
        st.success(f"Ditemukan resep khas {provinsi}!")
        st.markdown(response.choices[0].message.content)