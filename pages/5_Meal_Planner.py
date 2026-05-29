import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Meal Planner", page_icon="🗓️", layout="wide")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🗓️ Meal Planner")
st.write("Masukkan data diri Anda dan AI akan menyusun rencana makan harian yang dipersonalisasi.")

st.divider()

st.subheader("📊 Data Diri")

col1, col2 = st.columns(2)

with col1:
    nama = st.text_input("Nama", placeholder="Contoh: Nisrina")
    usia = st.number_input("Usia (tahun)", min_value=10, max_value=100, value=25)
    jenis_kelamin = st.radio("Jenis Kelamin", ["Perempuan", "Laki-laki"], horizontal=True)

with col2:
    berat_badan = st.number_input("Berat Badan (kg)", min_value=20.0, max_value=200.0, value=55.0, step=0.5)
    tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=160.0, step=0.5)

st.divider()
st.subheader("🏃 Aktivitas & Tujuan")

aktivitas = st.selectbox(
    "Tingkat Aktivitas",
    [
        "Sedentary (jarang olahraga, kerja duduk)",
        "Lightly Active (olahraga ringan 1-3x seminggu)",
        "Moderately Active (olahraga sedang 3-5x seminggu)",
        "Very Active (olahraga berat 6-7x seminggu)",
        "Extra Active (atlet / kerja fisik berat)"
    ]
)

tujuan = st.selectbox(
    "Tujuan Kesehatan",
    [
        "Menurunkan berat badan",
        "Menjaga berat badan ideal",
        "Menambah berat badan / massa otot",
        "Menjaga kesehatan jantung",
        "Meningkatkan energi harian"
    ]
)

preferensi_makan = st.multiselect(
    "Preferensi Makanan",
    ["Halal", "Vegetarian", "Bebas Gluten", "Rendah Gula", "Suka Masakan Indonesia", "Suka Masakan Internasional"],
    default=["Halal", "Suka Masakan Indonesia"]
)

alergi = st.text_input(
    "Alergi atau Pantangan Makanan (opsional)",
    placeholder="Contoh: kacang, seafood, susu"
)

st.divider()
st.subheader("📅 Durasi Meal Plan")

durasi = st.radio(
    "Pilih Durasi",
    ["1 Hari", "3 Hari", "7 Hari"],
    horizontal=True
)

st.divider()

if st.button("Buat Meal Plan Saya"):
    if not nama:
        st.warning("Mohon isi nama Anda terlebih dahulu.")
    else:
        with st.spinner(f"AI sedang menyusun meal plan {durasi} untuk {nama}..."):

            bmi = berat_badan / ((tinggi_badan / 100) ** 2)

            if bmi < 18.5:
                kategori_bmi = "Berat Badan Kurang (Underweight)"
            elif bmi < 25:
                kategori_bmi = "Berat Badan Normal"
            elif bmi < 30:
                kategori_bmi = "Berat Badan Berlebih (Overweight)"
            else:
                kategori_bmi = "Obesitas"

            preferensi_info = ", ".join(preferensi_makan) if preferensi_makan else "tidak ada preferensi khusus"
            alergi_info = alergi if alergi else "tidak ada"

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("BMI Anda", f"{bmi:.1f}")
            with col2:
                st.metric("Kategori", kategori_bmi)
            with col3:
                st.metric("Tinggi / Berat", f"{tinggi_badan}cm / {berat_badan}kg")

            st.divider()

            if durasi == "1 Hari":
                format_hari = """
## Meal Plan Harian

### 🌅 Sarapan (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### ☀️ Makan Siang (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### 🌙 Makan Malam (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### 🍎 Snack (... kkal)
- Snack pagi: ...
- Snack sore: ...

## Total Nutrisi Harian
- Total Kalori: ... kkal
- Total Protein: ... gram
- Total Lemak: ... gram
- Total Karbohidrat: ... gram

## Saran Khusus untuk {nama}
(3-4 saran personal berdasarkan tujuan dan kondisi)
                """

            elif durasi == "3 Hari":
                format_hari = """
Untuk setiap hari (Hari 1, Hari 2, Hari 3), berikan format berikut:

## Hari [X]

### 🌅 Sarapan (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### ☀️ Makan Siang (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### 🌙 Makan Malam (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### 🍎 Snack (... kkal)
- Snack pagi: ...
- Snack sore: ...

Pastikan menu setiap hari BERBEDA dan bervariasi.

## Total Nutrisi Harian (Rata-rata)
- Total Kalori: ... kkal
- Total Protein: ... gram
- Total Lemak: ... gram
- Total Karbohidrat: ... gram

## Saran Khusus
(3-4 saran personal)
    """

            else:
                format_hari = """
Untuk setiap hari (Hari 1 sampai Hari 7), berikan format berikut:

## Hari [X]

### 🌅 Sarapan (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### ☀️ Makan Siang (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### 🌙 Makan Malam (... kkal)
- Menu: ...
- Bahan & Takaran: ...
- Tips penyajian: ...

### 🍎 Snack (... kkal)
- Snack pagi: ...
- Snack sore: ...

Pastikan menu setiap hari BERBEDA dan bervariasi selama 7 hari penuh.
Hindari pengulangan menu yang sama dalam satu minggu.

## Total Nutrisi Harian (Rata-rata)
- Total Kalori: ... kkal
- Total Protein: ... gram
- Total Lemak: ... gram
- Total Karbohidrat: ... gram

## Saran Khusus
(3-4 saran personal)
    """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah ahli gizi dan nutrisi yang membantu menyusun rencana makan harian yang sehat dan dipersonalisasi."
                    },
                    {
                        "role": "user",
                        "content": f"""
Susun meal plan {durasi} untuk seseorang dengan data berikut:

Nama: {nama}
Usia: {usia} tahun
Jenis Kelamin: {jenis_kelamin}
Berat Badan: {berat_badan} kg
Tinggi Badan: {tinggi_badan} cm
BMI: {bmi:.1f} ({kategori_bmi})
Tingkat Aktivitas: {aktivitas}
Tujuan: {tujuan}
Preferensi Makanan: {preferensi_info}
Alergi/Pantangan: {alergi_info}

## Analisa Kondisi {nama}
(jelaskan kondisi kesehatan berdasarkan BMI dan data di atas)

## Kebutuhan Kalori Harian
- Total Kalori: ... kkal/hari
- Protein: ... gram/hari
- Lemak: ... gram/hari
- Karbohidrat: ... gram/hari

{format_hari}
                        """
                    }
                ]
            )

            st.success(f"Meal plan {durasi} untuk {nama} sudah siap!")
            st.markdown(response.choices[0].message.content)