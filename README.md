# Submission Akhir — Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)
**Kelas:** Belajar Penerapan Data Science (Dicoding)  
**Nama Institusi (Studi Kasus):** Jaya Jaya Institut  
**Nama Peserta:** Eko Andri Prasetyo  
**Username Dicoding:** ekoandriprasetyo  

## 📌 1. Deskripsi Proyek

Proyek ini bertujuan untuk membantu **Jaya Jaya Institut** dalam mengatasi permasalahan **tingginya angka dropout mahasiswa** dengan memanfaatkan pendekatan *data science*. Melalui analisis data historis mahasiswa, proyek ini membangun **model klasifikasi multikelas** untuk memprediksi status mahasiswa (`Dropout`, `Enrolled`, `Graduate`) serta menghasilkan *insight* yang dapat digunakan sebagai dasar pengambilan keputusan.

Model yang dihasilkan diimplementasikan dalam bentuk **prototype aplikasi Streamlit** sehingga dapat digunakan langsung untuk prediksi individu maupun prediksi batch (unggah CSV).

---

## 🎯 2. Business Understanding

### Permasalahan
Institusi pendidikan kesulitan dalam:
- Mengidentifikasi mahasiswa yang berpotensi melakukan dropout sejak dini  
- Mengetahui faktor utama penyebab mahasiswa berhenti studi  
- Menyusun strategi intervensi yang tepat sasaran dan berbasis data  

### Tujuan
- Mengidentifikasi **karakteristik umum mahasiswa yang berisiko dropout**
- Membangun **model prediksi status mahasiswa**
- Memberikan **rekomendasi berbasis data** untuk menurunkan angka dropout

---

## 📊 3. Data Understanding

Dataset berisi informasi mahasiswa yang mencakup:
- **Performa akademik semester awal** (mata kuliah lulus, nilai/grade)
- **Kondisi finansial** (Debtor, status pembayaran, beasiswa)
- **Informasi demografis** (usia saat pendaftaran, status internasional, program studi)
- **Status akhir mahasiswa** (`Dropout`, `Enrolled`, `Graduate`) sebagai target

Tahapan yang dilakukan:
- Pengecekan struktur dan tipe data
- Identifikasi *missing value* dan duplikasi data
- Analisis distribusi target dan potensi *class imbalance*

Sumber data:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dalam proyek ini, file data sudah disalin ke: `data/data.csv`.

---

## 🧹 4. Data Preparation

Tahapan *data preparation* meliputi:
- Penanganan *missing value* menggunakan imputasi median
- Standarisasi fitur numerik
- Pemisahan data latih dan data uji secara stratified
- Pipeline preprocessing untuk memastikan konsistensi antara training dan inference

---

## 🤖 5. Modeling

Model yang digunakan adalah **Logistic Regression multikelas** dengan pipeline:
- Imputer (median)
- StandardScaler
- Logistic Regression (`class_weight='balanced'`)

**Target:** kolom `Status`  
**Metrik evaluasi utama:** Macro F1-score (untuk mengatasi ketidakseimbangan kelas)

Model disimpan dalam berkas:
- `model/model.joblib`
- `model/schema.json` (untuk form Streamlit)
- `model/metrics.json`

---

## 📈 6. Evaluation

Hasil evaluasi menunjukkan bahwa model memiliki performa yang baik dalam membedakan status mahasiswa.  
Macro F1-score digunakan sebagai metrik utama karena distribusi kelas target tidak seimbang.  
Confusion matrix dan classification report digunakan untuk memahami kesalahan prediksi pada tiap kelas.

---

## 🧠 7. Karakteristik Umum Mahasiswa yang Berpotensi Melakukan Dropout

Berdasarkan hasil analisis data, EDA, dan pemodelan klasifikasi, mahasiswa dengan risiko dropout lebih tinggi umumnya memiliki karakteristik sebagai berikut:

1. **Performa akademik semester awal rendah**  
   Mahasiswa dengan jumlah mata kuliah lulus yang lebih sedikit dan nilai semester awal yang rendah menunjukkan probabilitas dropout yang lebih tinggi. Semester awal menjadi fase krusial dalam keberlanjutan studi.

2. **Permasalahan finansial**  
   Status sebagai **Debtor**, keterlambatan pembayaran, atau biaya kuliah yang tidak *up-to-date* berkorelasi dengan peningkatan risiko dropout. Sebaliknya, mahasiswa penerima beasiswa cenderung lebih stabil.

