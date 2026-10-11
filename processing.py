from datetime import datetime

class Tugas:
    # Penggunaan **kwargs untuk atribut bervariasi
    def __init__(self, nama, matkul, tanggal, prioritas, **kwargs):
        self.nama = nama
        self.matkul = matkul
        self.tanggal = tanggal
        self.prioritas = prioritas
        self.detail = kwargs 
        self.status = "Belum Selesai"

    def ubah_status(self, status_baru):
        self.status = status_baru

class ManajerTugas:
    def __init__(self):
        self.daftar_tugas = []

    def tambah_objek(self, objek_tugas):
        self.daftar_tugas.append(objek_tugas)

    def urutkan_prioritas(self):
        # Penggunaan lambda sebagai key pada fungsi sorted()
        self.daftar_tugas.sort(key=lambda t: t.prioritas)
        return self.daftar_tugas

    def hitung_sisa_hari(self, *args):
        # Penggunaan *args untuk memproses banyak tanggal sekaligus
        sisa_waktu = []
        hari_ini = datetime.now()
        for tgl_str in args:
            tgl_tujuan = datetime.strptime(tgl_str, "%d/%m/%Y")
            selisih = (tgl_tujuan - hari_ini).days
            sisa_waktu.append(max(0, selisih))
        return sisa_waktu