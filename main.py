import fileio
import validasi
from processing import Tugas, ManajerTugas

def main():
    fileio.buat_database()

    print("\n" + "="*40)
    print("  APLIKASI TO-DO LIST KULIAH ")
    print("="*40)
    
    while True:
        print("\n--- MENU UTAMA ---")
        print("1. Tambah Tugas Baru")
        print("2. Cetak dan Tampilkan Laporan")
        print("3. Hapus Tugas")
        print("4. Keluar dari Program")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            print("\n--- INPUT TUGAS ---")
            nama = input("Nama Tugas   : ")
            matkul = input("Mata Kuliah  : ")
            
            tgl_valid = None
            while not tgl_valid:
                tgl_input = input("DEADLINE (Format DD/MM/YYYY): ")
                tgl_valid = validasi.cek_tanggal(tgl_input)
            
            prio_valid = None
            while not prio_valid:
                prio_input = input("Tingkat Prioritas (1-3): ")
                prio_valid = validasi.cek_prioritas(prio_input)
            
            tipe_input = input("Tipe Tugas (Individu/Kelompok): ")
            
            data_simpan = f"{nama};{matkul};{tgl_valid};{prio_valid}"
            
            if fileio.cek_duplikat("data_tugas.txt", data_simpan):
                print(f"GAGAL: Tugas '{nama}' sudah ada di database.")
            else:
                fileio.simpan_tugas("data_tugas.txt", data_simpan)
                print(f"BERHASIL: Tugas '{nama}' berhasil ditambahkan ke database!")

        elif pilihan == '2':
            manajer = ManajerTugas()
            data_mentah = fileio.baca_semua("data_tugas.txt")
            
            if not data_mentah:
                print("\nBelum ada data tugas yang tersimpan di database.")
                continue
            
            for baris in data_mentah:
                bagian = baris.split(";")
                if len(bagian) >= 4:
                    tgs = Tugas(nama=bagian[0], matkul=bagian[1], 
                                tanggal=bagian[2], prioritas=int(bagian[3]))
                    manajer.tambah_objek(tgs)
            
            urut = manajer.urutkan_prioritas()
            sisa = manajer.hitung_sisa_hari(*[t.tanggal for t in urut])

            laporan = "=== LAPORAN TUGAS ===\n"
            for i, t in enumerate(urut):
                laporan += f"- [{t.prioritas}] {t.nama} ({t.matkul}). Sisa: {sisa[i]} hari.\n"
                
            print("\n" + laporan)
            fileio.cetak_laporan("laporan_tugas.txt", laporan)
            print("(Salinan laporan telah berhasil dicetak ke file laporan_tugas.txt)")

        elif pilihan == '3':
            print("\n--- HAPUS TUGAS ---")
            data_sementara = fileio.baca_semua("data_tugas.txt")
            if not data_sementara:
                print("Database kosong, tidak ada tugas yang bisa dihapus.")
                continue
                
            print("Tugas yang ada saat ini:")
            for baris in data_sementara:
                bagian = baris.split(';')
                print(f"- {bagian[0]} ({bagian[1]})")

            nama_hapus = input("\nMasukkan Nama Tugas yang ingin dihapus (harus persis): ")
            matkul_hapus = input("Masukkan Mata Kuliah tugas tersebut (harus persis): ")

            is_terhapus = fileio.hapus_tugas("data_tugas.txt", nama_hapus, matkul_hapus)

            if is_terhapus:
                print(f"BERHASIL: Tugas '{nama_hapus}' ({matkul_hapus}) berhasil dihapus dari database!")
            else:
                print(f"GAGAL: Tugas '{nama_hapus}' ({matkul_hapus}) tidak ditemukan.")

        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan aplikasi ini. KERJAIN!")
            break
        
        else:
            print("\nERROR: Input tidak valid. Silakan ketik angka 1, 2, 3, atau 4.")

if __name__ == '__main__':
    main()