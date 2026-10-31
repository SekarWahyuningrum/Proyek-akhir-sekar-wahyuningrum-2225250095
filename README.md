<<<<<<< HEAD
# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Identitas Proyek

- Nama: Sekar Wahyuningrum
- NIM: 2225250095
- Program Studi: S1 Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman
- Pertemuan: 15
- Tahun Ajaran: 2026/2027 Ganjil

## 2. Deskripsi Proyek

Proyek ini merupakan rancangan program sederhana menggunakan Python untuk membantu proses rekap dan analisis nilai matematika siswa. Program direncanakan dapat membaca data nilai, memvalidasi nilai, menghitung statistik sederhana, menentukan status ketuntasan, dan menyimpan hasil analisis ke dalam file laporan.

## 3. Tujuan Proyek

1. Menghitung rata-rata nilai siswa.
2. Menentukan nilai tertinggi dan nilai terendah.
3. Menghitung jumlah siswa yang tuntas dan belum tuntas.
4. Menyimpan hasil analisis ke dalam file laporan.

## 4. Struktur Folder

```text
proyek-akhir-sekar/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## 5. Teknologi yang Digunakan

- Bahasa pemrograman Python.
- Visual Studio Code sebagai editor kode.
- Git dan GitHub untuk pengelolaan versi dan penyimpanan proyek.

## 6. Status Proyek

Saat ini proyek berada pada tahap perancangan. Implementasi program, pengujian, dan dokumentasi hasil akan dilanjutkan pada tahap berikutnya.

## 7. Repository GitHub

Tautan repository: Diisi setelah repository dibuat.
=======
# Program Rekap dan Analisis Nilai Matematika Kelas Menggunakan Python

## 1. Identitas Pengembang

- **Nama:** Sekar Wahyuningrum
- **NIM:** 2225250095
- **Program Studi:** S1 Pendidikan Matematika
- **Fakultas:** FKIP
- **Universitas:** Universitas Sultan Ageng Tirtayasa
- **Mata Kuliah:** Algoritma dan Pemrograman

## 2. Deskripsi Program

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program sederhana menggunakan Python untuk mengolah nilai siswa. Program ini membaca data siswa dari file teks, kemudian menghitung jumlah siswa, rata-rata nilai, nilai tertinggi, nilai terendah, serta jumlah siswa yang lulus dan belum lulus berdasarkan Kriteria Ketuntasan Minimal (KKM).

## 3. Tujuan Program

1. Menerapkan dasar pemrograman Python.
2. Mengolah data nilai siswa secara otomatis.
3. Menghitung statistik sederhana dari nilai siswa.
4. Menentukan jumlah siswa yang lulus dan belum lulus.
5. Menerapkan pembagian program ke dalam beberapa fungsi dan modul.
6. Melakukan pengujian untuk memastikan fungsi program berjalan sesuai harapan.

## 4. Struktur Folder

```text
Proyek-akhir-sekar-2225250095/
├── README.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_program.py
│   └── test_case.md
└── output/
    └── .gitkeep
```

## 5. Fungsi Setiap Berkas

- `README.md`: Berisi dokumentasi proyek.
- `.gitignore`: Menentukan berkas yang tidak perlu dimasukkan ke Git.
- `data/nilai_contoh.txt`: Menyimpan data nama dan nilai siswa.
- `src/main.py`: Menjalankan program utama dan menampilkan hasil analisis.
- `src/data_io.py`: Membaca data siswa dari file teks.
- `src/analisis.py`: Menghitung rata-rata, nilai tertinggi, nilai terendah, dan kelulusan.
- `src/utilitas.py`: Menyediakan fungsi validasi dan format nilai.
- `tests/test_program.py`: Berisi kode pengujian otomatis.
- `tests/test_case.md`: Mendokumentasikan kasus dan hasil pengujian.
- `output/`: Disiapkan untuk menyimpan hasil keluaran program.

## 6. Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer.

Buka terminal VS Code pada folder utama proyek, kemudian jalankan perintah berikut:

```bash
python src/main.py
```

## 7. Hasil Pengujian Program Utama

Program dijalankan menggunakan perintah `python src/main.py` dengan hasil berikut:

```text
=== REKAP DAN ANALISIS NILAI MATEMATIKA ===
Jumlah siswa    : 8
Rata-rata nilai : 79.75
Nilai tertinggi : 95.00
Nilai terendah  : 65.00
Siswa lulus     : 6
Belum lulus     : 2
```

Berdasarkan hasil tersebut, program berhasil membaca dan menganalisis 8 data siswa. Rata-rata nilai yang diperoleh adalah 79,75, dengan nilai tertinggi 95 dan nilai terendah 65. Sebanyak 6 siswa dinyatakan lulus dan 2 siswa belum lulus dengan KKM 75.

## 8. Pengujian Otomatis

Pengujian otomatis dilakukan menggunakan modul `unittest` bawaan Python.

Perintah untuk menjalankan pengujian:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Hasil pengujian:

```text
Ran 6 tests in 0.010s

OK
```

Enam pengujian berhasil dijalankan, meliputi perhitungan rata-rata, kelulusan, nilai tertinggi, data kosong, validasi nilai, dan penanganan file yang tidak ditemukan.

## 9. Kesimpulan Pengujian

Berdasarkan hasil pengujian, program utama berhasil dijalankan dan seluruh enam pengujian otomatis dinyatakan berhasil. Program dapat melakukan perhitungan statistik nilai siswa dan menentukan kelulusan berdasarkan KKM yang ditetapkan. Pengujian ini menunjukkan bahwa fungsi-fungsi yang diuji bekerja sesuai hasil yang diharapkan.

## 10. Refleksi

Melalui proyek ini, saya mempelajari cara mengolah data menggunakan Python, membagi program menjadi beberapa modul, membuat fungsi, membaca data dari file teks, serta melakukan pengujian otomatis menggunakan `unittest`. Saya juga belajar bahwa pengujian penting untuk memeriksa apakah program berjalan sesuai harapan dan membantu menemukan kesalahan.

## 11. Pengembangan Selanjutnya

Program ini dapat dikembangkan dengan menambahkan fitur memasukkan data siswa secara langsung, menyimpan hasil analisis ke file, menampilkan daftar siswa yang belum lulus, dan membuat visualisasi hasil nilai siswa.
>>>>>>> da55b17 (Menyelesaikan proyek akhir Pertemuan 15)
