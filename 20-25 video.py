#video 20 yani ders 18
print("\nVİDEO 20\n")
#fonksiyonlar
def bes_bastir():
    print(5)
bes_bastir()
def faktoriyel(n):
    """
    burası ne yapildigini tanitmak icin kullanilabilir.
    :return:
    """
    if n < 0:
        return "Hata: Faktöriyel sadece pozitif tam sayılar için tanımlıdır."
    elif n == 0 or n == 1:
        return 1
    else:
        sonuc = 1
        for i in range(2, n + 1):
            sonuc *= i
        return sonuc
# return kullanimi da boyle olur.
print(faktoriyel(6))

#video 21 yani ders 19
print("\nVİDEO 21\n")
def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b

def metin_yazdir(a,b):
    buyuk_sayi=buyuk_sayi_dondur(a,b)
    sablon_metin="{} daha buyuk sayidir".format(buyuk_sayi)
    print(sablon_metin)
metin_yazdir(8,12)
print(" ".join(["Gokce", "Gün"])) # join metodu kullanimi
def isim_yazdir(*args):
    for item in args:
        print(item)
isim_yazdir("Ali","Ahmet","Emre","Talha")
#  *arg sayesinde sayisiz parametre gireiek istedigimiz gibi fonksiyonu yonetme sansina sahip olduk
# **arg yapısı da dict ler için kullanilabilir.

#video 22 yani ders 20
print("\nVİDEO 22\n")
# map filter ve lambda yapilari
def karesini_al(x):
    return x**2 # x sayisinin karesini almak anlamina gelir
print(karesini_al(6))
sayilar=[*range(1,6)]
print("Karesi alinmadan once",sayilar)
for index in range(len(sayilar)):
    sayilar[index]=karesini_al(sayilar[index])
print("Karesi alindiktan sonra",sayilar)
print("Map:",[*map(karesini_al,sayilar)]) # listedeki sayilarin karesini aldik.
#filter hepsine uygulamaktansa filtrelenerek uygulanir
def cift_sayilari_filtrele(x):
     return x if x%2==0 else None

print(cift_sayilari_filtrele(4))

sayilar=[*range(1,6)]
filt=[*filter(cift_sayilari_filtrele,sayilar)]
print("filter kullanimi",filt)
list=[*map(lambda sayi: sayi**3,sayilar)] # lamda fonksiyon taniminin basit hali gibi bir şey
print("Map ve lambda beraber kullanimi:",list)

print("Filter ve lambda beraber kullanimi:",[*filter(lambda x: x if x%2==0 else None,sayilar)])

#video 23 yani ders 21
print("\nVİDEO 23\n")
#input komutu

#=input("bir sayi girin:")
#("girdiğiniz sayi:{}".format(girdi))

def uygulama():
    girdi = input("bir sayi girin:")
    islem=input("Verinin tek mi cift mi oldugunu sorgula:")
    if islem=="cift":
         if int(girdi)%2==0:
             return "Evet bu bir cift sayidir"
         else:
             return "HAyir bu bir cift sayi degildir"
    elif islem=="tek":
         if int(girdi)%2==1:
            return "evet bu bir tek sayidir"
         else:
             return "hayir bu bir tek sayi degildir"
#print(uygulama())
# input edilen iki komutun kullanimina bir ornek.

#video 24 yani ders 22
print("\nVİDEO 24\n")
# kullanici girdisini onaylamak

def sayi_girdisi_kontrol():
    girdi=input("bir sayi giriniz: ")
    if girdi.isdigit(): # isdigit integer olup olmadigini kontrol eder.
        print("tebrikler sayi tipi bir deger girdiniz!!")
    else:
        print("bu bir sayi tipi degisken degildir.")

#sayi_girdisi_kontrol()
def sayi_girdisi_kontrol_dongu():
    girdi=input("bir sayi giriniz: ")
    while not girdi.isdigit():
        print("bu bir sayi tipi degisken degildir.")
        girdi=input("bir sayi giriniz: ")
    else:
        print("tebrikler sayi tipi bir deger girdiniz!!")
#sayi_girdisi_kontrol_dongu()
# sayi girilene kadar sayi istedigi bir sistem kurarak sayi girmesini sagladik.

#video 25 yani ders 23
print("\nVİDEO 25\n")
# try, except ve finally komutlari
def tam_sayiya_cevir():
    girdi = input("Bir ondalik sayi giriniz: ")
    statu=""
    try:
        # Girdiyi float'a çeviriyoruz
        sayi = float(girdi)
        # Başarılıysa yuvarlama işlemi yapılır
        print("Yuvarlama isleminin sonucu: {}".format(round(sayi)))
        statu="basarili"
    except :
        # Hata durumunda kullanıcıya bilgi verilir
        print("{} girdisi tam sayiya cevrilemiyor.".format(girdi))
        statu="basarisiz"
    finally: # her durumda calisip durum bilgilendirmesi yapilabilir.
        print("tam sayiya cevirme islemi {} olarak tamamlandi".format(statu))

tam_sayiya_cevir()
