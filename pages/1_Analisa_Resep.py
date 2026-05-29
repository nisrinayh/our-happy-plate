import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Analisa Resep", page_icon="🔍", layout="wide")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🔍 Analisa Resep")
st.write("Masukkan resep Anda dan AI akan menganalisa kandungan nutrisinya.")

st.divider()

nama_resep = st.text_input("Nama Resep", placeholder="Contoh: Ayam Goreng Kunyit")

bahan = st.text_area(
    "Daftar Bahan",
    placeholder="Contoh:\n- 500g ayam\n- 2 siung bawang putih\n- 1 sdt kunyit\n- Garam secukupnya",
    height=200
)

porsi = st.number_input("Jumlah Porsi", min_value=1, max_value=20, value=2)

if st.button("Analisa Nutrisi"):
    if not nama_resep or not bahan:
        st.warning("Mohon isi nama resep dan daftar bahan terlebih dahulu.")
    else:
        with st.spinner("AI sedang menganalisa nutrisi resep Anda..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah ahli nutrisi yang membantu menganalisa kandungan gizi resep masakan."
                    },
                    {
                        "role": "user",
                        "content": f"""
                        Analisa kandungan nutrisi dari resep berikut:
                        
                        Nama Resep: {nama_resep}
                        Jumlah Porsi: {porsi}
                        
                        Bahan-bahan:
                        {bahan}
                        
                        Berikan informasi dalam format berikut:
                        
                        ## Informasi Nutrisi per Porsi
                        - Kalori: ... kkal
                        - Protein: ... gram
                        - Lemak: ... gram
                        - Karbohidrat: ... gram
                        - Serat: ... gram
                        - Sodium: ... mg
                        
                        ## Analisa Kesehatan
                        (jelaskan manfaat kesehatan dari resep ini dalam 3-4 kalimat)
                        
                        ## Saran
                        (berikan 2-3 saran untuk membuat resep ini lebih sehat)
                        """
                    }
                ]
            )

            st.success("Analisa selesai!")
            st.markdown(response.choices[0].message.content)