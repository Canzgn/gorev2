# Video 27 yani ders 25
print("\n VİDEO 27 \n")
# class yapisi
# Sınıf (class), bir nesnenin yapısını ve davranışını tanımlayan bir şablondur.
# Nesne (object), bir sınıfın örneğidir. Yani sınıfa dayanarak oluşturulan somut bir veri.
 #Sınıflar, büyük projelerde kodu düzenli ve tekrar kullanılabilir hale getirmek için çok önemlidir.
#    - Nesne yönelimli programlama (OOP) prensipleri:
#      - Sınıf ve Nesne
#      - Encapsulation (Kapsülleme)
#      - Inheritance (Kalıtım)
#      - Polymorphism (Çok biçimlilik)
#      Python'da sınıflar, bazı özel metodlarla özelleştirilebilir.
#  - Örneğin, __init__, __str__, __len__ gibi metodlar.
class Ucus():
    havayolu = "THY"  # Sınıf genelinde sabit bir değişken

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        # Başlangıç özelliklerini tanımlıyoruz
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def yolcu_ekle(self, yeni_yolcu):
        # Kapasite kontrolü ile yolcu ekleme işlemi
        if self.yolcu + yeni_yolcu <= self.kapasite:
            self.yolcu += yeni_yolcu
            return f"{yeni_yolcu} yolcu eklendi. Toplam yolcu: {self.yolcu}"
        else:
            return "Kapasite aşıldı! Yolcu eklenemedi."

    def anons_yap(self):
        # Uçuş bilgilerini duyuran bir metot
        return "{} sefer sayılı {}-{} uçuşumuz {} dakika sürecektir. Toplam yolcu: {}.".format(
            self.kod, self.kalkis, self.varis, self.sure, self.yolcu
        )
    def koltuk_sayisi_guncelle(self):
        return self.kapasite-self.yolcu
    def bilet_satis(self,bilet_adedi=1):
        self.yolcu+= bilet_adedi
        self.koltuk_sayisi_guncelle()
        print("{} adet bilet satilmistir, kalan koltuk sayisi {}".format(
            bilet_adedi,self.koltuk_sayisi_guncelle()))
# Uçuş nesnesi oluşturuluyor
ucus1 = Ucus("TK123", "İstanbul", "Ankara", 60, 300, 50)

# Kodun çalışması ve çıktıları
print(ucus1.kod)  # Uçuş kodunu yazdır
ucus1.kod = "TK456"  # Kod güncellendi
print(ucus1.kod)

# Yolcu ekleme işlemi
print(ucus1.yolcu_ekle(20))
print(ucus1.yolcu_ekle(250))  # Kapasite aşımı kontrolü

# Anons yapma
print(ucus1.anons_yap())

# Video 28 yani ders 26
print("\n VİDEO 28 \n")
#tüm islemler class yapisinda yapildigi icin burasi bos duruyor.
# ama islem olarak class yapisi guncellemeyi gorduk.
print(ucus1.koltuk_sayisi_guncelle())

ucus1.bilet_satis(5)

# Video 29 yani ders 27
print("\n VİDEO 29 \n")
ucus2 = Ucus("TK139", "BDR", "ANT", 90, 250, 150)
print(ucus2.__dir__()) # classa ait olan metotlari gorebiliyoruz.
#kalitim
class seyahat(): #superclass
    def __init__(self,kalkis,varis):
        self.kalkis=kalkis
        self.varis=varis
    def anons(self):
        return "{}-{} seyahatine hosgeldiniz.".format(self.kalkis,self.varis)
class otobus(seyahat):# altclass
    def __init__(self,mola_duraklari):
        seyahat.__init__(self,"IST","ANK")
        self.mola_duraklari= mola_duraklari
seyahat1=seyahat("ANT","BDR")
print(seyahat1.anons())
oto1= otobus(["fet","Alanya"])
print(oto1.mola_duraklari)
print(oto1.anons())
# kalıtım yapısını zaten biliyordum burada da kod üzerinde ornekler yapmıs olduk


