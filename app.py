import streamlit as st
import pandas as pd
import joblib
import re

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    page_icon="🎓",
    layout="wide",
)

# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    return joblib.load("model/model.joblib")

model = load_model()

# =========================================================
# AMBIL FITUR LANGSUNG DARI MODEL (ANTI MISMATCH)
# =========================================================
if not hasattr(model, "feature_names_in_"):
    st.error(
        "Model tidak memiliki feature_names_in_. "
        "Model HARUS dilatih menggunakan pandas DataFrame."
    )
    st.stop()

MODEL_FEATURES = list(model.feature_names_in_)

# =========================================================
# HELPER: NORMALISASI NAMA KOLOM (FINAL)
# =========================================================
def normalize_col(col: str) -> str:
    col = col.strip().lower()
    col = re.sub(r"[()]", "", col)
    col = re.sub(r"[^\w]+", "_", col)
    col = re.sub(r"_+", "_", col)
    col = col.strip("_")        # 🔥 FIX FINAL (hapus underscore depan/belakang)
    return col

# =========================================================
# TITLE
# =========================================================
st.title("🎓 Prediksi Status Mahasiswa")
st.write(
    """
Prototype **Machine Learning** untuk memprediksi status mahasiswa:
**Dropout**, **Enrolled**, atau **Graduate**.

Aplikasi ini:
- menerima CSV mentah dari Dicoding
- mendukung delimiter `,` maupun `;`
- menyesuaikan kolom otomatis dengan model
"""
)

# =========================================================
# INFO MODEL (TRANSPARANSI – BAGUS UNTUK REVIEWER)
# =========================================================
with st.expander("ℹ️ Info Model & Fitur"):
    st.write("Jumlah fitur yang digunakan model:", len(MODEL_FEATURES))
    st.code(MODEL_FEATURES)

# =========================================================
# SINGLE PREDICTION (AUTO-SYNC)
# =========================================================
st.sidebar.header("📌 Prediksi Tunggal")

single_input = {}

for col in MODEL_FEATURES:
    cl = col.lower()

    if "grade" in cl or "rate" in cl or "gdp" in cl:
        single_input[col] = st.sidebar.number_input(col, 0.0, 500.0, 0.0)
    elif "age" in cl:
        single_input[col] = st.sidebar.number_input(col, 15, 80, 20)
    else:
        single_input[col] = st.sidebar.number_input(col, 0, 100, 0)

if st.sidebar.button("🔍 Prediksi"):
    single_df = pd.DataFrame([single_input])

    pred = model.predict(single_df)[0]
    proba = model.predict_proba(single_df)[0]

    st.subheader("📊 Hasil Prediksi (Tunggal)")
    st.success(f"Prediksi Status: **{pred}**")

    st.dataframe(
        pd.DataFrame(
            {
                "Status": model.classes_,
                "Probabilitas": proba,
            }
        ).sort_values("Probabilitas", ascending=False),
        use_container_width=True,
    )

# =========================================================
# BATCH PREDICTION (CSV UPLOAD)
# =========================================================
st.divider()
st.header("📦 Prediksi Batch (Upload CSV)")
st.caption(
    """
Upload file CSV (boleh CSV asli Dicoding).

✔ Delimiter `,` atau `;` terdeteksi otomatis  
✔ Kolom `Status` akan dihapus otomatis  
✔ Nama kolom disesuaikan otomatis dengan model
"""
)

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded is not None:
    try:
        # -------------------------------------------------
        # AUTO-DETECT DELIMITER
        # -------------------------------------------------
        df = pd.read_csv(uploaded, sep=None, engine="python")

        # -------------------------------------------------
        # HAPUS TARGET JIKA ADA
        # -------------------------------------------------
        if "Status" in df.columns:
            st.info("Kolom 'Status' terdeteksi dan dihapus otomatis.")
            df = df.drop(columns=["Status"])

        # -------------------------------------------------
        # NORMALISASI KOLOM CSV
        # -------------------------------------------------
        df.columns = [normalize_col(c) for c in df.columns]

        # -------------------------------------------------
        # NORMALISASI FITUR MODEL
        # -------------------------------------------------
        model_norm = {normalize_col(c): c for c in MODEL_FEATURES}

        # -------------------------------------------------
        # ALIGN CSV -> MODEL
        # -------------------------------------------------
        rename_map = {}
        for c in df.columns:
            if c in model_norm:
                rename_map[c] = model_norm[c]

        df = df.rename(columns=rename_map)

        # -------------------------------------------------
        # VALIDASI FINAL
        # -------------------------------------------------
        missing = [c for c in MODEL_FEATURES if c not in df.columns]
        if missing:
            st.error("Kolom berikut WAJIB ada sesuai model, namun tidak ditemukan:")
            st.code(missing)
            st.write("Kolom CSV terbaca:")
            st.code(list(df.columns))
            st.stop()

        X = df[MODEL_FEATURES].copy()

        # -------------------------------------------------
        # PREDIKSI
        # -------------------------------------------------
        preds = model.predict(X)
        proba = model.predict_proba(X)

        result = df.copy()
        result["predicted_status"] = preds

        for i, cls in enumerate(model.classes_):
            result[f"proba_{cls}"] = proba[:, i]

        st.success("✅ Prediksi batch berhasil.")
        st.dataframe(result.head(20), use_container_width=True)

        st.download_button(
            "⬇️ Download hasil prediksi (CSV)",
            result.to_csv(index=False).encode("utf-8"),
            "batch_prediction_result.csv",
            "text/csv",
        )

    except Exception as e:
        st.error(f"Gagal memproses file CSV: {e}")
