import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Analisa Label Nutrisi", page_icon="🏷️", layout="wide")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🏷️ Analisa Label Nutrisi")
st.write("Masukkan informasi dari label kemasan makanan dan AI akan menganalisa apakah makanan ini sehat untuk Anda.")

st.divider()

nama_produk = st.text_input("Nama Produk", placeholder="Contoh: Mie Instan Goreng")

st.subheader("📦 Informasi Kemasan")
col1, col2 = st.columns(2)

with col1:
    ukuran_kemasan = st.number_input(
        "Ukuran Total Kemasan (gram)",
        min_value=0.0, value=0.0, step=0.5,
        help="Total berat/isi satu kemasan produk. Contoh: 1 bungkus Indomie = 85 gram"
    )

with col2:
    ukuran_sajian = st.number_input(
        "Ukuran 1 Sajian di Label (gram)",
        min_value=0.0, value=0.0, step=0.5,
        help="Ukuran 1 sajian yang tertera di label nutrisi. Contoh: 1 sajian = 30 gram"
    )

if ukuran_kemasan > 0 and ukuran_sajian > 0:
    jumlah_sajian = ukuran_kemasan / ukuran_sajian
    st.info(f"📊 1 kemasan = **{jumlah_sajian:.1f} sajian**")
else:
    jumlah_sajian = 1

st.divider()
st.subheader("🔢 Nilai Gizi per 1 Sajian (sesuai label)")

col1, col2 = st.columns(2)

with col1:
    kalori = st.number_input("Kalori (kkal)", min_value=0, value=0)
    protein = st.number_input("Protein (gram)", min_value=0.0, value=0.0, step=0.1)
    lemak = st.number_input("Lemak Total (gram)", min_value=0.0, value=0.0, step=0.1)
    lemak_jenuh = st.number_input("Lemak Jenuh (gram)", min_value=0.0, value=0.0, step=0.1)

with col2:
    karbohidrat = st.number_input("Karbohidrat (gram)", min_value=0.0, value=0.0, step=0.1)
    gula = st.number_input("Gula (gram)", min_value=0.0, value=0.0, step=0.1)
    serat = st.number_input("Serat (gram)", min_value=0.0, value=0.0, step=0.1)
    sodium = st.number_input("Sodium (mg)", min_value=0.0, value=0.0, step=1.0)

if jumlah_sajian > 1:
    st.divider()
    st.subheader("📦 Estimasi Nutrisi per Kemasan")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Kalori", f"{kalori * jumlah_sajian:.0f} kkal")
    with col2:
        st.metric("Protein", f"{protein * jumlah_sajian:.1f} g")
    with col3:
        st.metric("Lemak", f"{lemak * jumlah_sajian:.1f} g")
    with col4:
        st.metric("Karbohidrat", f"{karbohidrat * jumlah_sajian:.1f} g")

st.divider()

tujuan = st.selectbox(
    "Tujuan Kesehatan Anda",
    ["Menjaga berat badan ideal", "Diet menurunkan berat badan",
     "Menambah massa otot", "Menjaga kesehatan jantung", "Umum / tidak ada tujuan khusus"]
)

if st.button("Analisa Label", use_container_width=True):
    if not nama_produk:
        st.warning("Mohon isi nama produk terlebih dahulu.")
    elif kalori == 0 and protein == 0.0 and karbohidrat == 0.0:
        st.warning("Mohon isi minimal kalori, protein, dan karbohidrat.")
    else:
        with st.spinner("AI sedang menganalisa label nutrisi..."):

            kalori_kemasan = kalori * jumlah_sajian
            protein_kemasan = protein * jumlah_sajian
            lemak_kemasan = lemak * jumlah_sajian
            karbohidrat_kemasan = karbohidrat * jumlah_sajian
            gula_kemasan = gula * jumlah_sajian
            serat_kemasan = serat * jumlah_sajian
            sodium_kemasan = sodium * jumlah_sajian

            kemasan_info = ""
            if ukuran_kemasan > 0 and ukuran_sajian > 0:
                kemasan_info = f"""
Informasi Kemasan:
- Ukuran total kemasan: {ukuran_kemasan} gram
- Ukuran 1 sajian: {ukuran_sajian} gram
- Jumlah sajian per kemasan: {jumlah_sajian:.1f} sajian

Nilai Gizi per Kemasan (total):
- Kalori: {kalori_kemasan:.0f} kkal
- Protein: {protein_kemasan:.1f} gram
- Lemak Total: {lemak_kemasan:.1f} gram
- Karbohidrat: {karbohidrat_kemasan:.1f} gram
- Gula: {gula_kemasan:.1f} gram
- Serat: {serat_kemasan:.1f} gram
- Sodium: {sodium_kemasan:.0f} mg
                """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah ahli nutrisi dan gizi yang membantu masyarakat memahami label nutrisi pada kemasan makanan."
                    },
                    {
                        "role": "user",
                        "content": f"""
Analisa label nutrisi produk berikut:

Nama Produk: {nama_produk}

Nilai Gizi per 1 Sajian (sesuai label):
- Kalori: {kalori} kkal
- Protein: {protein} gram
- Lemak Total: {lemak} gram
- Lemak Jenuh: {lemak_jenuh} gram
- Karbohidrat: {karbohidrat} gram
- Gula: {gula} gram
- Serat: {serat} gram
- Sodium: {sodium} mg

{kemasan_info}

Tujuan kesehatan pengguna: {tujuan}

Berikan analisa dalam format berikut:

## Ringkasan Produk
(deskripsikan produk ini secara singkat dari sisi nutrisi)

## Skor Kesehatan
Berikan skor dari 1-10 dan penjelasan singkat mengapa

## Analisa per Komponen
- Kalori: (apakah tinggi/sedang/rendah per sajian dan per kemasan)
- Protein: (apakah tinggi/sedang/rendah)
- Lemak: (apakah perlu diwaspadai)
- Karbohidrat & Gula: (apakah aman)
- Sodium: (apakah perlu diwaspadai)
- Serat: (apakah cukup)

## Perhatian Khusus
(jika 1 kemasan mengandung lebih dari 1 sajian, berikan peringatan tentang 
risiko mengkonsumsi 1 kemasan penuh sekaligus)

## Cocok untuk Tujuan Anda?
(apakah produk ini cocok untuk tujuan: {tujuan})

## Rekomendasi
(2-3 saran praktis untuk konsumsi produk ini)
                        """
                    }
                ]
            )

            st.success("Analisa selesai!")
            st.markdown(response.choices[0].message.content)