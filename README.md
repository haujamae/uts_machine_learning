# uts_machine_learning
# Dokumentasi Sistem Pipeline Machine Learning - Pohon Pintar

Proyek ini merupakan implementasi pipeline *Machine Learning* terstruktur menggunakan algoritma **Random Forest Regressor** untuk memprediksi tren konsentrasi gas Karbon Monoksida (CO) berdasarkan kondisi mikro-klimat (Suhu dan Kelembapan) di sekitar pohon. Sistem ini dirancang secara modular (terpisah per tahap) untuk dieksekusi melalui PowerShell/Terminal.

## 👥 Anggota Kelompok / Identitas
- **Elda Oktavia Astutiningtyas** 
- **Fatma Rizzah Jibrina Haujam** 
- **Saga Al Mi'raj** 
---

## 📂 Struktur File Proyek
Semua file harus berada dalam satu direktori kerja yang sama agar dapat dieksekusi dengan benar:
* `data_pohon.xlsx` : Dataset mentah hasil eksperimen sensor fisik (86.400 baris).
* `1_data_loading.py` : Skrip untuk memuat dan memeriksa struktur dataset awal.
* `2_data_cleaning.py` : Skrip untuk pengecekan missing values dan duplikasi data.
* `3_target_fitur.py` : Skrip penentu fitur (X) dan pembuatan target ilmiah (y).
* `4_preprocessing_scaling.py` : Skrip pembagian dataset dan standarisasi nilai sensor.
* `5_traning_rf.py` : Skrip pelatihan model Random Forest dan evaluasi metrik.
* `6_inference.py` : Skrip pengujian satu sampel data baru menggunakan model yang sudah dilatih.

---

## 🛠️ Langkah-Langkah Eksekusi Program (PowerShell)

### 1. Instalasi Pustaka Dependensi
Sebelum menjalankan program, pastikan modul-modul berikut telah terpasang:
```powershell
pip install pandas openpyxl scikit-learn joblib
```

### 2. Alur Pipeline Tahap demi Tahap
Jalankan perintah berikut secara berurutan di dalam Windows PowerShell:

```powershell
python 1_data_loading.py
python 2_data_cleaning.py
python 3_target_fitur.py
python 4_preprocessing_scaling.py
python 5_training_rf.py
python 6_inference.py
```

---

## 📝 Penjelasan Detail Alur Kerja Sistem (Pipeline ML)

### Step 1: Data Loading (`1_data_loading.py`)
Memuat dataset `data_pohon.xlsx` ke dalam DataFrame Pandas dengan penyesuaian tanda koma desimal (`decimal=','`). Program memastikan nama kolom, jumlah baris (86.400), dan tipe data (`float64`/`int64`) telah tervalidasi dengan benar sebelum masuk ke tahap berikutnya.

### Step 2: Data Cleaning (`2_data_cleaning.py`)
Melakukan audit kualitas data dengan menghitung nilai kosong (*missing values*) dan memeriksa adanya baris duplikat. Tahap ini mendokumentasikan jumlah baris sebelum dan sesudah proses pembersihan untuk memastikan integritas data, lalu menyimpan hasilnya ke dalam `data_pohon_clean.csv`.

### Step 3: Menentukan Target & Fitur (`3_target_fitur.py`)
Untuk memenuhi kaidah ilmiah, target (y) dirancang menggunakan metode regresi deret waktu (*time-series forecasting*), yaitu **memprediksi nilai sensor ADC MQ-7 pada satu baris waktu berikutnya (`Target_MQ7_Next`)**. 
* **Fitur (Input X):** `Suhu DHT (°C)`, `Kelembapan DHT (%)`, dan `ADC MQ-7` saat ini.
* **Target (Output y):** Nilai `ADC MQ-7` di detik/menit berikutnya.

### Step 4: Preprocessing & Scaling (`4_preprocessing_scaling.py`)
* **Data Splitting:** Dataset dibagi menjadi **80% Training Set** dan **20% Testing Set** berdasarkan urutan waktu (bukan acak) untuk mencegah terjadinya *data leakage* (kebocoran data) pada data deret waktu.
* **Feature Scaling:** Menggunakan `StandardScaler`. Parameter skala (*mean* dan *variance*) **hanya dipelajari dari Training Set** dan disimpan ke file `scaler.pkl` agar bisa diterapkan dengan identik pada data baru (*testing/inference*).

### Step 5: Training Random Forest (`5_training_rf.py`)
Melatih algoritma `RandomForestRegressor` (100 pohon keputusan acak) menggunakan data training yang sudah terskala. Performa model dievaluasi menggunakan metrik evaluasi regresi standar industri:
* **Mean Absolute Error (MAE):** ~5.39 (Rata-rata kesalahan tebakan model hanya meleset sebesar ±5 nilai ADC).
* **Root Mean Squared Error (RMSE):** ~7.46
* **R-Squared (R² Score):** ~0.7974 (Model berhasil mengenali pola tren sensor sebesar 79.74%).
Model yang sudah pintar dikunci dan disimpan menjadi file biner `model_pohon_rf.pkl`.

### Step 6: Inference (`6_inference.py`)
Simulasi penggunaan model pada data pengukuran baru dari taman tanpa melakukan pelatihan ulang. Program mengambil data sensor mentah (Suhu, Kelembapan, MQ-7), melakukan transformasi berdasarkan `scaler.pkl`, lalu memasukkannya ke `model_pohon_rf.pkl` untuk menghasilkan prediksi nilai gas di masa depan secara instan.
