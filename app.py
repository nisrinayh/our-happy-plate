import streamlit as st

st.set_page_config(
    page_title="Our Happy Plate",
    page_icon="🍽️",
    layout="wide"
)

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF;
    }
    [data-testid="stSidebarContent"] {
        background-color: #F9F5F0;
    }
    [data-testid="stHeadingWithActionElements"] h1,
    [data-testid="stHeadingWithActionElements"] h2,
    [data-testid="stHeadingWithActionElements"] h3 {
        color: #2D6A2D !important;
    }
    /* Sembunyikan tulisan "app" di sidebar */
    [data-testid="stSidebarNav"] a[href*="app"] span {
        display: none;
    }
    [data-testid="stSidebarNav"] a[href*="app"]::before {
        content: "🏠 Home";
        font-weight: 500;
    }
    .hero-container {
        background: linear-gradient(135deg, #f0f7f0 0%, #fff8f0 100%);
        border-radius: 16px;
        padding: 48px 40px;
        text-align: center;
        margin-bottom: 32px;
        border: 1px solid #e8f0e8;
    }
    .hero-title {
        font-size: 48px;
        font-weight: 700;
        color: #2D6A2D;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 18px;
        color: #888;
        margin-bottom: 24px;
    }
    .hero-tagline {
        font-size: 15px;
        color: #FF8C00;
        font-weight: 500;
    }
    .feature-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 24px 24px 12px 24px;
        border: 1px solid #e8f0e8;
        height: 100%;
    }
    .feature-icon {
        font-size: 36px;
        margin-bottom: 12px;
    }
    .feature-title {
        font-size: 16px;
        font-weight: 600;
        color: #2D6A2D;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
        margin-bottom: 16px;
    }
    .stats-container {
        background: #f0f7f0;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        margin: 32px 0;
    }
    .stat-number {
        font-size: 32px;
        font-weight: 700;
        color: #FF8C00;
    }
    .stat-label {
        font-size: 13px;
        color: #666;
    }
    .footer {
        text-align: center;
        padding: 24px;
        color: #aaa;
        font-size: 13px;
        border-top: 1px solid #f0f0f0;
        margin-top: 48px;
    }
    /* Tombol full width */
    div.stButton > button {
        background-color: #2D6A2D;
        color: white;
        border: none;
        border-radius: 8px;
        width: 100%;
        padding: 10px;
        font-size: 14px;
        margin-top: 12px;
    }
    div.stButton > button:hover {
        background-color: #FF8C00;
        color: white;
        border: none;
    }
    /* Paksa kolom tidak overflow */
    [data-testid="column"] {
        padding: 0 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🍽️ Our Happy Plate</div>
        <div class="hero-subtitle">Eat Well. Feel Good. Explore Nusantara.</div>
        <div class="hero-tagline">✨ Powered by AI — Gratis untuk semua orang</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 🌟 Apa yang bisa kamu lakukan?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Analisa Resep</div>
            <div class="feature-desc">Masukkan resep masakan kamu dan dapatkan analisa nutrisi lengkap dari AI — kalori, protein, lemak, dan saran kesehatan.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Mulai Analisa Resep", use_container_width=True):
        st.switch_page("pages/1_Analisa_Resep.py")

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🏷️</div>
            <div class="feature-title">Analisa Label Nutrisi</div>
            <div class="feature-desc">Input angka dari kemasan makanan dan AI akan menganalisa apakah produk tersebut sehat sesuai tujuan kesehatanmu.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Mulai Analisa Label", use_container_width=True):
        st.switch_page("pages/2_Analisa_Label_Nutrisi.py")

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🗺️</div>
            <div class="feature-title">Jelajah Nusantara</div>
            <div class="feature-desc">Temukan resep masakan khas dari seluruh provinsi di Indonesia, lengkap dengan cerita budaya dan informasi nutrisinya.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Jelajahi Nusantara", use_container_width=True):
        st.switch_page("pages/3_Jelajah_Nusantara.py")

st.markdown("<br>", unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📖</div>
            <div class="feature-title">Cari Resep</div>
            <div class="feature-desc">Cari resep berdasarkan nama masakan atau bahan yang kamu punya di rumah. AI akan rekomendasikan resep terbaik lengkap dengan nutrisinya.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Cari Resep Sekarang", use_container_width=True):
        st.switch_page("pages/4_Cari_Resep.py")

with col5:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🗓️</div>
            <div class="feature-title">Meal Planner</div>
            <div class="feature-desc">Input data diri kamu dan dapatkan rencana makan harian yang dipersonalisasi — lengkap dengan BMI, kebutuhan kalori, dan menu 1, 3, atau 7 hari.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Buat Meal Plan", use_container_width=True):
        st.switch_page("pages/5_Meal_Planner.py")

st.markdown("""
    <div class="stats-container">
        <div style="display: flex; justify-content: center; gap: 80px; flex-wrap: wrap;">
            <div>
                <div class="stat-number">5</div>
                <div class="stat-label">Fitur Unggulan</div>
            </div>
            <div>
                <div class="stat-number">100%</div>
                <div class="stat-label">Gratis</div>
            </div>
            <div>
                <div class="stat-number">AI</div>
                <div class="stat-label">Powered</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        Made with ❤️ for a healthier Indonesia &nbsp;|&nbsp; Our Happy Plate © 2025
    </div>
""", unsafe_allow_html=True)