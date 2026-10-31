# PROPOSAL PROYEK PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas Menggunakan Python.

## 2. Latar Belakang

Dalam kegiatan pembelajaran matematika, guru perlu mengolah nilai siswa untuk mengetahui hasil belajar dan tingkat ketuntasan siswa. Jika pengolahan nilai dilakukan secara manual, prosesnya dapat membutuhkan waktu dan berisiko terjadi kesalahan perhitungan.

Oleh karena itu, dirancang sebuah program sederhana menggunakan bahasa pemrograman Python untuk membantu proses rekap dan analisis nilai matematika siswa. Program ini direncanakan dapat membaca data nilai, memeriksa validitas nilai, menghitung statistik sederhana, menentukan status ketuntasan, serta menyimpan hasil analisis ke dalam file.

## 3. Pengguna dan Tujuan

### Pengguna
Guru matematika yang membutuhkan bantuan dalam mengolah nilai siswa.

### Tujuan
1. Membantu menghitung rata-rata nilai siswa.
2. Menentukan nilai tertinggi dan nilai terendah.
3. Menghitung jumlah siswa yang tuntas dan belum tuntas.
4. Menyimpan hasil analisis nilai ke dalam file laporan.

## 4. Ruang Lingkup

Program dirancang untuk dijalankan melalui terminal atau console di Visual Studio Code menggunakan Python.

Fitur yang direncanakan:
1. Membaca data nilai siswa dari file.
2. Memvalidasi nilai dalam rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM).
5. Menyimpan hasil analisis ke dalam file laporan.

Program ini dibatasi pada pengolahan data nilai sederhana dan tidak menggunakan antarmuka grafis atau aplikasi berbasis web.

## 5. Kebutuhan Program

### Kebutuhan Fungsional
- Program dapat membaca data nilai siswa dari file.
- Program dapat memvalidasi nilai dalam rentang 0–100.
- Program dapat menghitung rata-rata, nilai minimum, dan nilai maksimum.
- Program dapat menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
- Program dapat menyimpan hasil analisis ke dalam file laporan.

### Kebutuhan Nonfungsional
- Program dapat dijalankan melalui terminal VS Code.
- Program menggunakan nama variabel dan fungsi yang mudah dipahami.
- Program menampilkan pesan kesalahan yang jelas.
- Program dapat diuji menggunakan data contoh.

## 6. Input, Proses, dan Output (IPO)

### Input
Data nama siswa dan nilai matematika yang disimpan dalam file.

### Proses
1. Membaca data nilai siswa.
2. Memeriksa format dan rentang nilai.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status ketuntasan berdasarkan KKM.
5. Menyusun laporan hasil analisis.

### Output
Ringkasan statistik nilai siswa, jumlah siswa yang tuntas dan belum tuntas, serta file laporan hasil analisis.

## 7. Algoritma

MULAI

1. Membaca data nilai siswa dari file.
2. Memeriksa apakah file tersedia.
3. Memvalidasi data dan rentang nilai.
4. Menyimpan data yang valid.
5. Memeriksa apakah terdapat data valid.
6. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
7. Menentukan status ketuntasan siswa berdasarkan KKM.
8. Menampilkan ringkasan hasil analisis.
9. Menyimpan hasil analisis ke dalam file laporan.

SELESAI

## 8. Struktur Program

Program dirancang menggunakan beberapa file Python dengan fungsi yang berbeda.

- `main.py`: mengatur jalannya program.
- `data_io.py`: membaca data nilai dan menyimpan laporan.
- `analisis.py`: menghitung statistik dan menentukan status ketuntasan.
- `utilitas.py`: menyediakan fungsi bantuan untuk program.

## 9. Struktur Data

Struktur data yang direncanakan meliputi:

- **List**, untuk menyimpan kumpulan nilai siswa.
- **Dictionary**, untuk menyimpan data siswa beserta atributnya.
- **String**, untuk menyusun teks laporan.
- **File teks**, untuk menyimpan data masukan dan hasil laporan.

## 10. Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Nilai diterima sebagai data valid |
| TC03 | Batas | Nilai 100 | Nilai diterima sebagai data valid |
| TC04 | Invalid | Nilai 105 | Nilai ditolak dengan pesan validasi |
| TC05 | Invalid | File data tidak ditemukan | Program menampilkan pesan kesalahan yang sesuai |

## 11. Pembagian Tugas

Proyek ini dikerjakan secara individu. Seluruh tahapan, mulai dari perancangan, penyusunan algoritma, pemrograman, pengujian, hingga dokumentasi, menjadi tanggung jawab penyusun.

## 12. Jadwal Pengerjaan

- Pertemuan 14: menyusun proposal, algoritma, struktur program, dan test case.
- Antara Pertemuan 14 dan 15: mulai membuat program Python berdasarkan rancangan.
- Pertemuan 15: melanjutkan implementasi, pengujian, debugging, dan dokumentasi.
- Pertemuan 16: mempersiapkan presentasi dan demonstrasi program.

## 13. Repository GitHub

Repository GitHub akan digunakan untuk menyimpan proposal, dokumentasi, kode program, dan test case.

Tautan repository: Diisi setelah repository GitHub dibuat.
