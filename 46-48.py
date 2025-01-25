import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from imap_tools import Mailbox
from imap_tools import AND
import datetime

#video 46 yani ders 44
print("\n VİDEO 46 \n")
kullanici = "barisozgen101@gmail.com"
sifre = "x"  # Gmail uygulama şifrenizi buraya girin

# Alıcı bilgisi
alici = kullanici

# E-posta içeriği
mesaj= "Merhaba"
baslik="PYthon gönderisi"
context=ssl.create_default_context()

# SMTP ayarları
host = "smtp.gmail.com"
port = 465

eposta_sunucu=smtplib.SMTP_SSL(host=host,port=port,context=context)
eposta_sunucu.login(kullanici, sifre) # Kimlik doğrulama
eposta_sunucu.sendmail(kullanici, alici, mesaj)  # E-posta gönderimi
print("E-posta başarıyla gönderildi!")

# epostadaki bu gonderememe sorununu cozemedim ama ne nasil yapiliyor anladim

#video 47 yani ders 45
print("\n VİDEO 47 \n")

# MIMEMultipart sınıfı ile çok parçalı bir e-posta oluşturuluyor
posta = MIMEMultipart()
posta["From"] = kullanici  # Gönderen adresi
posta["To"] = kullanici  # Alıcı adresi
posta["Subject"] = baslik  # E-posta konusu (başlık)

# E-posta gövdesine metin ekleniyor
posta.attach(MIMEText(mesaj, "plain"))  # Düz metin (plain text) olarak ekleniyor

# Eklenecek dosyanın adı
eklenti_dosya_ismi = "arjantin.jpg"

# Dosya okuma ve e-postaya ekleme işlemi
with open(eklenti_dosya_ismi, "rb") as eklenti_dosyasi:  # Dosya okuma modunda açılıyor
    payload = MIMEBase("application", "octate_stream")  # Dosya için MIMEBase sınıfı kullanılıyor
    payload.set_payload(eklenti_dosyasi.read())  # Dosyanın içeriği yükleniyor
    encoders.encode_base64(payload)  # Dosya içeriği base64 formatına kodlanıyor
    payload.add_header("Content-Disposition", "attachment", filename=eklenti_dosya_ismi)  # Dosya ek olarak tanımlanıyor
    posta.attach(payload)  # Dosya e-postaya ekleniyor

# E-posta içeriğini bir string'e dönüştürme
posta_str = posta.as_string()

# SMTP sunucusuna bağlanma ve oturum açma (tekrar)
host = "smtp.gmail.com"  # Gmail SMTP sunucusu
port = 465  # SSL için bağlantı noktası
eposta_sunucu = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucu.login(kullanici, sifre)  # Kimlik doğrulama işlemi

# E-posta gönderimi
eposta_sunucu.sendmail(kullanici, alici, posta_str)  # Gönderen, alıcı ve mesaj belirtiliyor
print("E-posta başarıyla gönderildi!")  # İşlem başarıyla tamamlandıysa mesaj yazdırılıyor

# yine notlar aldım ama yeterince duzgun calıstiramiyorum nasıl yapilacigini ogrenmeye odaklandım

#video 48 yani ders 46
print("\n VİDEO 48 \n")
# Gmail IMAP sunucusuna bağlantı sağlıyoruz
posta_kutusu = MailBox("imap.gmail.com")  # IMAP sunucusu tanımlanıyor

# Kullanıcı bilgileri ile giriş yapılıyor
posta_kutusu.login(kullanici, sifre, initial_folder="INBOX")  # Gelen kutusu (INBOX) varsayılan olarak ayarlanıyor
# E-posta filtreleme kriterleri
kriter = AND(
    date_gte=datetime.date(2022, 1, 1),  # 1 Ocak 2022 veya daha yeni tarihli e-postaları seç
    from_=kullanici  # Gönderen e-posta adresi filtreleniyor (kullanıcının kendi e-postası)
)
# E-postaları kriterlere göre tarıyoruz
for msg in posta_kutusu.fetch(kriter):  # Belirtilen kriterlere uygun e-postalar taranıyor
    print(msg.text)