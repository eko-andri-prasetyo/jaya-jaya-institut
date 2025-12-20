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
docker run -d --name jayainstitut -p 3000:3000 ^
  -v c:/submission:/metabase.db ^
  -v c:/submission/students.db:/data/students.db ^
  -e MB_DB_FILE=/metabase.db/metabase.db ^
  metabase/metabase:v0.57.3
```

#### 5. Akses dashboard
Buka browser:
```
http://localhost:3000/dashboard/2-jaya-jaya-institute-students-dropout-analysis
```

### Kredensial Reviewer
- **Email:** root@mail.com  
- **Password:** root123
