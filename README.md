
# Heart Failure Prediction App

Aplikasi **Prediksi Kematian Jantung** ini dibangun menggunakan Python dan **PySimpleGUI**, dan memprediksi kemungkinan kematian akibat gagal jantung berdasarkan input yang diberikan. Aplikasi ini menggunakan model **Logistic Regression** yang telah dilatih sebelumnya untuk memberikan prediksi.

## Fitur Aplikasi

- **Input Data Pengguna**: Pengguna dapat memasukkan informasi seperti umur, kadar creatinine phosphokinase, ejection fraction, jumlah trombosit, kadar serum creatinine, serum sodium, dan kebiasaan merokok.
- **Prediksi Kematian Jantung**: Setelah memasukkan data, aplikasi akan memberikan hasil prediksi apakah pengguna kemungkinan mengalami kematian jantung atau tidak.
- **Antarmuka yang Mudah Digunakan**: Dibangun dengan menggunakan **PySimpleGUI**, antarmuka aplikasi ini sederhana dan intuitif.

## Persyaratan

Untuk menjalankan aplikasi ini, Anda memerlukan:

- **Python 3.x**
- **PySimpleGUI**: Framework yang digunakan untuk membuat GUI aplikasi.
- **Pandas**: Untuk manipulasi data tabular.
- **Joblib**: Untuk memuat model machine learning yang sudah disimpan.

### Instalasi PySimpleGUI

Anda bisa menginstal PySimpleGUI menggunakan pip:

```bash
pip install pysimplegui
```

### Instalasi Dependensi Lainnya

Instal dependensi lainnya dengan:

```bash
pip install pandas joblib
```

## Menjalankan Aplikasi

1. Clone repositori ini ke lokal Anda:

```bash
git clone https://github.com/username/heart-failure-prediction-app.git
```

2. Pastikan Anda memiliki file **logistic_model_Heart_failure.pkl** di direktori utama. Ini adalah file model Logistic Regression yang telah dilatih. Anda bisa melatih model sendiri atau menggunakan model yang sudah ada.

3. Jalankan aplikasi dengan perintah:

```bash
python logistic_model_heart_failure_app.py
```

## Cara Menggunakan

1. Buka aplikasi.
2. Masukkan data pengguna di bidang yang tersedia:
   - **Umur**: Umur pengguna (misalnya 60.0).
   - **Creatinine Phosphokinase**: Tingkat creatinine phosphokinase dalam mcg/L (misalnya 582.0).
   - **Ejection Fraction**: Persentase ejeksi fraksi jantung (misalnya 35.0).
   - **Platelets**: Jumlah trombosit dalam kiloplatelets/mL (misalnya 263.0).
   - **Serum Creatinine**: Kadar serum creatinine dalam mg/dL (misalnya 1.1).
   - **Serum Sodium**: Kadar serum sodium dalam mEq/L (misalnya 137.0).
   - **Waktu Tindak Lanjut**: Jumlah hari tindak lanjut pengobatan (misalnya 45).
   - **Anemia**: Apakah pengguna mengalami anemia (Ya/Tidak).
   - **Diabetes**: Apakah pengguna memiliki diabetes (Ya/Tidak).
   - **Hipertensi**: Apakah pengguna memiliki riwayat hipertensi (Ya/Tidak).
   - **Jenis Kelamin**: Laki-laki atau Perempuan.
   - **Status Merokok**: Apakah pengguna merokok atau tidak merokok.
3. Klik tombol **Prediksi** untuk melihat hasil prediksi.
4. Hasil prediksi akan ditampilkan di bagian bawah aplikasi.

## Model Machine Learning

Model machine learning yang digunakan adalah **Logistic Regression** yang telah dilatih untuk memprediksi kemungkinan kematian jantung berdasarkan data dari pengguna. Model ini menggunakan fitur-fitur berikut:
- **Umur**
- **Creatinine Phosphokinase**
- **Ejection Fraction**
- **Jumlah Trombosit**
- **Serum Creatinine**
- **Serum Sodium**
- **Waktu Tindak Lanjut**
- **Anemia**
- **Diabetes**
- **Hipertensi**
- **Jenis Kelamin**
- **Status Merokok**
