def buat_database(filename="data_tugas.txt"):
    try:
        with open(filename, 'x') as f:
            f.write("=== DATABASE TUGAS ===\n")
        print(f"File {filename} berhasil dibuat.")
    except FileExistsError:
        pass 

def simpan_tugas(filename, data_str):
    with open(filename, 'a') as f:
        f.write(data_str + "\n")

def baca_semua(filename="data_tugas.txt"):
    data = []
    try:
        with open(filename, 'r') as f:
            for baris in f:
                if "===" not in baris and baris.strip():
                    data.append(baris.strip())
    except FileNotFoundError:
        print(f"Error: File {filename} belum ada!")
    return data

def cetak_laporan(filename, isi_laporan):
    with open(filename, 'w') as f:
        f.write(isi_laporan)

def cek_duplikat(filename, baris_baru):
    try:
        with open(filename, 'r') as f:
            isi_file = f.read()
            if baris_baru in isi_file:
                return True
    except FileNotFoundError:
        return False
    return False

def hapus_tugas(filename, nama_tugas_hapus):
    try:
        with open(filename, 'r') as f:
            semua_baris = f.readlines()
            
        berhasil_dihapus = False
        
        with open(filename, 'w') as f:
            for baris in semua_baris:
                if not baris.strip():
                    continue
                if baris.startswith(nama_tugas_hapus + ";"):
                    berhasil_dihapus = True 
                else:
                    f.write(baris) 
                    
        return berhasil_dihapus
    except FileNotFoundError:
        print(f"Error: File {filename} tidak ditemukan.")
        return False