import random
import math
from collections import Counter
import datetime
from datetime import date
from datetime import time

# video 34 yani ders 32
print("\n VİDEO 34 \n")
# random ve math modulu

print("Random 0la 1 aralikli sayi:",random.random()) # 0la 1 arasinda sayi verir random sekilde
print("random aralikli sayi: ",random.uniform(5,10)) # 5 ile 10 arasi random bi sayi
print("Rastgele int sayi:",random.randint(8,100)) # 8le 100 arsai rastgele bir int sayi
liste1=[*range(10)]
print("Lİsteye cevirdikten sonra choice:",random.choice(liste1)) # listeden rastgele bir eleman alma komutu
print("Listeye cevirmeden choice:",random.choice(range(20))) # listeye cevirmeden de choice kullanabildik.
print("belirli aralıkta belirli sayida random sayi:",random.sample(range(100),k=4))
print("Shuflle etmeden once liste:   {}".format(liste1))
random.shuffle(liste1)
print("Shuffle ettikten sonra liste:",liste1)

print("Ceil yukarıya yuvarlar:",math.ceil(5.1))
print("Floor alta yuvarlar",math.floor(7.9))
# round ise nereye yakinsa oraya yuvarlar
print("faktoriyel:",math.factorial(4))
print("us alma:",math.pow(3,2))

# video 35 yani ders 33
print("\n VİDEO 35 \n")
#collection modulu
list1= random.sample(range(10),k=5)
list2= random.sample(range(10),k=5)
list3= random.sample(range(10),k=5)
list4= random.sample(range(10),k=5)
liste_listesi=[list1,list2,list3,list4]# 4elemanlı listeler listesi
list_toplam= list1+list2+list3+list4 # 12 elemanli genis bir liste
print(liste_listesi)
print(list_toplam)
for index, liste in enumerate(liste_listesi):
    print("{}.liste {}".format(index+1,liste))
sayac=Counter(list_toplam)
print(sayac)
print(Counter("askdjfadsdsfsdf"))
sarki= """Yine bana gel
Yana yana yine beni sev
Yine bana gel
Yana yana yine beni sev
"""
print(Counter(sarki))
print("Kucuk harfe cevrilmemis hali:\n",Counter(sarki.split()))
sarki= sarki.lower()
print("kucuk harfli hali:\n",Counter(sarki.split()))
sarki=sarki.lower().split()
print(Counter(sarki).most_common(3)) # en cok tekrar eden verileri yazdiriyor.

# video 36 yani ders 34
print("\n VİDEO 36 \n")

bugun= date.today()
print(bugun)
dun=date(2025,1,21)
print(dun)
print(bugun-dun)
yarin=bugun+ datetime.timedelta(days=1)
print(yarin)
print(dun<bugun)
print(bugun.year,bugun.month,bugun.day)
print(bugun.__getattribute__("month"))
print(date.isocalendar(bugun)) # hangi haftada oldugumuzu haftanın kacinci gununde oldugumuzun verisini verir.
print(date.weekday(bugun))
#0 pazartesi 1 saliya 2 carsambaya.. esit
print(date.ctime(bugun)) # gun ve ay isimlerinin verilmesini sagladı

zaman=time(15,24,20)
print(zaman)
print(zaman.hour,zaman.minute,zaman.second)
# datetime date ve time kutuphanelerinin birlesmis hali gibi
dt=datetime.datetime(2025,1,22,15,27,46)
print(dt)

# video 37 yani ders 35
print("\n VİDEO 37 \n")

def deneme():
    print("Deneme fonksiyonu çalışıyor.")  # Ana fonksiyonun çıktısı
    def test():
        return "test fonksiyonu çalışıyor"  # İç içe bir fonksiyon tanımlandı
    print(test())  # İçteki fonksiyon çağrıldı ve sonucu yazdırıldı

# Fonksiyon referansı ile çalıştırma
f = deneme  # deneme fonksiyonu bir referansa atanıyor
f()  # f çağrılarak deneme fonksiyonu çalıştırılır

print("")

# Bir başka fonksiyon tanımlaması
def deneme1():
    return "Deneme fonksiyonu çalışıyor"  # Basit bir string döndürür

# Bir fonksiyon, başka bir fonksiyonu argüman olarak alır
def ikinci(a):
    print("ikinci fonksiyon çalışıyor.")  # Bilgilendirici çıktı
    print(a())  # Argüman olarak gelen fonksiyon çalıştırılır ve sonucu yazdırılır

ikinci(deneme1)  # deneme1 fonksiyonu ikinci'nin içine argüman olarak verilir

# Dekoratör tanımlaması
def deco(f):
    # Wrapper: Fonksiyonu süsleyen iç fonksiyon
    def wrapper(*args):  # *args ile dinamik argümanlar alınır
        print("başlangıç")  # Fonksiyon çağrılmadan önceki çıktı
        f(*args)  # Asıl fonksiyon çağrılır
        print("bitiş")  # Fonksiyon çağrıldıktan sonraki çıktı
    return wrapper  # Wrapper fonksiyonu döndürülür

# Basit bir yazdırma fonksiyonu
def yazdir():
    print("yazdır")

# yazdir fonksiyonunu deco dekoratörü ile süslüyoruz
@deco
def yazdir():
    print("yazdır")

yazdir()  # yazdir fonksiyonunu çağırıyoruz, dekoratör uygulanmış hali çalışır

print("")

# Parametre alan bir fonksiyon için dekoratör
@deco
def toplama(a, b):  # İki parametreli toplama fonksiyonu
    print(a + b)  # Parametrelerin toplamını yazdırır

toplama(4, 5)  # Dekoratörlü toplama fonksiyonunu çağırıyoruz

print("")

# Mesajları özelleştirebilen bir dekoratör
def deco1(msg1, msg2):  # İki mesaj alır
    # Ara katman fonksiyonu
    def ara_katman(f):
        # Wrapper: Fonksiyonu süsleyen iç fonksiyon
        def wrapper(*args):
            print(msg1)  # İlk mesaj yazdırılır
            f(*args)  # Asıl fonksiyon çağrılır
            print(msg2)  # Son mesaj yazdırılır
        return wrapper  # Wrapper döndürülür
    return ara_katman  # Ara katman döndürülür

# Basit bir yazdırma fonksiyonu
def yazdir1():
    print("yazdır")

# deco1 dekoratörü ile toplama fonksiyonunu süslüyoruz
@deco1("ilk", "sonuç")  # Mesajlar: "ilk" ve "sonuç"
def toplama(a, b):  # İki parametreli toplama fonksiyonu
    print(a + b)  # Parametrelerin toplamını yazdırır

toplama(8, 13)  # Dekoratörlü toplama fonksiyonunu çağırıyoruz