3. **Perbedaan risiko antar program studi**  
   Beberapa program studi menunjukkan kecenderungan dropout yang lebih tinggi, yang dapat menjadi sinyal perlunya evaluasi kurikulum atau sistem pendampingan.

4. **Faktor demografis tertentu**  
   Usia saat pendaftaran yang lebih tinggi dapat berkaitan dengan tantangan eksternal (pekerjaan, keluarga) sehingga meningkatkan risiko dropout.

Dropout umumnya **tidak disebabkan oleh satu faktor tunggal**, melainkan kombinasi faktor akademik dan finansial yang saling berkaitan.

---

## 🔍 8. Kesimpulan

Proyek ini membuktikan bahwa pendekatan *data science* dapat digunakan untuk **memprediksi risiko dropout mahasiswa** secara efektif. Dengan memanfaatkan data akademik, finansial, dan demografis, institusi pendidikan dapat melakukan **deteksi dini** terhadap mahasiswa berisiko dan merancang intervensi yang lebih tepat sasaran.

---

## 💡 9. Rekomendasi untuk Institusi Pendidikan

- Menerapkan **early warning system berbasis data**
- Menyediakan **pendampingan akademik pada semester awal**
- Memberikan **dukungan finansial atau skema pembayaran fleksibel**
- Melakukan evaluasi program studi dengan tingkat dropout tinggi
- Memantau kondisi mahasiswa secara berkala melalui dashboard

---

## 🚀 10. Implementasi Aplikasi

Prototype aplikasi dikembangkan menggunakan **Streamlit** dan mendukung:
- Prediksi satu mahasiswa melalui form input
- Prediksi batch melalui unggah file CSV
- Unduhan hasil prediksi dalam format CSV

Aplikasi menggunakan model yang dihasilkan dari notebook ini secara konsisten.

### 10.1 Buat dan aktifkan virtual env
Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Mac/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 10.2 Install dependencies
```bash
pip install -r requirements.txt
```

### 10.3. Notebook (End-to-End Data Science)

Buka dan jalankan `notebook.ipynb` dari awal sampai akhir.
Notebook mencakup:
- Business understanding (tujuan & KPI)
- Load data + EDA
- Preprocessing + training model multiclass
- Evaluasi (accuracy, macro F1, confusion matrix)
- Export model ke `model/model.joblib`
- Pembuatan SQLite database untuk dashboard: `dashboard/students.db`

### 10.4. Prototype Machine Learning (Streamlit), jalankan lokal

```bash
streamlit run app.py
```

Fitur pada prototype:
- Prediksi 1 data (form sidebar)
- Prediksi batch (upload CSV)
- Menampilkan probabilitas per kelas

### 10.5 Deploy ke Streamlit Community Cloud
1. Push folder submission ini ke GitHub (public).
2. Pastikan file `app.py`, `requirements.txt`, folder `model/` ikut ter-commit.
3. Di Streamlit Community Cloud: pilih repo → pilih `app.py` → Deploy.
4. Tempel link deploy Anda di sini:

**Link Streamlit Cloud:** _(isi sendiri setelah deploy)_  
`https://jaya-jaya-institut-ekoandriprasetyo.streamlit.app`


### 10.6 Business Dashboard (Metabase v0.57.3), jalankan Metabase via Docker
a. buat folder submission
```bash
mkdir C:\submission
```
b. ekstrak file submission-jayainstitut-ekoandriprasetyo.zip ke C:\
```bash
tar -xf submission_final_ekoandriprasetyo.zip -C C:\
```
c. buka command prompt, ketikkan perintah
```bash
cd c:\submission
```
d. jalankan metabase via docker
```bash
docker run -d --name jayainstitut -p 3000:3000 -v c:/submission:/metabase.db -v c:/submission/students.db:/data/students.db -e MB_DB_FILE=/metabase.db/metabase.db metabase/metabase
```
e. buka dashboard melalui URL
```bash
http://localhost:3000/dashboard/2-jaya-jaya-institute-students-dropout-analysis
```

### 10.7 Kredensial reviewer
- Email: **root@mail.com**
- Password: **root123**

### 10.8 Screenshot dashboard
Screenshot dashboard tersimpan dengan nama file:
`ekoandriprasetyo-dashboard.png`

---

## 11. Struktur Folder

```
submission/
├── model/
│   ├── model.joblib
│   ├── schema.json
│   └── metrics.json
├── dashboard/
│   └── students.db
├── data/
│   └── data.csv
├── notebook.ipynb
├── app.py
└── requirements.txt
```

---
