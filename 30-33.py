import os
import re

# video 30 yani ders 28
print("\n VİDEO 30 \n")
# Dosya ve klasör işlemleri
# pwd ile path'i göstermek
print("Projemin bulunduğu adres:", os.getcwd())  # Mevcut çalışma dizinini gösterir

# Mevcut klasördeki dosya ve klasörleri listeleme
print(os.listdir())  # Geçerli klasörün içeriğini gösterir

# Belirtilen bir klasörün içeriğini listeleme
print(os.listdir("C:\\Users"))  # "Users" klasörünün altındaki içerik

# Çalışma dizinini değiştirme
os.chdir("C:\\Users")  # Çalışma ortamını değiştir
print("Yeni çalışma dizini:", os.getcwd())  # Yeni çalışma dizinini yazdır
print(os.listdir())  # Yeni çalışma dizininin içeriğini listele

# Dosyaları döngü ile listeleme
dosyalar = os.listdir()
for eleman in dosyalar:
    print("Users'ın altındaki:", eleman)

# Çalışma dizinini yeniden değiştir
os.chdir("C:\\Users\\PAVİLİON\\PycharmProjects\\PythonProject")
print("Yeni çalışma dizini:", os.getcwd())  # Yeni çalışma dizinini yazdır
print(os.listdir())  # İçeriği listele

# Yeni klasör oluşturma
klasor_yolu = "C:\\Users\\PAVİLİON\\PycharmProjects\\PythonProject\\deneme"

# Klasörün var olup olmadığını kontrol ederek oluşturma
if not os.path.exists(klasor_yolu):
    os.mkdir(klasor_yolu)
    print(f"Klasör oluşturuldu: {klasor_yolu}")
else:
    print(f"Klasör zaten mevcut: {klasor_yolu}")

# Mevcut dosya ve klasörleri yazdırma
dosyalar = os.listdir()
for eleman in dosyalar:
    print("Projenin altındaki:", eleman)
#print(os.mkdir("C:\\Users\\PAVİLİON\\PycharmProjects\\PythonProject\\deneme"))
print(os.listdir())  # deneme klasoru de eklendi
print(os.rmdir("C:\\Users\\PAVİLİON\\PycharmProjects\\PythonProject\\deneme"))
print(os.listdir())  # deneme klasoru silindi yukarıdaki rmdir sayesinde

yeni_dosya = os.open("yeni_dosya.txt", os.O_RDWR | os.O_CREAT)
# rdwr sayesinde hem dosyayı okuma hem yazma işlemini yapabiliyoruz.
os.write(yeni_dosya,"Merhaba Dunya!".encode())
os.close(yeni_dosya)
yeni_dosya = os.open("yeni_dosya.txt", os.O_RDONLY )
uzunluk= os.stat(yeni_dosya).st_size # daha dinamik dosya yapisini okumayisaglar.
print(os.read(yeni_dosya,uzunluk))
os.close(yeni_dosya)
os.unlink("yeni_dosya.txt") # dosyayi silmemizi saglayan komut
#os.mkdir("deneme_yeni")
#print(os.listdir())
#print(os.rename("deneme_yeni","deneme_eski"))
print(os.listdir())
#os.rmdir("deneme_yeni")
# os.rmdir("deneme_eski") # dosyayi silme islemi için gerekliydi

# video 31 yani ders 29
print("\n VİDEO 31 \n")

cumle = "Mustafa Kemal Atatürk, Türk asker, devlet adamı ve Türkiye Cumhuriyeti'nin kurucusudur."
patern = "Türk"
durum=re.search(patern, cumle)
print(durum.span())
print(dir(durum)) # sahip oldugu özellikler
print("baslangic:",durum.start())
print("son:",durum.end())
for eslesme in re.finditer(patern,cumle):
    print(eslesme.span(),eslesme.group())
ornek = "en sevdigim kanal base42"
patern=r"base\d\d" #\d rakamlari bulabiliriz.
durum=re.search(patern,ornek)
print(durum)
cumle = "Selam, benim telefon numaram 0535-8886622."
patern = r"\d\d\d\d-\d\d\d\d\d\d\d"
durum=re.search(patern, cumle)
print(durum)
# degisken durumlarda aramayi \d komutuyla hallettik

