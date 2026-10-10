import unittest
import validasi
from processing import ManajerTugas, Tugas

class TestToDoList(unittest.TestCase):
    
    def test_tanggal_valid(self):
        # Pengujian 1: Format tanggal benar
        hasil = validasi.cek_tanggal("30/12/2026")
        self.assertEqual(hasil, "30/12/2026")

    def test_tanggal_salah(self):
        # Pengujian 2: Format salah memicu blok except
        hasil = validasi.cek_tanggal("30-Desember")
        self.assertIsNone(hasil)

    def test_prioritas_valid(self):
        # Pengujian 3: Prioritas di batas 1-3
        hasil = validasi.cek_prioritas("2")
        self.assertEqual(hasil, 2)

    def test_prioritas_invalid(self):
        # Pengujian 4: Prioritas di luar batas memicu AssertionError
        hasil = validasi.cek_prioritas("5")
        self.assertIsNone(hasil)

    def test_hitung_sisa_hari(self):
        # Pengujian 5: Fungsi *args mengembalikan list yang tepat
        manajer = ManajerTugas()
        # Menggunakan tanggal jauh di masa depan agar tidak minus
        hasil = manajer.hitung_sisa_hari("01/01/2030", "01/01/2031")
        self.assertEqual(len(hasil), 2)
        self.assertGreater(hasil[0], 0)

if __name__ == '__main__':
    unittest.main()