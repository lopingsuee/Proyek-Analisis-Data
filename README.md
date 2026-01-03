# Proyek Analisis Data

**Bike Sharing Dataset**

##  Deskripsi Proyek

Repository ini dibuat sebagai **submission proyek akhir** untuk course **Belajar Fundamental Analisis Data** di Dicoding.
Proyek ini bertujuan untuk menerapkan seluruh tahapan analisis data, mulai dari **data wrangling**, **exploratory data analysis (EDA)**, **visualisasi**, hingga **pembuatan dashboard interaktif** menggunakan Streamlit.

Dataset yang digunakan adalah **Bike Sharing Dataset**, yang berisi data peminjaman sepeda harian beserta informasi kondisi cuaca dan tipe hari.

---

## Tujuan Proyek

Tujuan utama dari proyek ini adalah:

* Melakukan proses analisis data secara end-to-end
* Menjawab pertanyaan bisnis menggunakan data
* Menyajikan hasil analisis dalam bentuk visualisasi yang informatif
* Membangun dashboard sederhana yang interaktif dan dapat dijalankan secara lokal

---

## Pertanyaan Bisnis

Proyek ini berfokus untuk menjawab dua pertanyaan utama:

1. **Bagaimana perbedaan rata-rata jumlah peminjaman sepeda harian pada setiap kondisi cuaca selama periode pengamatan dataset?**
2. **Bagaimana perbedaan rata-rata jumlah peminjaman sepeda harian berdasarkan tipe hari (Working Day, Weekend, dan Holiday)?**

---

## Struktur Direktori

Struktur repository ini adalah sebagai berikut:

```
submission
├── dashboard
│   ├── main_data.csv
│   └── dashboard.py
├── data
│   ├── data_1.csv
│   └── data_2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

**Penjelasan:**

* `data/` : Berisi dataset mentah
* `notebook.ipynb` : Notebook analisis data (data wrangling, EDA, visualisasi, dan insight)
* `dashboard/` :

  * `main_data.csv` : Data yang telah diproses dan digunakan untuk dashboard
  * `dashboard.py` : File aplikasi Streamlit
* `requirements.txt` : Daftar library yang digunakan
* `url.txt` : Link dashboard Streamlit Cloud
* `README.md` : Dokumentasi proyek

---

## Tahapan Analisis Data

Proyek ini mencakup tahapan berikut:

1. **Data Gathering**
   Mengambil dan memuat data Bike Sharing Dataset.

2. **Data Assessing**
   Mengecek kualitas data, tipe data, dan kelengkapan data.

3. **Data Cleaning**

   * Konversi tipe data tanggal
   * Mapping variabel kategorikal (cuaca dan tipe hari)
   * Menyiapkan data agar siap dianalisis

4. **Exploratory Data Analysis (EDA)**
   Menganalisis pola peminjaman sepeda berdasarkan kondisi cuaca dan tipe hari.

5. **Visualization & Explanatory Analysis**
   Membuat visualisasi untuk menjawab pertanyaan bisnis dan menjelaskan insight yang diperoleh.

6. **Dashboard Development**
   Membangun dashboard interaktif menggunakan **Streamlit**.

---

## Dashboard

Dashboard dibuat menggunakan **Streamlit** dan menampilkan:

* Rata-rata peminjaman sepeda berdasarkan kondisi cuaca
* Rata-rata peminjaman sepeda berdasarkan tipe hari
* Tren peminjaman sepeda dari waktu ke waktu
* Filter interaktif berdasarkan rentang tanggal, kondisi cuaca, dan tipe hari

Dashboard dapat dijalankan secara lokal maupun diakses melalui Streamlit Cloud.

---

## Cara Menjalankan Dashboard Secara Lokal

1. Clone repository ini:

   ```bash
   git clone <url-repository>
   ```

2. Masuk ke folder dashboard:

   ```bash
   cd submission/dashboard
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi Streamlit:

   ```bash
   streamlit run dashboard.py
   ```

---

## Library yang Digunakan

* pandas
* matplotlib
* seaborn
* streamlit

---

## Kesimpulan Singkat

Hasil analisis menunjukkan bahwa:

* Kondisi cuaca berpengaruh terhadap jumlah peminjaman sepeda, dengan cuaca cerah menghasilkan peminjaman tertinggi.
* Hari kerja memiliki rata-rata peminjaman sepeda lebih tinggi dibandingkan akhir pekan dan hari libur.
* Penggunaan sepeda pada hari non-kerja cenderung lebih bervariasi dan dipengaruhi faktor eksternal.

---

## Pesan Author:)

Proyek ini disusun sebagai bagian dari submission course **Belajar Fundamental Analisis Data – Dicoding**.

---
