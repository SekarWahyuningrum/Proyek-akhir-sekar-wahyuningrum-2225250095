def hitung_rata_rata(data_siswa):
    if not data_siswa:
        return 0

    total = sum(siswa["nilai"] for siswa in data_siswa)
    return total / len(data_siswa)


def cari_nilai_tertinggi(data_siswa):
    if not data_siswa:
        return 0

    return max(siswa["nilai"] for siswa in data_siswa)


def cari_nilai_terendah(data_siswa):
    if not data_siswa:
        return 0

    return min(siswa["nilai"] for siswa in data_siswa)


def hitung_kelulusan(data_siswa, kkm=75):
    lulus = 0
    belum_lulus = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= kkm:
            lulus += 1
        else:
            belum_lulus += 1

    return lulus, belum_lulus