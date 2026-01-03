# Bike Sharing Dashboard 

**Submission – Belajar Fundamental Analisis Data (Dicoding)**

Dashboard ini dibuat sebagai bagian dari **submission proyek akhir** pada course **Belajar Fundamental Analisis Data** di Dicoding.
Dashboard menyajikan hasil analisis data peminjaman sepeda berdasarkan **kondisi cuaca** dan **tipe hari** secara interaktif menggunakan **Streamlit**.

---

##  Setup Environment – Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

---

##  Setup Environment – Shell / Terminal

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pip install -r requirements.txt
```

---

##  Run Streamlit App

Masuk ke folder `dashboard`, lalu jalankan:

```bash
streamlit run dashboard.py
```

Pastikan file berikut tersedia:

* `dashboard/dashboard.py`
* `dashboard/main_data.csv`
* `requirements.txt`

---

##  Fitur Dashboard

* Visualisasi rata-rata peminjaman sepeda berdasarkan kondisi cuaca
* Visualisasi rata-rata peminjaman sepeda berdasarkan tipe hari (Working Day, Weekend, Holiday)
* Tren peminjaman sepeda dari waktu ke waktu
* Filter interaktif:

  * Rentang tanggal
  * Kondisi cuaca
  * Tipe hari

---

##  Insight Utama

* Cuaca cerah menghasilkan rata-rata peminjaman sepeda tertinggi.
* Hari kerja memiliki peminjaman sepeda yang lebih tinggi dan stabil dibandingkan akhir pekan dan hari libur.
* Peminjaman pada hari non-kerja cenderung lebih bervariasi dan dipengaruhi faktor eksternal.

---

##  Deployment

Dashboard ini telah dideploy menggunakan **Streamlit Community Cloud**.
Link dashboard dapat dilihat pada file `url.txt`.

---

##  Author

Submission proyek untuk course **Belajar Fundamental Analisis Data – Dicoding**.

---
