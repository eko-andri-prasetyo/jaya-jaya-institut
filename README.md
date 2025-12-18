# Submission Akhir — Menyelesaikan Permasalahan Institusi Pendidikan (Jaya Jaya Institut)
**Kelas:** Belajar Penerapan Data Science (Dicoding)  
**Nama Institusi (Studi Kasus):** Jaya Jaya Institut  
**Nama Peserta:** Eko Andri Prasetyo  
**Username Dicoding:** ekoandriprasetyo  

Repo/folder ini disusun agar memenuhi **5 kriteria wajib** pada submission:
1) pakai template proyek,  
2) end-to-end proses data science,  
3) minimal 1 dashboard,  
4) minimal 1 solusi ML siap pakai (Streamlit) + deploy,  
5) action items.

---

## 1. Business Understanding

**Masalah:** Jaya Jaya Institut memiliki angka **dropout** yang relatif tinggi.  
**Tujuan:** mendeteksi sedini mungkin mahasiswa yang berpotensi **Dropout** sehingga institusi dapat melakukan intervensi/bimbingan.

**Target ML:** memprediksi kolom **`Status`** (kelas: `Dropout`, `Enrolled`, `Graduate`) berdasarkan fitur-fitur pendaftaran & performa akademik.

---

## 2. Dataset

Sumber data:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dalam proyek ini, file data sudah disalin ke: `data/data.csv`.

---

## 3. Struktur Folder

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

## 4. Setup Environment (Local)

### 4.1 Buat dan aktifkan virtual env
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

### 4.2 Install dependencies
```bash
pip install -r requirements.txt
```

---

## 5. Notebook (End-to-End Data Science)

Buka dan jalankan `notebook.ipynb` dari awal sampai akhir.
Notebook mencakup:
- Business understanding (tujuan & KPI)
- Load data + EDA
- Preprocessing + training model multiclass
- Evaluasi (accuracy, macro F1, confusion matrix)
- Export model ke `model/model.joblib`
- Pembuatan SQLite database untuk dashboard: `dashboard/students.db`

---

## 6. Prototype Machine Learning (Streamlit)

### 6.1 Jalankan local
```bash
streamlit run app.py
```

Fitur pada prototype:
- Prediksi 1 data (form sidebar)
- Prediksi batch (upload CSV)
- Menampilkan probabilitas per kelas

### 6.2 Deploy ke Streamlit Community Cloud
1. Push folder submission ini ke GitHub (public).
2. Pastikan file `app.py`, `requirements.txt`, folder `model/` ikut ter-commit.
3. Di Streamlit Community Cloud: pilih repo → pilih `app.py` → Deploy.
4. Tempel link deploy Anda di sini:

**Link Streamlit Cloud:** _(isi sendiri setelah deploy)_  
`https://jaya-jaya-institut-ekoandriprasetyo.streamlit.app`

---

## 7. Business Dashboard (Metabase v0.57.3)

> **Penting:** File `metabase.db.mv.db` pada repo ini adalah *placeholder*. Anda **WAJIB** menggantinya dengan hasil export dari Metabase Anda sebelum submit.
> Jalankan `python check_submission.py` untuk memastikan tidak ada file placeholder.

> Untuk memenuhi kriteria 3, buat dashboard visual (bukan tabel saja).

### 7.1 Jalankan Metabase (Docker)
```bash
docker run -d --name jayainstitut -p 3000:3000 -v c:/submission:/metabase.db -v c:/submission/students.db:/data/students.db -e MB_DB_FILE=/metabase.db/metabase.db metabase/metabase
```

Buka: [http://localhost:3000](http://localhost:3000/dashboard/2-jaya-jaya-institute-students-dropout-analysis)

### 7.2 Kredensial reviewer
Gunakan (atau buat akun dengan):
- Email: **root@mail.com**
- Password: **root123**

### 7.3 Hubungkan database ke Metabase
Gunakan SQLite file: `dashboard/students.db`  
Tabel utama: `students`

### 7.4 Rekomendasi isi dashboard (minimal)
- KPI: Total mahasiswa, Dropout rate, Graduate rate
- Dropout rate by Course
- Status by Debtor (0/1)
- Status by Scholarship holder (0/1)
- Distribusi Admission grade per Status
- Performa semester 1/2 (enrolled/approved) vs Status

### 7.5 Screenshot dashboard
Simpan screenshot ke file:
`ekoandriprasetyo-dashboard.png`

### 7.6 Export database Metabase (metabase.db.mv.db)
Setelah dashboard selesai dibuat, export DB metabase:
```bash
docker cp metabase:/metabase.db/metabase.db.mv.db ./
```

Lalu taruh file itu di folder submission (root): `metabase.db.mv.db`

---

## 8. Conclusion (ringkas)

Model baseline multiclass (Logistic Regression + scaling) menghasilkan metrik (lihat `model/metrics.json`):
- Accuracy: 0.7288
- Macro F1: 0.6927

---

## 9. Action Items (Rekomendasi)

1. **Early warning system**: lakukan monitoring rutin mahasiswa dengan probabilitas `Dropout` tinggi, prioritas konseling akademik & psikologis.
2. **Intervensi finansial**: fokus pada kelompok **Debtor** dan status pembayaran, sediakan skema keringanan/angsuran.
3. **Program remedial semester awal**: jika indikator semester 1/2 (approved rendah) mengarah ke dropout, lakukan kelas tambahan & tutor.
4. **Audit per Course**: jika ada course dengan dropout tinggi, evaluasi beban kurikulum, kualitas pengajaran, dan sistem penilaian.
5. **Dashboard monitoring bulanan**: tetapkan target penurunan dropout per semester dan evaluasi progres via dashboard.

