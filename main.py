import fileio
import validasi
from processing import Tugas, ManajerTugas

def main():
    fileio.buat_database()
    manajer = ManajerTugas()

    print("\n--- TUGAS KULIAH YA AMPUN ---")
    
    # Input Data & Validasi
    tgl_valid = validasi.cek_tanggal("10/10/2026")
    prio_valid = validasi.cek_prioritas("1")
    
    if tgl_valid and prio_valid:
        # Keyword argument saat pemanggilan fungsi
        tugas1 = Tugas(nama="UTS", matkul="PETRUK", 
                       tanggal=tgl_valid, prioritas=prio_valid, 
                       dosen="Pak Rahman", tipe="Individu") # **kwargs terisi disini
        
        manajer.tambah_objek(tugas1)
        
        # hasil akan dsimpan disini
        data_simpan = f"{tugas1.nama};{tugas1.matkul};{tugas1.tanggal};{tugas1.prioritas}"
        
        # Mengecek apakah tugas ini sudah pernah diinput sebelumnya
        is_duplikat = fileio.cek_duplikat("data_tugas.txt", data_simpan)
        if is_duplikat:
            print(f"Peringatan: Tugas '{tugas1.nama}' sudah ada di database. Batal menyimpan.")
        else:
            fileio.simpan_tugas("data_tugas.txt", data_simpan)
            print("Tugas berhasil ditambahkan ke database!")

    # Proses Hitung Sisa Hari (Pakai *args)
    tanggal_kumpul = [t.tanggal for t in manajer.daftar_tugas]
    sisa = manajer.hitung_sisa_hari(*tanggal_kumpul)
    
    # Cetak Laporan (Mode W)
    laporan = "--- LAPORAN TUGAS ---\n"
    for i, t in enumerate(manajer.urutkan_prioritas()):
        laporan += f"- {t.nama} (Prioritas {t.prioritas}). Sisa waktu: {sisa[i]} hari.\n"
        laporan += f"  Detail: {t.detail}\n"
        
    fileio.cetak_laporan("laporan_tugas.txt", laporan)
    print("\nLaporan berhasil dicetak ke laporan_tugas.txt")

# Blok pengujian lokal
if __name__ == '__main__':
    main()