# video 32 yani ders 30
print("\n VİDEO 32 \n")

cumle = "Selam, benim telefon numaram 0535-8886622."
patern = r"\d{3,4}-\d{7}" # \w isareti de kullanilabilir.
# \d {3,4} yapmamizin sebebi numara baslabgicinin 0535 veya 535 seklinde yapilabiliyor olmasi
durum=re.search(patern, cumle)
print(durum)
cumle = "En sevdigim kanal 42base."
patern = r"\s\w{5,}"
# \s koyarak boslukla balmasini sagladik
#\w{5,} ekleyerek de 5 harf ve 5 harften buyuk kelimeleri aramasini sagladik
i=1
for eslesme in re.finditer(patern, cumle):
    print("{}. eslesme".format(i),eslesme.group(), eslesme.span())
    i+=1

cumle = "En sevdigim kanal 42base."
patern = r"\w*\d+"

for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span())

def gsm_operator_bul(tel_no):
    patern = r"(\d{3})-(\d{7})"
    eslesme = re.search(patern, tel_no)

    if eslesme:
        gsm_kod = eslesme.groups()[0]
        print(gsm_kod)
        if gsm_kod.startswith("54"):
            return "Vodafone"
        elif gsm_kod.startswith("501") or gsm_kod.startswith("505") or gsm_kod.startswith("506"):
            return "AVEA"
        elif gsm_kod.startswith("53"):
            return "Turkcell"
        else:
            return "Sebeke bulunamadi"
    else:
        return "Patern bulunamadi"

print("")

tel_no = "Selam, benim telefon numaram 0535-8886622."
print(gsm_operator_bul(tel_no))
# bu da tum yaptıklarimizi gormek amacli bir ornek oldu

# video 33 yani ders 31
print("\n VİDEO 33 \n")


def mesaj_hissi_bul(mesaj):
    hisler = []  # Hisleri saklamak için bir liste oluşturuyoruz.

    # Pozitif hisler için düzenli ifade (pattern)
    pozitif_patern = r"(merhaba|selam|ask|sevgi|dost|kardes|:\)+)"
    # Negatif hisler için düzenli ifade
    negatif_patern = r"(lan|aptal|abv|yeter|birak)"

    # Heyecanlı ifadeler için düzenli ifade (! ve birden fazla ünlem veya soru işareti)
    heyecanli_patern = r"!|[!|?]{2,}$"
    # Sakin ifadeler için düzenli ifade (örneğin "Tabi", "Hayhay")
    sakin_patern = r"^[T|t]abi+|[H|h]ayhay]"

    # Eminlik belirten ifadeler için düzenli ifade
    emin_patern = r"[K|k]esin|[T|t]abi|[E|e]lbet"
    # Kararsızlık belirten ifadeler için düzenli ifade
    kararsiz_patern = r"[B|b]elki|[S|s]anirim"

    if re.search(pozitif_patern, mesaj):
        hisler.append("Pozitif")
    if re.search(negatif_patern, mesaj):
        hisler.append("Negatif")
    if re.search(heyecanli_patern, mesaj):
        hisler.append("Heyecanli")
    if re.search(sakin_patern, mesaj):
        hisler.append("Sakin")
    if re.search(emin_patern, mesaj):
        hisler.append("Emin")
    if re.search(kararsiz_patern, mesaj):
        hisler.append("Kararsiz")

    return hisler

# Örnek mesajlar
cumle1 = "Naber abi? :)             "
cumle2 = "Tabiii ki buyrun          "
cumle3 = "Sacmalamayi birak artik!  "
cumle4 = "Belki yarindan da yakin..."
cumle5 = "Elbet birgün bulusacagiz  "

# Mesajları bir listeye ekleyip döngü ile hisleri tespit ediyoruz.
cumleler = [cumle1, cumle2, cumle3, cumle4, cumle5]
for cumle in cumleler:
    # Her cümlenin hislerini tespit edip yazdırıyoruz.
    print(cumle, '\t', mesaj_hissi_bul(cumle))
