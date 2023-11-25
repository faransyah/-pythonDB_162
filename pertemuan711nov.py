import tkinter as tk
import sqlite3

def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()
    # Mendapatkan nilai dari 10 mata pelajaran (3 yang sudah ada + 10 tambahan)
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_mtkpeminatan = float(entry_mtkpeminatan.get())
    nilai_mtk = float(entry_mtk.get())
    nilai_kimia = float(entry_kimia.get())
    nilai_ekonomi = float(entry_ekonomi.get())
    nilai_geografi = float(entry_geografi.get())
    nilai_seni = float(entry_seni.get())
    nilai_olahraga = float(entry_olahraga.get())
    nilai_pai = float(entry_pai.get())

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    # Membandingkan nilai dari 13 mata pelajaran
    nilai_tinggi = max(nilai_biologi, nilai_fisika, nilai_mtkpeminatan, nilai_mtk, nilai_kimia,
                       nilai_ekonomi, nilai_geografi, nilai_seni, nilai_olahraga,
                       nilai_pai)

    if nilai_tinggi == nilai_biologi:
        hasil_prodi = "Kedokteran"
    elif nilai_tinggi == nilai_fisika:
        hasil_prodi = "Fisika murni"
    elif nilai_tinggi == nilai_mtkpeminatan:
        hasil_prodi = "Matematika Murni"
    elif nilai_tinggi == nilai_mtk:
        hasil_prodi = "Teknik Informatika"
    elif nilai_tinggi == nilai_kimia:
        hasil_prodi = "Teknik Kimia"
    elif nilai_tinggi == nilai_ekonomi:
        hasil_prodi = "Ekonomi"
    elif nilai_tinggi == nilai_geografi:
        hasil_prodi = "Fisipol"
    elif nilai_tinggi == nilai_seni:
        hasil_prodi = "Ilmu Budaya"
    elif nilai_tinggi == nilai_olahraga:
        hasil_prodi = "Keolahragaan"
    elif nilai_tinggi == nilai_pai:
        hasil_prodi = "Teknik Informatika"
    else:
        hasil_prodi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_prodi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('data_nilai_siswa.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        mtkpeminatan REAL,
                        mtk REAL,
                        kimia REAL,
                        ekonomi REAL,
                        geografi REAL,
                        seni REAL,
                        olahraga REAL,
                        pai REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, mtkpeminatan, mtk,
                    kimia, ekonomi, geografi, seni, olahraga, pai, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nama, nilai_biologi, nilai_fisika, nilai_mtkpeminatan, nilai_mtk, nilai_kimia,
                    nilai_ekonomi, nilai_geografi, nilai_seni, nilai_olahraga,
                    nilai_pai, hasil_prodi))
    conn.commit()
    conn.close()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")  # Mengatur ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat 10 label dan entry baru untuk 10 mata pelajaran tambahan
label_biologi = tk.Label(root, text="Nilai Biologi: ")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika: ")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_mtkpeminatan = tk.Label(root, text="Nilai Matematika Peminatan: ")
label_mtkpeminatan.pack()
entry_mtkpeminatan = tk.Entry(root)
entry_mtkpeminatan.pack()

label_mtk = tk.Label(root, text="Nilai Matematika: ")
label_mtk.pack()
entry_mtk = tk.Entry(root)
entry_mtk.pack()

label_kimia = tk.Label(root, text="Nilai Kimia: ")
label_kimia.pack()
entry_kimia = tk.Entry(root)
entry_kimia.pack()

label_ekonomi = tk.Label(root, text="Nilai Ekonomi: ")
label_ekonomi.pack()
entry_ekonomi = tk.Entry(root)
entry_ekonomi.pack()

label_geografi = tk.Label(root, text="Nilai Geografi: ")
label_geografi.pack()
entry_geografi = tk.Entry(root)
entry_geografi.pack()

label_seni = tk.Label(root, text="Nilai Seni: ")
label_seni.pack()
entry_seni = tk.Entry(root)
entry_seni.pack()

label_olahraga = tk.Label(root, text="Nilai Olahraga: ")
label_olahraga.pack()
entry_olahraga = tk.Entry(root)
entry_olahraga.pack()

label_pai = tk.Label(root, text="Nilai Pendidikan Agama Islam: ")
label_pai.pack()
entry_pai = tk.Entry(root)
entry_pai.pack()

# Button untuk melakukan prediksi
button_prediksi = tk.Button(root, text="Prediksi", command=hasil_prediksi)
button_prediksi.pack(pady=10)

# Label untuk menampilkan hasil prediksi
hasil = tk.Label(root, text="")
hasil.pack()

# Menjalankan aplikasi
root.mainloop()
