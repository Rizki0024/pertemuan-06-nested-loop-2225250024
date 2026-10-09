# ==================================================
# LATIHAN 3: JUMLAH PER BARIS
# ==================================================

# LANGKAH 1: Menampilkan judul awal program.
print("=== LATIHAN 3: JUMLAH PER BARIS ===")

# LANGKAH 2: Membuat perulangan luar untuk menentukan baris.
# Nilai i berjalan dari 1 sampai 4.
for i in range(1, 5):

    # LANGKAH 3: Mengatur ulang jumlah baris menjadi 0.
    # Letaknya di dalam loop luar agar setiap baris dihitung terpisah.
    total_baris = 0

    # LANGKAH 4: Membuat perulangan dalam untuk nilai j dari 1 sampai 3.
    for j in range(1, 4):

        # LANGKAH 5: Menghitung hasil perkalian i dan j.
        hasil = i * j

        # LANGKAH 6: Menambahkan hasil perkalian ke jumlah baris.
        total_baris += hasil

    # LANGKAH 7: Menampilkan jumlah setelah satu baris selesai dihitung.
    print(f"Jumlah baris {i} = {total_baris}")

# LANGKAH 8: Menampilkan judul hasil.
print("\n=== HASIL LATIHAN 3 ===")

# LANGKAH 9: Menampilkan keterangan akhir.
print("Perhitungan jumlah setiap baris telah selesai.")
