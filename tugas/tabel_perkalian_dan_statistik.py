# ==========================================================
# TUGAS 3: TABEL PERKALIAN DAN STATISTIK
# ==========================================================

# LANGKAH 1: Menampilkan judul awal program.
print("=== TUGAS 3: TABEL PERKALIAN DAN STATISTIK ===")

# LANGKAH 2: Meminta pengguna memasukkan ukuran tabel.
n = int(input("Masukkan ukuran tabel (bilangan positif): "))

# LANGKAH 3: Memvalidasi input.
# Jika n kurang dari atau sama dengan 0, input diminta kembali.
while n <= 0:
    print("Input tidak valid. n harus berupa bilangan positif.")
    n = int(input("Masukkan ukuran tabel (bilangan positif): "))

# LANGKAH 4: Menyiapkan akumulator total keseluruhan.
# Variabel ini tidak direset setiap pergantian baris.
total_semua = 0

# LANGKAH 5: Menyiapkan counter hasil perkalian genap.
# Nilai awal 0 karena belum ada hasil yang diperiksa.
count_genap = 0

# LANGKAH 6: Menampilkan judul bagian tabel.
print("\n=== TABEL PERKALIAN ===")

# LANGKAH 7: Membuat perulangan luar untuk menentukan baris.
for i in range(1, n + 1):

    # LANGKAH 8: Mengatur jumlah baris menjadi 0.
    # Akumulator ini direset setiap memulai baris baru.
    total_baris = 0

    # LANGKAH 9: Membuat perulangan dalam untuk menentukan kolom.
    for j in range(1, n + 1):

        # LANGKAH 10: Menghitung hasil perkalian pada setiap pasangan.
        hasil = i * j

        # LANGKAH 11: Menampilkan hasil secara teratur.
        print(f"{hasil:4}", end="")

        # LANGKAH 12: Menambahkan hasil ke jumlah baris.
        total_baris += hasil

        # LANGKAH 13: Menambahkan hasil ke jumlah keseluruhan.
        total_semua += hasil

        # LANGKAH 14: Memeriksa apakah hasil perkalian genap.
        if hasil % 2 == 0:

            # LANGKAH 15: Menambah counter jika hasil genap.
            count_genap += 1

    # LANGKAH 16: Menampilkan jumlah setelah satu baris selesai.
    print(f"   | Jumlah baris = {total_baris}")

# LANGKAH 17: Menampilkan judul hasil akhir.
print("\n=== HASIL STATISTIK TABEL ===")

# LANGKAH 18: Menampilkan jumlah seluruh hasil perkalian.
print(f"Jumlah seluruh hasil perkalian = {total_semua}")

# LANGKAH 19: Menampilkan banyak hasil perkalian yang genap.
print(f"Banyak hasil perkalian genap = {count_genap}")
