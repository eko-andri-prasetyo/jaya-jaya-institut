# Submission Akhir – Menyelesaikan Permasalahan Institusi Pendidikan
**Kelas:** Belajar Penerapan Data Science (Dicoding)  
**Nama Institusi (Studi Kasus):** Jaya Jaya Institut  
**Nama Peserta:** Eko Andri Prasetyo  
**Username Dicoding:** ekoandriprasetyo  

---

## 1. Latar Belakang (Business Understanding)
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan memiliki reputasi lulusan yang baik. Namun demikian, institusi ini menghadapi permasalahan serius berupa **tingginya angka mahasiswa dropout** (tidak menyelesaikan pendidikan).

Tingginya tingkat dropout berdampak pada:
- Penurunan reputasi institusi
- Kerugian finansial
- Tidak optimalnya proses pembelajaran

Oleh karena itu, Jaya Jaya Institut membutuhkan solusi berbasis data untuk **mendeteksi mahasiswa yang berpotensi dropout sedini mungkin**, sehingga dapat diberikan bimbingan atau intervensi yang tepat.

---

## 2. Tujuan Proyek
Tujuan dari proyek ini adalah:
1. Menganalisis faktor-faktor yang memengaruhi status mahasiswa (Dropout, Enrolled, Graduate).
2. Mengembangkan **model machine learning** untuk memprediksi status mahasiswa.
3. Menyediakan **dashboard** untuk membantu institusi memonitor performa mahasiswa.
4. Membangun **prototype aplikasi machine learning** yang siap digunakan oleh user.
5. Memberikan **rekomendasi action items** berbasis hasil analisis.

---

## 3. Dataset
Dataset yang digunakan berasal dari Dicoding dan dapat diakses melalui tautan berikut:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dataset berisi informasi demografis, akademik, dan sosial ekonomi mahasiswa, dengan target variabel **Status** yang terdiri dari:
- Dropout
- Enrolled
- Graduate

---

## 4. Tahapan Proyek Data Science
Proyek ini mengikuti tahapan standar data science sebagai berikut:

1. Business Understanding  
2. Data Understanding  
3. Data Preparation  
4. Modeling  
5. Evaluation  
6. Deployment  

---

## 5. Business Dashboard
Dashboard dibuat menggunakan **Metabase** untuk memudahkan pihak institusi dalam memahami data dan memonitor performa mahasiswa.

**Akses Dashboard (untuk reviewer):**
- Email: `root@mail.com`
- Password: `root123`

File database Metabase disertakan dalam submission:
```
metabase.db.mv.db
```

---

## 6. Solusi Machine Learning (Prototype Streamlit)
Prototype machine learning dikembangkan menggunakan **Streamlit** dan siap digunakan oleh user.

**Fitur utama:**
- Prediksi tunggal melalui form input
- Prediksi batch melalui upload CSV
- Dukungan delimiter `,` dan `;`
- Penghapusan kolom `Status` secara otomatis
- Hasil prediksi dapat diunduh

---

## 7. Cara Menjalankan Prototype Secara Lokal

### 7.1 Membuat Virtual Environment
```bash
python -m venv venv
```

### 7.2 Aktivasi Virtual Environment
```bash
venv\Scripts\activate        # Windows
source venv/bin/activate      # Linux / macOS
```

### 7.3 Instalasi Dependensi
```bash
pip install -r requirements.txt
```

### 7.4 Menjalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi dapat diakses melalui:
```
http://localhost:8501
```

---

## 8. Deployment ke Streamlit Community Cloud
Prototype machine learning ini **telah berhasil dideploy ke Streamlit Community Cloud** dan dapat diakses secara remote.

🔗 **Link Prototype Streamlit (Cloud):**  
https://jaya-jaya-institut-ekoandriprasetyo.streamlit.app/

Apabila aplikasi tidak dapat diakses sementara karena batasan fair-use Streamlit, prototype tetap dapat dijalankan secara lokal.

---

## 9. Action Items (Rekomendasi)
1. Penerapan early warning system bagi mahasiswa berisiko dropout.
2. Pendampingan akademik pada semester awal.
3. Bantuan atau keringanan finansial bagi mahasiswa bermasalah.
4. Monitoring berkala menggunakan dashboard.
5. Evaluasi program studi dengan dropout rate tinggi.

---

## 10. Kesimpulan
Proyek ini berhasil membangun solusi data science end-to-end yang mencakup analisis data, dashboard, model machine learning, serta prototype aplikasi yang siap digunakan oleh user. Seluruh kriteria submission Dicoding telah terpenuhi.

---

## 11. Struktur Folder Submission
```
submission/
├── model/
├── notebook.ipynb
├── app.py
├── README.md
├── requirements.txt
├── metabase.db.mv.db
├── ekoandriprasetyo-dashboard.png
```

---

**Catatan:**  
Proyek ini dibuat untuk keperluan pembelajaran dan mengikuti seluruh ketentuan Dicoding.
