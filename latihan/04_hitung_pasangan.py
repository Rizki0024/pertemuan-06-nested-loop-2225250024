# ==================================================
# LATIHAN 4: MENGHITUNG PASANGAN
# ==================================================

# LANGKAH 1: Menampilkan judul awal program.
print("=== LATIHAN 4: MENGHITUNG PASANGAN ===")

# LANGKAH 2: Meminta pengguna memasukkan nilai n.
n = int(input("Masukkan nilai n: "))

# LANGKAH 3: Menyiapkan penghitung pasangan yang memenuhi syarat.
count = 0

# LANGKAH 4: Membuat perulangan luar untuk nilai i dari 1 sampai n.
for i in range(1, n + 1):

    # LANGKAH 5: Membuat perulangan dalam untuk nilai j dari 1 sampai n.
    for j in range(1, n + 1):

        # LANGKAH 6: Memeriksa apakah jumlah i dan j tidak melebihi n.
        if i + j <= n:

            # LANGKAH 7: Menambah penghitung jika syarat terpenuhi.
            count += 1

# LANGKAH 8: Menampilkan judul hasil.
print("\n=== HASIL LATIHAN 4 ===")

# LANGKAH 9: Menampilkan jumlah pasangan yang memenuhi syarat.
print(f"Banyak pasangan yang memenuhi i + j <= {n} adalah {count}")
