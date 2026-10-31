def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                bagian = baris.strip().split(",")

                if len(bagian) != 2:
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    continue

                if nama and 0 <= nilai <= 100:
                    data_siswa.append({
                        "nama": nama,
                        "nilai": nilai
                    })

        return data_siswa

    except FileNotFoundError:
        print("File data tidak ditemukan.")
        return []