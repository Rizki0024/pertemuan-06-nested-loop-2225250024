# ==================================================
# LATIHAN 2: POLA SEGITIGA
# ==================================================

# LANGKAH 1: Menampilkan judul awal program.
print("=== LATIHAN 2: POLA SEGITIGA ===")

# LANGKAH 2: Meminta pengguna memasukkan jumlah baris.
n = int(input("Masukkan jumlah baris: "))

# LANGKAH 3: Membuat perulangan luar untuk menentukan baris.
# Nilai i berjalan dari 1 sampai n.
for i in range(1, n + 1):

    # LANGKAH 4: Membuat perulangan dalam untuk mencetak bintang.
    # Banyak bintang pada setiap baris sama dengan nilai i.
    for j in range(i):

        # LANGKAH 5: Mencetak bintang tanpa pindah baris.
        print("*", end=" ")

    # LANGKAH 6: Pindah ke baris berikutnya setelah bintang selesai dicetak.
    print()

# LANGKAH 7: Menampilkan judul hasil.
print("\n=== HASIL LATIHAN 2 ===")

# LANGKAH 8: Menampilkan keterangan bahwa pola telah selesai dibuat.
print(f"Pola segitiga berhasil dibuat dengan {n} baris.")
