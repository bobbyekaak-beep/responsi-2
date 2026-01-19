mahasiswa = []

def menu():
    print("\n=== MENU MANAJEMEN MAHASISWA ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Update Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Keluar")

def tambah_data():
    nrp = input("Masukkan NRP: ")
    nama = input("Masukkan Nama: ")
    prodi = input("Masukkan Program Studi: ")

    for m in mahasiswa:
        if m["nrp"] == nrp:
            print("Gagal menambahkan data! NRP sudah terdaftar.")
            return
        if m["nama"].lower() == nama.lower():
            print("Gagal menambahkan data! Nama sudah terdaftar.")
            return

    mahasiswa.append({
        "nrp": nrp,
        "nama": nama,
        "prodi": prodi
    })
    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_data():
    if not mahasiswa:
        print("Data mahasiswa masih kosong.")
    else:
        print("\nDaftar Mahasiswa:")
        for m in mahasiswa:
            print(f"NRP: {m['nrp']} | Nama: {m['nama']} | Prodi: {m['prodi']}")

def update_data():
    nrp = input("Masukkan NRP mahasiswa yang ingin diupdate: ")
    for m in mahasiswa:
        if m["nrp"] == nrp:
            m["nama"] = input("Masukkan nama baru: ")
            m["prodi"] = input("Masukkan program studi baru: ")
            print("Data mahasiswa berhasil diperbarui.")
            return
    print("Data mahasiswa tidak ditemukan.")

def hapus_data():
    nrp = input("Masukkan NRP mahasiswa yang ingin dihapus: ")
    for m in mahasiswa:
        if m["nrp"] == nrp:
            mahasiswa.remove(m)
            print("Data mahasiswa berhasil dihapus.")
            return
    print("Data mahasiswa tidak ditemukan.")

# Program utama (loop)
while True:
    menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
