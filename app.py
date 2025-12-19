import json
from pathlib import Path
 
import joblib
import numpy as np
import pandas as pd
import streamlit as st
 
st.set_page_config(
    page_title="Jaya Jaya Institut - Prediksi Risiko Dropout",
    page_icon="🎓",
    layout="wide",
)
 
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "model.joblib"
SCHEMA_PATH = BASE_DIR / "model" / "schema.json"
 
@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return model, schema
 
model, schema = load_artifacts()
 
st.title("🎓 Prediksi Risiko Dropout Mahasiswa — Jaya Jaya Institut")
st.caption(
    "Prototype ini memprediksi status mahasiswa (**Dropout / Enrolled / Graduate**) "
    "berdasarkan data pendaftaran & performa akademik."
)
 
with st.expander("Cara pakai", expanded=False):
    st.write(
        "- Isi input di sidebar, lalu klik **Prediksi**.\n"
        "- Anda juga bisa **upload CSV** untuk prediksi batch.\n"
        "- Model yang dipakai disimpan di `model/model.joblib` (hasil training dari notebook)."
    )
 
# =========================
# Sidebar input (single row)
# =========================
with st.sidebar:
    st.header("Input Mahasiswa (Satu Data)")
 
    inputs = {}
    for feat in schema["features"]:
        name = feat["name"]
        if feat["type"] == "numeric":
            mn = feat.get("min", 0.0)
            mx = feat.get("max", 1.0)
            default = feat.get("default", 0.0)
            subtype = feat.get("subtype", "float")
 
            # Clamp default (biar tidak error kalau schema berubah)
            default = float(min(max(default, mn), mx))
 
            if subtype == "int":
                inputs[name] = st.number_input(
                    name,
                    min_value=int(mn),
                    max_value=int(mx),
                    value=int(round(default)),
                    step=1,
                )
            else:
                inputs[name] = st.number_input(
                    name,
                    min_value=float(mn),
                    max_value=float(mx),
                    value=float(default),
                )
        else:
            cats = feat.get("categories", [])
            default = feat.get("default", cats[0] if cats else "")
            inputs[name] = st.selectbox(name, options=cats if cats else [default], index=0)
 
    predict_btn = st.button("Prediksi", type="primary")
 
# =========================
# Main output
# =========================
def predict_dataframe(X: pd.DataFrame) -> pd.DataFrame:
    """Return predictions + probabilities for each class."""
    preds = model.predict(X)
    proba = model.predict_proba(X)
    classes = list(model.classes_)
    out = X.copy()
    out["pred_status"] = preds
    for i, c in enumerate(classes):
        out[f"proba_{c}"] = proba[:, i]
    return out
 
if predict_btn:
    X_one = pd.DataFrame([inputs], columns=[f["name"] for f in schema["features"]])
    result = predict_dataframe(X_one)
 
    pred_label = result.loc[0, "pred_status"]
    classes = list(model.classes_)
    probas = {c: float(result.loc[0, f"proba_{c}"]) for c in classes}
    probas_sorted = dict(sorted(probas.items(), key=lambda kv: kv[1], reverse=True))
 
    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Hasil Prediksi")
        st.success(f"Prediksi status: **{pred_label}**")
 
        top_class, top_p = next(iter(probas_sorted.items()))
        st.write(f"Probabilitas tertinggi: **{top_class}** = **{top_p:.2%}**")
 
        st.markdown("**Catatan interpretasi (praktis):**")
        st.write(
            "Jika probabilitas **Dropout** tinggi, prioritaskan intervensi lebih cepat "
            "(konseling akademik, bantuan finansial, monitoring kehadiran/performansi)."
        )
 
    with c2:
        st.subheader("Probabilitas per kelas")
        st.dataframe(
            pd.DataFrame({"class": list(probas_sorted.keys()), "probability": list(probas_sorted.values())}),
            use_container_width=True,
        )
 
# =========================
# Batch prediction via CSV
# =========================
st.divider()
st.subheader("Prediksi Batch (Upload CSV)")
 
uploaded = st.file_uploader("Upload file CSV dengan kolom sesuai dataset (tanpa kolom Status)", type=["csv"])
if uploaded is not None:
    try:
        df_u = pd.read_csv(uploaded, sep=";")
        # Jika user upload masih punya kolom Status, drop dulu
        if schema["target"] in df_u.columns:
            df_u = df_u.drop(columns=[schema["target"]])
 
        missing = [f["name"] for f in schema["features"] if f["name"] not in df_u.columns]
        if missing:
            st.error(f"Kolom kurang: {missing[:10]}{' ...' if len(missing) > 10 else ''}")
        else:
            df_u = df_u[[f["name"] for f in schema["features"]]]
            out = predict_dataframe(df_u)
            st.success("Selesai memprediksi.")
            st.dataframe(out.head(50), use_container_width=True)
 
            st.download_button(
                "Download hasil prediksi (CSV)",
                data=out.to_csv(index=False).encode("utf-8"),
                file_name="predictions.csv",
                mime="text/csv",
            )
    except Exception as e:
        st.exception(e)
