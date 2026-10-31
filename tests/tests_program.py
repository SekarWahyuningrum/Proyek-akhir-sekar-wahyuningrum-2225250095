import os
import sys
import tempfile
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from analisis import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_kelulusan
)
from data_io import baca_data
from utilitas import validasi_nilai


class TestProgramAnalisisNilai(unittest.TestCase):

    def test_rata_rata(self):
        data = [
            {"nama": "Ayu", "nilai": 70},
            {"nama": "Budi", "nilai": 80},
            {"nama": "Citra", "nilai": 90}
        ]
        self.assertEqual(hitung_rata_rata(data), 80)

    def test_kelulusan(self):
        data = [
            {"nama": "Ayu", "nilai": 75},
            {"nama": "Budi", "nilai": 74}
        ]
        self.assertEqual(hitung_kelulusan(data, 75), (1, 1))

    def test_nilai_tertinggi(self):
        data = [
            {"nama": "Ayu", "nilai": 85},
            {"nama": "Budi", "nilai": 95}
        ]
        self.assertEqual(cari_nilai_tertinggi(data), 95)

    def test_data_kosong(self):
        self.assertEqual(hitung_rata_rata([]), 0)
        self.assertEqual(cari_nilai_tertinggi([]), 0)
        self.assertEqual(cari_nilai_terendah([]), 0)
        self.assertEqual(hitung_kelulusan([]), (0, 0))

    def test_validasi_nilai(self):
        self.assertTrue(validasi_nilai(100))
        self.assertTrue(validasi_nilai(0))
        self.assertFalse(validasi_nilai(105))
        self.assertFalse(validasi_nilai("abc"))

    def test_file_tidak_ditemukan(self):
        with tempfile.TemporaryDirectory() as folder:
            nama_file = os.path.join(folder, "tidak_ada.txt")
            self.assertEqual(baca_data(nama_file), [])


if __name__ == "__main__":
    unittest.main()