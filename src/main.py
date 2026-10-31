from data_io import baca_data
from analisis import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_kelulusan
)
from utilitas import format_nilai


def main():
    nama_file = "data/nilai_contoh.txt"
    kkm = 75

    data_siswa = baca_data(nama_file)

    if not data_siswa:
        print("Tidak ada data siswa yang dapat dianalisis.")
        return

    rata_rata = hitung_rata_rata(data_siswa)
    tertinggi = cari_nilai_tertinggi(data_siswa)
    terendah = cari_nilai_terendah(data_siswa)
    lulus, belum_lulus = hitung_kelulusan(data_siswa, kkm)

    print("=== REKAP DAN ANALISIS NILAI MATEMATIKA ===")
    print("Jumlah siswa    :", len(data_siswa))
    print("Rata-rata nilai :", format_nilai(rata_rata))
    print("Nilai tertinggi :", format_nilai(tertinggi))
    print("Nilai terendah  :", format_nilai(terendah))
    print("Siswa lulus     :", lulus)
    print("Belum lulus     :", belum_lulus)


if __name__ == "__main__":
    main()