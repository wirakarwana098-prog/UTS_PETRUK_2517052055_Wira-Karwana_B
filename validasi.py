from datetime import datetime

# Membuat exception buatan sendiri (Syarat D: raise)
class PastDateError(Exception):
    pass

def cek_tanggal(tanggal_str):
    """Memvalidasi format tanggal dan memastikan bukan di masa lalu."""
    try: # Syarat D: try/except ValueError
        tgl = datetime.strptime(tanggal_str, "%d/%m/%Y")
        if tgl.date() < datetime.now().date():
            # Syarat D: raise exception buatan sendiri
            raise PastDateError("Tenggat waktu tidak boleh di masa lalu!")
        return tanggal_str
    except ValueError:
        print("Error: Format tanggal salah! Gunakan DD/MM/YYYY.")
        return None
    except PastDateError as e:
        print(f"Error: {e}")
        return None

def cek_prioritas(prio_str):
    """Memastikan tingkat prioritas valid (1-3)."""
    try:
        prio = int(prio_str)
        # Syarat D: Penggunaan assert
        assert 1 <= prio <= 3, "Prioritas harus berkisar antara angka 1 hingga 3."
        return prio
    except ValueError:
        print("Error: Prioritas harus berupa angka!")
        return None
    except AssertionError as e:
        print(f"Error: {e}")
        return None