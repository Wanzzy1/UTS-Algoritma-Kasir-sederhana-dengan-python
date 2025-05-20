# Algoritma Kasir Sederhana

kode_barang = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6']
nama_barang = ['Beras/1kg', 'Minyak Goreng/1L', 'Indomie ', 'Telur (1 kg)', 'Terigu', 'Kopi Sachet']
harga_barang = [11000, 20000, 4000, 32000, 20000, 2000]

keranjang = ["", "", "", "", "", ""]
jumlah_barang = [0, 0, 0, 0, 0, 0]
subtotal_barang = [0, 0, 0, 0, 0, 0]

total_belanja = 0
lanjut = "ya"
slot = 0



# Tampilan Daftar Barang 

print("==================================")
print("          Toko Sakamoto           ")
print("\nDaftar Barang Toko Sakamoto     ")
print("==================================")
print(kode_barang[0],"-", nama_barang[0],"-", "Rp.", harga_barang[0])
print(kode_barang[1],"-", nama_barang[1],"-", "Rp.", harga_barang[1])
print(kode_barang[2],"-", nama_barang[2],"-", "Rp.", harga_barang[2])
print(kode_barang[3],"-", nama_barang[3],"-", "Rp.", harga_barang[3])
print(kode_barang[4],"-", nama_barang[4],"-", "Rp.", harga_barang[4])
print(kode_barang[5],"-", nama_barang[5],"-", "Rp.", harga_barang[5])

# Input belanja

while (lanjut == "ya" or lanjut == "YA" ) and slot < 6 :
    kode = input("\nMasukkan Kode Barang : ")

    if kode == "A1" :
        index = 0
    elif kode == "B2" :
        index = 1
    elif kode == "C3" :
        index = 2
    elif kode == "D4" :
        index = 3
    elif kode == "E5" :
        index = 4
    elif kode == "F6" :
        index = 5
    else :
        print("Kode barang tidak ditemukan")
        index = -1
    
    if index != -1 :
        jumlah = int(input("Masukkan Jumlah Beli : "))
        nama = nama_barang[index]
        harga = harga_barang[index]
        subtotal = jumlah * harga

        keranjang[slot] = nama
        jumlah_barang[slot] = jumlah
        subtotal_barang[slot] = subtotal

        total_belanja = total_belanja + subtotal 
        slot += 1

        lanjut = input("Apakah kamu ingin menambah barang lain? (ya/tidak) : ")

# Hitung Diskon
if total_belanja > 100000 :
    diskon = total_belanja * 0.1
elif total_belanja > 50000 :
    diskon = total_belanja * 0.05
else :
    diskon = 0

total_bayar = total_belanja - diskon

# Tampilan Struk Belanja
print("==================================")
print("           Struk Belanja          ")
print("==================================")

if keranjang[0] != "" :
    print(keranjang[0], "x", jumlah_barang[0],"= Rp.",subtotal_barang[0])
if keranjang[1] != "" :
    print(keranjang[1], "x", jumlah_barang[1],"= Rp.",subtotal_barang[1])
if keranjang[2] != "" :
    print(keranjang[2], "x", jumlah_barang[2],"= Rp.",subtotal_barang[2])
if keranjang[3] != "" :
    print(keranjang[3], "x", jumlah_barang[3],"= Rp.",subtotal_barang[3])
if keranjang[4] != "" :
    print(keranjang[4], "x", jumlah_barang[4],"= Rp.",subtotal_barang[4])
if keranjang[5] != "" :
    print(keranjang[5], "x", jumlah_barang[5],"= Rp.",subtotal_barang[5])


print("==================================")
print("Total Belanja    : Rp.",total_belanja)
print("Diskon           : Rp.",diskon)
print("Total Bayar      : Rp.",total_bayar)
print("==================================")
print("   Terima Kasih Telah Berbelanja   ")
print("==================================")
print("          Sakamoto Store          ")
print("----------------------------------")
