# Perbandingan Pemrosesan Serial dan Paralel

## Deskripsi Studi Kasus
Proyek ini membahas perbandingan pemrosesan serial dan paralel dalam menyelesaikan perhitungan dengan jumlah data yang besar. Studi kasus ini disusun berdasarkan materi High Performance Computing (HPC), yang membahas pemanfaatan komputasi untuk menyelesaikan permasalahan yang membutuhkan sumber daya komputasi.

Dalam implementasi ini, operasi perhitungan yang sama dijalankan menggunakan dua pendekatan, yaitu serial dan paralel. Waktu eksekusi kedua pendekatan kemudian dibandingkan untuk melihat perbedaan kinerjanya.

## Tujuan
- Memahami konsep dasar pemrosesan serial dan paralel.
- Membandingkan waktu eksekusi dari kedua metode.
- Mengetahui pengaruh pembagian pekerjaan terhadap waktu komputasi.
- Memahami bahwa pemrosesan paralel tidak selalu lebih cepat karena adanya overhead dan keterbatasan perangkat keras.

## Metode yang Digunakan
**Pemrosesan serial:** pekerjaan dijalankan secara berurutan dalam satu proses.

**Pemrosesan paralel:** pekerjaan dibagi menjadi beberapa bagian yang diproses oleh beberapa proses secara bersamaan.

Kedua metode menggunakan jenis perhitungan yang sama agar hasil dan waktu eksekusinya dapat dibandingkan secara lebih adil.

## Teknologi yang Digunakan
- Python
- `multiprocessing`
- `time`

## Implementasi
Program menjalankan perhitungan menggunakan metode serial dan paralel, mencatat waktu yang dibutuhkan, kemudian menampilkan hasil perbandingan. Hasil pengujian dapat berbeda bergantung pada jumlah data, jumlah proses, serta spesifikasi komputer yang digunakan.

## Cara Menjalankan
Pastikan Python sudah terpasang di komputer. Tidak diperlukan pustaka tambahan karena modul yang digunakan tersedia dalam pustaka standar Python.

Jalankan program melalui terminal:

```bash
python app.py
```

## Output yang Diharapkan
Program menampilkan hasil perhitungan serta waktu eksekusi pemrosesan serial dan paralel. Informasi tersebut digunakan untuk membandingkan kinerja kedua metode pada pengujian yang dilakukan.

## Kesimpulan
Studi kasus ini memperlihatkan konsep dasar High Performance Computing melalui perbandingan dua pendekatan pemrosesan. Hasil pengujian membantu memahami bahwa efektivitas pemrosesan paralel bergantung pada karakteristik pekerjaan dan sumber daya komputer.

Catatan: waktu eksekusi perlu diukur langsung saat program dijalankan. Kesimpulan mengenai metode yang lebih cepat tidak ditentukan sebelum pengujian dilakukan.
