class Sarkuteri:
    def __init__(self, isim):
        self.isim = isim
        self.urunler = []

    def urun_ekle(self, urun, fiyat, stok):
        self.urunler.append({"urun": urun, "fiyat": fiyat, "stok": stok})
        print(f"{urun} şarküteriye eklendi. Fiyatı: {fiyat} TL, Stok: {stok} adet")
        print("//////////////////////////")

    def urun_sil(self, urun):
        for u in self.urunler:
            if u["urun"] == urun:
                self.urunler.remove(u)
                print(f"{urun} şarküteriden silindi.")
                print("//////////////////////////")
                return
        print(f"{urun} şarküteride bulunmuyor.")
        print("//////////////////////////")

    def urun_listele(self):
        print("Şarküterideki ürünler:")
        for u in self.urunler:
            print(f"{u['urun']}: Fiyatı: {u['fiyat']} TL, Stok: {u['stok']} adet")
            print("//////////////////////////")

    def fiyat_arttir(self, adi, fiyat):
        for u in self.urunler:
            if u["urun"] == adi:
                u["fiyat"] += fiyat
                print(f"{adi} ürününü fiyatı {fiyat} TL artırıldı.")
                print("//////////////////////////")
                return
        print("Böyle bir ürün bulunmamaktadır.")
        print("//////////////////////////")

    def fiyat_azalt(self, adi, fiyat):
        for u in self.urunler:
            if u["urun"] == adi:
                u["fiyat"] -= fiyat
                print(f"{adi} ürününü fiyatı {fiyat} TL azaldı.")
                print("//////////////////////////")
                return
        print("Böyle bir ürün bulunmamaktadır.")
        print("//////////////////////////")

    def stok_arttir(self, adi, stok):
        for u in self.urunler:
            if u["urun"] == adi:
                u["stok"] += stok
                print(f"{adi} ürününü stok miktarı {stok} adet arttırıldı.")
                print("//////////////////////////")
                return
        print("Böyle bir ürün bulunmamaktadır.")
        print("//////////////////////////")

sarkuteri = Sarkuteri("Nevale Peynircilik")
while True:
    try:
        print(f"{sarkuteri.isim} Menüsü:")
        print("1. Ürün Ekle")
        print("2. Ürün Sil")
        print("3. Ürün Listele")
        print("4. Fiyat Arttır")
        print("5. Fiyat Azalt")
        print("6. Stok Arttır.")
        print("7. Çıkış")
        secim = int(input("Seçiminiz: "))

        if secim == 1:
            urun = input("Ürün Adı: ")
            fiyat = float(input("Fiyat : "))
            stok = int(input("Stok Miktarı : "))
            sarkuteri.urun_ekle(urun, fiyat, stok)
        elif secim == 2:
            urun = input("Ürün adı: ")
            sarkuteri.urun_sil(urun)
        elif secim == 3:
            sarkuteri.urun_listele()
        elif secim == 4:
            urun = input("Ürün adı: ")
            miktar = float(input("Zam Yapılacak Miktar: "))
            sarkuteri.fiyat_arttir(urun, miktar)
        elif secim == 5:
            urun = input("Ürün adı: ")
            miktar = float(input("Miktar: "))
            sarkuteri.fiyat_azalt(urun, miktar)
        elif secim == 6:
            urun = input("Ürün adı: ")
            miktar = int(input("Miktar: "))
            sarkuteri.stok_arttir(urun, miktar)
        elif secim == 7:
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Geçersiz değer girdiniz. Lütfen tekrar deneyin.")
