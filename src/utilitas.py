def validasi_nilai(nilai):
    try:
        nilai = float(nilai)
        return 0 <= nilai <= 100
    except (ValueError, TypeError):
        return False


def format_nilai(nilai):
    return "{:.2f}".format(nilai)