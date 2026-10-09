# ==================================================
# LATIHAN 1: PASANGAN INDEKS
# ==================================================

# LANGKAH 1: Menampilkan judul awal program.
print("=== LATIHAN 1: PASANGAN INDEKS ===")

# LANGKAH 2: Membuat variabel penghitung.
# Variabel count dimulai dari 0 karena belum ada pasangan.
count = 0

# LANGKAH 3: Membuat perulangan luar.
# Variabel i berjalan dari 1 sampai 3.
for i in range(1, 4):

    # LANGKAH 4: Membuat perulangan dalam.
    # Untuk setiap nilai i, variabel j berjalan dari 1 sampai 4.
    for j in range(1, 5):

        # LANGKAH 5: Menampilkan pasangan indeks.
        print(f"Pasangan: ({i}, {j})")

        # LANGKAH 6: Menambah penghitung setiap pasangan ditemukan.
        count += 1

# LANGKAH 7: Menampilkan judul hasil.
print("\n=== HASIL LATIHAN 1 ===")

# LANGKAH 8: Menampilkan jumlah seluruh pasangan.
print(f"Banyak pasangan = {count}")
