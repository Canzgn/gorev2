import requests
# video 38 yani ders 36
print("\n VİDEO 38 \n")
# Bir kullanıcı, sunucu ile belirli HTTP metotları (GET, POST, PUT, DELETE vb.) üzerinden haberleşir.
# Status code (durum kodu), sunucunun isteğe verdiği cevabı ifade eder.
# Örneğin:
# - 200: Başarılı.
# - 404: Bulunamadı.
# - 500: Sunucu hatası.
# Content type (içerik türü), sunucunun dönen cevabın türünü belirtmek için kullanılır.
# Örneğin:
# - application/json: JSON formatında veri döner.
# - text/html: HTML formatında veri döner.

# video 39 yani ders 37
print("\n VİDEO 39 \n")

# Sunucudan veri almak için requests modülü kullanılıyor
response = requests.get("https://data.police.uk/api/forces")  # API'den veri çekiliyor
print(response)  # Response nesnesinin detaylarını yazdırır

# 200 status kodu, isteğin başarılı bir şekilde sonuçlandığını gösterir
print(response.status_code)  # Status kodunu yazdırır

# Sunucudan dönen JSON formatındaki cevabı yazdırır
print(response.json())

# Suç kategorilerini çekmek için kullanılan API URL'si
suc_kategorileri_URL = "https://data.police.uk/api/crime-categories"

# Bu API çağrısı için gerekli olan parametreler (payload) tanımlanıyor
payload = {"date": "2020-01"}  # 'date' parametresi, 2020-01 ayını belirtiyor

# API'ye GET isteği yapılır ve yanıt alınır
response1 = requests.get(suc_kategorileri_URL, params=payload)

# Response nesnesinin detaylarını yazdırır
print(response1)

# İstek sonrası oluşan tam URL'yi yazdırır (parametrelerin eklendiği haliyle)
print(response1.url)

