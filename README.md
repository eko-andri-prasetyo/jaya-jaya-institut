# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)

## Business Understanding
Jaya Jaya Institut mengalami tantangan **tingginya angka dropout mahasiswa**. Jika dropout bisa dideteksi lebih awal, institusi dapat melakukan intervensi (akademik/finansial) yang lebih tepat sasaran untuk meningkatkan retensi dan kelulusan.

### Permasalahan Bisnis
Permasalahan yang ingin diselesaikan pada proyek ini:
- Institusi belum memiliki mekanisme **deteksi dini** mahasiswa berisiko dropout.
- Sulit mengetahui **faktor utama** yang berkorelasi dengan dropout (akademik, finansial, demografi, program studi).
- Intervensi yang dilakukan masih belum konsisten karena belum berbasis data.

### Cakupan Proyek
Cakupan pekerjaan pada proyek ini:
- Melakukan **EDA** untuk memahami pola dropout dan fitur-fitur yang berpengaruh.
- Membangun **model machine learning klasifikasi multikelas** untuk memprediksi status mahasiswa: `Dropout`, `Enrolled`, `Graduate`.
- Menyediakan **prototype aplikasi** (Streamlit) untuk prediksi individu dan prediksi batch (upload CSV).
- Menyediakan **business dashboard** (Metabase) untuk monitoring kondisi mahasiswa (opsional untuk reviewer yang ingin mengecek dashboard).

### Persiapan

Sumber data:  
- Dataset Dicoding (students performance): https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv  
- Pada submission ini, dataset sudah disalin ke: `data/data.csv`.

Setup environment (jalankan di folder submission):

```bash
# (opsional) buat virtual env
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Mac/Linux
# source .venv/bin/activate

# install dependency
pip install -r requirements.txt
```

#### Struktur Folder
```
submission/
├── model/
│   ├── model.joblib
│   ├── metrics.json
│   ├── schema.json
├── notebook.ipynb
├── notebook.py
├── app.py
├── batch-inference.csv
├── data.csv
├── README.md
├── ekoandriprasetyo-dashboard.png
├── metabase.db.mv.db
├── metabase.db.trace.db
├── students.db
└── requirements.txt
```

## Business Dashboard (Metabase)

Proyek ini menyediakan **Business Dashboard** menggunakan **Metabase v0.57.3** untuk membantu Jaya Jaya Institut dalam memantau performa mahasiswa dan tingkat dropout secara menyeluruh. Dashboard dirancang ringkas, informatif, dan mudah dipahami oleh stakeholder non-teknis.

### Tujuan Dashboard
Dashboard digunakan untuk:
- Memantau **jumlah total mahasiswa** dan **dropout rate** sebagai indikator utama.
- Melihat **distribusi status mahasiswa** (Dropout, Enrolled, Graduate).
- Mengidentifikasi **program studi dengan tingkat dropout tinggi**.
- Menganalisis pengaruh **faktor finansial** (Debtor dan Scholarship).
- Membandingkan **performa akademik awal** berdasarkan status mahasiswa.

### Ringkasan Insight Utama
Berdasarkan visualisasi dashboard:
- Sekitar **32% mahasiswa berstatus Dropout**, menunjukkan permasalahan yang signifikan.
- Beberapa **program studi memiliki dropout rate lebih tinggi**, sehingga perlu prioritas evaluasi.
- Mahasiswa dengan **tunggakan pembayaran (Debtor)** dan **tanpa beasiswa** menunjukkan kecenderungan dropout lebih besar.
- Mahasiswa **Graduate** memiliki rata-rata **Admission Grade** lebih tinggi dibandingkan Dropout, mengindikasikan pentingnya performa akademik awal.

Insight ini **konsisten dengan hasil eksplorasi data dan kesimpulan proyek**, serta mendukung rekomendasi penerapan *early warning system* dan intervensi akademik maupun finansial.

### Menjalankan Dashboard (Metabase via Docker)

#### 1. Buat folder submission
```bash
mkdir C:\submission
```

#### 2. Ekstrak file submission
```bash
tar -xf submission-jayainstitut-ekoandriprasetyo.zip -C C:\submission
```

#### 3. Masuk ke folder submission
```bash
cd C:\submission
```

#### 4. Jalankan Metabase
```bash
docker run -d --name jayainstitut -p 3000:3000 -v c:/submission:/metabase.db -v c:/submission/students.db:/data/students.db -e MB_DB_FILE=/metabase.db/metabase.db metabase/metabase:v0.57.3
```

#### 5. Akses dashboard
Buka browser:
```
http://localhost:3000/dashboard/2-jaya-jaya-institute-students-dropout-analysis
```

### Kredensial Reviewer
- **Email:** root@mail.com  
- **Password:** root123


## Menjalankan Sistem Machine Learning
Prototype machine learning dibuat dengan **Streamlit** dan mendukung:
- Prediksi **1 mahasiswa** melalui form input.
- Prediksi **batch** melalui unggah file CSV.
- Unduh hasil prediksi dalam format CSV (untuk batch).

Link prototype (Streamlit Community Cloud):  
`https://jaya-jaya-institut-ekoandriprasetyo.streamlit.app`

Cara menjalankan prototype secara lokal:

```bash
streamlit run app.py
```

### Prediksi Batch (Upload CSV)

Prototype mendukung prediksi batch menggunakan file CSV.
Untuk memudahkan pengujian, disediakan contoh file CSV
yang telah disesuaikan dengan skema fitur model dan **tidak menyertakan
kolom target (Status)**.

File contoh:
- `batch_inference_sample.csv`

File ini dapat langsung diunggah ke aplikasi Streamlit pada menu
**Prediksi Batch (Upload CSV)** untuk menguji proses inference secara batch.


## Conclusion
Dari hasil analisis data dan pemodelan, dropout pada Jaya Jaya Institut **cenderung dipengaruhi oleh kombinasi** faktor akademik dan finansial, bukan satu faktor tunggal.

Karakteristik umum mahasiswa yang berisiko dropout lebih tinggi (berdasarkan EDA & pemodelan):
- **Performa akademik semester awal rendah** (jumlah mata kuliah lulus lebih sedikit / nilai awal lebih rendah).
- **Permasalahan finansial**, misalnya status **Debtor** atau pembayaran biaya kuliah yang tidak up-to-date.
- **Perbedaan risiko antar program studi**, sehingga beberapa prodi perlu perhatian/intervensi lebih.
- **Faktor demografis tertentu**, misalnya usia saat pendaftaran yang lebih tinggi yang bisa berkaitan dengan tantangan eksternal.

Dengan prototype model yang dibuat, institusi dapat melakukan **deteksi dini** mahasiswa berisiko dan menyiapkan intervensi yang lebih cepat dan tepat sasaran.

### Rekomendasi Action Items
Berikut rekomendasi action items yang dapat diterapkan institusi:
- Menerapkan **early warning system** berbasis prediksi model + threshold risiko.
- Menjalankan **pendampingan akademik semester awal** (kelas remedial, tutoring, monitoring kehadiran/performansi).
- Menyediakan **dukungan finansial** (skema cicilan fleksibel, beasiswa/relief untuk kelompok berisiko).
- Melakukan **evaluasi kurikulum & layanan pendampingan** pada program studi dengan dropout tinggi.
- Memantau tren dropout secara berkala melalui **dashboard** untuk pengambilan keputusan yang lebih cepat.
