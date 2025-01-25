#video 3 yani ders 1
print("VİDEO 3\n")
print("Selam")
# print içerisinde \n \t kullanılabiliyor.(aslında bilinen seyler sadece not almak için ekledim)
print("Benim adım {}".format("Mesut"))
# format(degisken) süslü parantez içinin doldurulmasını sağladı
print("Benim adım {}, yasim {}".format("Mesut",32))
print("Benim adım {1}, yasim {0}".format("Mesut",32))
print("Benim adım {ad}, yasim {yas}".format(ad="ahmet",yas=40))
#en saglikli yontem son yontemdir.

#video 4 yani ders 2
print("\nVİDEO 4\n")
sayi=10
print(sayi*sayi)
#degisken adlari sayi ile baslayamaz.
_ = 20
print(_)
# sabit degisken isimlerine print gibi atama yapilabilir ama bi faydasi olmaz

#video 5 yani ders 3
print("\nVİDEO 5 \n")
# string tanımlamalarda "" veya '' kullanilabilir.
# list icerisnde veriler ayni tipte olmak zorunda degil,ust siniri yok, ayni veri tekrar edebilir.
# list tanımında [] kullanılır.
# set {} tanimiyla yapilir.
# set tanımında birden fazla aynı elemandan varsa tek defa sayar.
#dictionary {} tanimiyla yapilir.
x = {"isim": "mehmet", "yas": 40}
print(x["isim"])
print(x["yas"])
#tuple () şeklinde olusturulur. list yapisinin degistireleyen hali gibidir.
print(type(3))
print(3.1*5)

#video 6 yani ders 4
print("\nVİDEO 6\n")
var ="python"
print(type(var))
print(var)
print("son eleman:",var[-1])
#terstten siralama da yapilabilir son eleman -1 den başlar sonra -2,-3,-4,-5 ve 0 olarak tamamlanır(6 harfli str icin)
print(var[2:4])
#baslangic bitis arasi elemanlar alinir.baslangic indexi dahilken biis indexi dahil edilmez.
print(var[1::2])
# baslangictan baslayarak atlamali gider.
print("uzunluk:{}".format(len(var)))
var+= " ogren! "
# bu sekilde stringler birbirine eklenebilir.
print(var)
#var*= 5 # bu sekilde stringi kendyle carpabiliyoruz
#print(var)
var=var.upper()
print("upper kullanimi: ",var)
var= var.lower()
print("lower kullanimi:",var)
print(var.split(sep="o",maxsplit=1))
print(var.split("o"))
# max split degerini 1 yaparak sadece 1 kere bolmesini sagladik.

# video 7 yani ders 5
print("\nVİDEO 7\n")
a= True
b= False
print(a,b)
yas1=20
print(yas1>18)
print(not yas1<18)
# not -1le carpmak gibi tam tersini donderiyor yani.

# video 8 yani ders 6
print("\nVİDEO 8\n")
liste=["a","b","c","d","e","a"]
liste= liste + list("f")
# + "f" seklinde kullanamayız bu str tipind eoldugu icin eklemez.
liste+= [3]
print(liste)
print("3ten 5e:",liste[3:5])
liste.append("g")
# tekrardan atamaya ihtiyaci yok
print("append test adimi:",liste)
liste.pop()
# pop bossa sondaki indexi atar doluysa girilen indexi atar.
print("pop testi:",liste)
sayilar=[123,12321,321,45434,35,345,1,1]
sayilar.sort()
# sayilarin siralanmasini saglar.
print("Sort denemesi:",sayilar)
sayilar.reverse()
print("Reverse denemesi:",sayilar)
sayilar= set(sayilar)
# bu sayede tekrar eden degerleri teke indirdik.
print("set'e donusturme:",sayilar)
# yazdırırken [] bu kullanımdan {} bu kullanıma gecti.

# video 9 yani ders 7
print("\nVİDEO 9\n")
tup= tuple(liste)
#[] bu kullanımdan () bu kullanıma gectik ve tup verileri artik degistirielemez oldu.
print("Tuple listesi:",tup)
liste[0]=12312
###tup[0]=12312 bu degistirelemez oldugunu ispatlamak icin
print(liste)
print(tup.count("a"))
print(tup.index("a"))
print(tup.index("a", 4))

# video 10 yani ders 8
print("\nVİDEO 10\n")
dict1= {"isim": "Barış","yaş":20,"lokasyon":"İzmit"}
dict2= {
    "isim": "can",
    "yaş":14,
    "lokasyon":"gebze"
}
#iki tanımlamada aynı mumkun oldukça 2.yi kullanmak gerek(okunabirliğin artması icin
dict3= {
    "isim": "can",
    "yaş":14,
    "lokasyon":{
        "dogdugu sehir":"gebze",
        "yasadigi sehir":"istanbul"
}}
print(dict3)
print("Lokasyon:",dict3["lokasyon"])
print(dict3.get("lokasyon").get("yasadigi sehir"))
