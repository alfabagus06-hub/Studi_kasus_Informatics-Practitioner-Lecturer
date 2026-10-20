
from multiprocessing import Pool, cpu_count
from time import perf_counter


def hitung_kuadrat(rentang):
    awal, akhir = rentang
    return sum(i * i for i in range(awal, akhir))


def proses_serial(jumlah):
    return hitung_kuadrat((0, jumlah))


def proses_paralel(jumlah, jumlah_proses):
    ukuran = (jumlah + jumlah_proses - 1) // jumlah_proses
    bagian = [
        (awal, min(awal + ukuran, jumlah))
        for awal in range(0, jumlah, ukuran)
    ]

    with Pool(processes=jumlah_proses) as pool:
        hasil = pool.map(hitung_kuadrat, bagian)

    return sum(hasil)


if __name__ == "__main__":
    jumlah = 1_000_000
    jumlah_proses = max(2, min(cpu_count(), 4))

    mulai = perf_counter()
    hasil_serial = proses_serial(jumlah)
    waktu_serial = perf_counter() - mulai

    mulai = perf_counter()
    hasil_paralel = proses_paralel(jumlah, jumlah_proses)
    waktu_paralel = perf_counter() - mulai

    print("PERBANDINGAN PEMROSESAN SERIAL DAN PARALEL")
    print(f"Jumlah data: {jumlah:,}")
    print(f"Hasil serial: {hasil_serial:,}")
    print(f"Waktu serial: {waktu_serial:.4f} detik")
    print(f"Hasil paralel: {hasil_paralel:,}")
    print(f"Waktu paralel: {waktu_paralel:.4f} detik")
    print(f"Jumlah proses: {jumlah_proses}")
    print(f"Hasil perhitungan sama: {hasil_serial == hasil_paralel}")

    if waktu_paralel > 0:
        print(f"Speedup: {waktu_serial / waktu_paralel:.2f}x")
