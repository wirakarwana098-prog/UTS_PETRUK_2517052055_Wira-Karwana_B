def buat_database(filename="data_tugas.txt"):
    try:
        # Mode 'x': Membuat file pertama kali
        with open(filename, 'x') as f:
            f.write("=== DATABASE TUGAS ===\n")
        print(f"File {filename} berhasil dibuat.")
    except FileExistsError:
        pass # File sudah ada, lanjutkan saja

def cek_duplikat(filename, baris_baru):
    """Mengecek apakah data_str sudah ada di dalam file database."""
    try:
        with open(filename, 'r') as f:
            isi_file = f.read()
            # Jika baris_baru sudah ada di dalam isi file, kembalikan True
            if baris_baru in isi_file:
                return True
    except FileNotFoundError:
        return False
    return False

def simpan_tugas(filename, data_str):
    # Mode 'a': Menambah data baru ke baris bawah
    with open(filename, 'a') as f:
        f.write(data_str + "\n")

def baca_semua(filename="data_tugas.txt"):
    data = []
    try:
        # Mode 'r': Membaca baris demi baris
        with open(filename, 'r') as f:
            for baris in f:
                if "===" not in baris and baris.strip():
                    data.append(baris.strip())
    except FileNotFoundError:
        print(f"Error: File {filename} belum ada! Sistem gagal membaca.")
    return data

def cetak_laporan(filename, isi_laporan):
    # Mode 'w': Menulis file laporan (menimpa isi lama)
    with open(filename, 'w') as f:
        f.write(isi_laporan)
        