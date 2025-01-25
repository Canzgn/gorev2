#video 13 ders 11
print("\nVİDEO 13\n")
hava_durumu = 'karli'

if hava_durumu == 'yagisli':
    print("Semsiyeni al!")
elif hava_durumu == 'karli':
    print("Atkini al!")
else:
    print("Sikinti yok!")

liste = ["a", "b", "c"]
hedef_harf = "e"

if hedef_harf in liste:
    print("buldum")
else:
    liste.append(hedef_harf)
    print("listeye ekledim")
    print("guncel liste {}".format(liste))

hedef_harf = "a"

if hedef_harf in liste and hedef_harf == liste[0]:
    print("buldum ve ilk harf konumunda")
elif hedef_harf in liste:
    print("buldum ama ilk konumda degil")
else:
    liste.append(hedef_harf)
    print("ekledim")
    print("guncel liste {}".format(liste))
    # bu videoda if yapısını and ve or kullanımı vs. anlattı zaten bilinen şeylerin formal farklılığını öğrenmiş oldum.
#video 14 ders 12
print("\nVİDEO 14\n")
yorum_birakanlar = ["Ismail Aydemir", "Uygar Aydin", "Naz Yagcioglu","Ferhat Ibrik","Ulas Acil", "Bilal Kurucay"]
for isim in yorum_birakanlar:
    print(isim)
print("\n")
kullanici_sayi = 0
for isim in yorum_birakanlar:
    kullanici_sayi+=1
    print(kullanici_sayi, isim)
print("\n")
kullanici_sayi = 0

for isim in yorum_birakanlar:
    kullanici_sayi+=1
    ad, soyad = isim.split()[0], isim.split()[1]
    print('{0}. Kullanicinin Adi {1} ve Soyadi {2}'.format(kullanici_sayi,ad,soyad))

#video 15 ders 13
print("\nVİDEO 15\n")
tup1=(1,2,3,4,5)
for sayi in tup1:
        print(sayi)
liste1= [[1,2],[3,5],[7,8]]
for x,y in liste1: # bu sekilde matris benzeri listeleri ekrana yazdirma seklini pgrenmis oldum.
    print(x,"\t",y)
    print("Carpimlari:",x*y)
kullanici1 = {
    "ad":"Naz",
    "soyad":"yagci"
}
print(kullanici1.items())
#forun listeler dışında kullanımı gormus oldum

#video 16 ders 14
print("\nVİDEO 16\n")
#while
x=0
while x<10:
    print("{} degeri 10'dan kucuktur".format(x))
    x+=1
print("\n")
x=8
while x < 10:
        print("{} degeri 10'dan kucuktur".format(x))
        x += 1
else:
    print("{} degeri 10'dan kucuk degil".format(x))
# while de hem normal haliyle hem de else haliyle kullanım vardır.

#video 17 ders 15
print("\nVİDEO 17\n")

# range enumerate ve zip yapilari
print(range(10))# 10 dahil degil ama 0 dahil 0'dan 10'a kadar gider.
print(list(range(12)))
print([*range(2,10)])# * işaretle list[ açmaya gerek kalmadna ayni şeyi elde ederiz.
print([*range(2,12,3)]) # 3er atlamalı sekilde ilerler.

for sayi in range (10):
    if sayi%6==0 and sayi!=0:
        print(sayi)
# boylelikle lsit yapisi olusturmaya gerek kalmadan pratik islem yapabildik.
# enumerate
harfler =["a","b","c","d","e"]
for harf in enumerate(harfler):
    print(harf)
# enumerate elemanı indexiyle beraber bastiriyor.
for index,harf in enumerate(harfler):
    print("index:{0} harf:{1}".format(index,harf))
# burada da indexi ve harfi ayrı ayrı yazdirabilecegimizi yani ayirabilecegimizi gosteriyor
# zip yapisi
ulkeler=["TR","FR","DE"]
siralamalar= range(1,4)
for ulke in zip(ulkeler,siralamalar):
    print(ulke)
# uzunlugu esit iki listenin birlestirilmesini saglamis gibi bi sey oldu.

#video 18 ders 16
print("\nVİDEO 18\n")
# break, continue ve pass komutlari
harfler =["a","b","c","d","e","f"]*100
for index,harf in enumerate(harfler):
    if harf=="c":
        print("{} harfi {}. indexte".format(harf.upper(),index))
        break # bu sayede 500 tane c yi tek tek kontrol etmesine engel olundu.
for sayi in range(1,5):
    if sayi%2==0:
        continue # bu sayede cift sayilari ekrana bastirmama isini donguyu kesmeden halletmis olduk.
    print("Tek sayilar:{}".format(sayi))
for sayi in range (1,8):
    if sayi%2==0:
        pass
    else:
        print(sayi)










