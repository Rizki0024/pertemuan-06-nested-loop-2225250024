# Pertemuan 06 — Nested Loop

## Identitas
- Nama: Rizki Ramadan
- NIM: 2225250024
- Kelas: 3F
- Mata Kuliah: Algoritma dan Pemrograman
- Program Studi: S1 Pendidikan Matematika FKIP UNTIRTA

## Tujuan
Memahami dan menerapkan nested loop, pembentukan pola, akumulasi, pencacahan, tracing, serta pengujian program Python.

## Deskripsi
Nested loop adalah perulangan yang berada di dalam perulangan lain. Pada materi ini, loop luar mengatur kelompok atau baris, sedangkan loop dalam memproses elemen pada setiap baris. Akumulasi digunakan untuk menjumlahkan nilai, sedangkan pencacahan digunakan untuk menghitung banyak kejadian yang memenuhi kondisi.

## Struktur Folder
```text
pertemuan_06_nested_loop/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
├── tugas/
│   └── tabel_perkalian_dan_statistik.py
└── kuis_formatif_pertemuan_6.docx
```

## Cara Menjalankan
Jalankan perintah berikut dari terminal pada folder utama proyek:

```bash
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py
```

Pada sebagian sistem, perintah Python dapat menggunakan `python3` sebagai pengganti `python`.

## Ringkasan Algoritma Latihan
1. **Pasangan indeks:** loop luar mengatur nilai `i`, loop dalam mengatur nilai `j`, dan `count` menghitung jumlah pasangan yang ditampilkan.
2. **Pola segitiga:** loop luar menentukan baris, sedangkan loop dalam mencetak bintang sebanyak nomor baris.
3. **Jumlah per baris:** untuk setiap `i` dari 1 sampai 4, program menjumlahkan `i * j` untuk `j` dari 1 sampai 3.
4. **Menghitung pasangan:** program memeriksa semua pasangan dan menambah `count` jika `i + j <= n`.

## Algoritma Tugas 3
1. Meminta ukuran tabel `n`.
2. Meminta ulang input selama `n <= 0`.
3. Menginisialisasi `total_semua = 0` dan `count_genap = 0` sebelum kedua loop.
4. Mengulang `i` dari 1 sampai `n` sebagai pengatur baris.
5. Menginisialisasi `total_baris = 0` pada awal setiap baris.
6. Mengulang `j` dari 1 sampai `n` sebagai pengatur kolom.
7. Menghitung `hasil = i * j` dan menampilkan hasilnya.
8. Menambahkan hasil ke `total_baris` dan `total_semua`.
9. Jika hasil genap, menambah `count_genap`.
10. Setelah loop dalam selesai, menampilkan jumlah baris.
11. Setelah kedua loop selesai, menampilkan total keseluruhan dan banyak hasil genap.

## Peran Variabel
- `i`: mengatur baris tabel.
- `j`: mengatur kolom tabel.
- `hasil`: menyimpan hasil perkalian `i * j`.
- `total_baris`: menjumlahkan hasil dalam satu baris dan direset pada awal baris berikutnya.
- `total_semua`: menjumlahkan semua hasil perkalian dan tidak direset selama loop berlangsung.
- `count_genap`: menghitung berapa hasil perkalian yang genap.

## Pengujian Tugas 3
Nilai yang diharapkan berdasarkan test case pada modul:

| Input n | Banyak Pasangan | Total Semua | Hasil Genap |
|---------|-----------------|-------------|-------------|
| 1       | 1               | 1           | 0           |
| 2       | 4               | 9           | 3           |
| 3       | 9               | 36          | 5           |

Jalankan program untuk `n = 1`, `n = 2`, dan `n = 3`, lalu cocokkan hasil aktual dengan tabel di atas. Catat hasil aktual setelah pengujian benar-benar dilakukan.

## Analisis Efisiensi
Untuk tabel berukuran `n × n`, loop dalam dijalankan `n` kali untuk setiap dari `n` iterasi loop luar. Dengan demikian, badan loop dalam berjalan sebanyak `n × n = n²` kali. Kompleksitas waktu utamanya adalah **O(n²)**.

## Refleksi
Nested loop dapat digunakan untuk membuat pola, menghasilkan pasangan indeks, dan mengolah data berbentuk tabel. Letak inisialisasi variabel berpengaruh terhadap hasil: `total_baris` perlu direset pada awal setiap baris, sedangkan `total_semua` dan `count_genap` diinisialisasi sebelum kedua loop agar mencakup seluruh tabel. Setelah menjalankan program, tambahkan satu contoh kesalahan yang benar-benar ditemukan beserta cara memperbaikinya.

## Pengumpulan melalui GitHub
Setelah program diuji:
1. Buat repositori bernama `pertemuan-06-nested-loop-NIM` (ganti `NIM` sesuai NIM sendiri).
2. Lakukan commit bertahap yang bermakna, misalnya:
   - `feat: menambahkan latihan nested loop`
   - `feat: menyelesaikan tugas 3 tabel perkalian`
   - `docs: menambahkan hasil pengujian dan refleksi`
3. Lakukan `git push` agar commit tersedia di GitHub.
4. Pastikan repositori berisi README, folder `latihan`, dan folder `tugas`.

## Sumber
Modul perkuliahan Algoritma dan Pemrograman — Pertemuan 06: Nested Loop, Pola, Akumulasi, dan Pencacahan.
OpenAI. (2026). ChatGPT [Alat bantu kecerdasan buatan]. https://chatgpt.com/
Keterangan penggunaan AI: ChatGPT digunakan sebagai alat bantu untuk memahami instruksi tugas, menyusun dan memberikan komentar pada kode Python, serta membantu menyusun dokumentasi README. Kode dan hasil program diperiksa kembali melalui pengujian di VS Code.
