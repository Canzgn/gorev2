from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pyexpat.errors import messages
from tkcalendar import *
# video 41 yani ders 39
print("\n VİDEO 41 \n")
# gui arayuzu
# bu video hem 6 dakika hem cok sozel o yuzden not alamadım

# video 42 yani ders 40
print("\n VİDEO 42 \n")

master = Tk()
#PART 1
# Ana pencereye bir tuval (canvas) ekliyoruz
canvas = Canvas(master, height=450, width=750)
canvas.pack()  # Tuvali ana pencereye yerleştiriyoruz

# Üst çerçeveyi oluşturuyoruz (Hatırlatma tipi ve tarih seçici için)
frame_ust = Frame(master, background="#add8e6")  # Açık mavi arka plan
frame_ust.place(relx=0.1, rely=0.03, relwidth=0.8, relheight=0.17)  # Çerçevenin boyut ve konumu

# Sol alt çerçeveyi oluşturuyoruz (Ek bileşenler için)
frame_alt_sol = Frame(master, background="#add8e6")
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

# Sağ alt çerçeveyi oluşturuyoruz (Ek bileşenler için)
frame_alt_sag = Frame(master, background="#add8e6")
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

# Üst çerçeveye bir etiket (Label) ekliyoruz (Hatırlatma Tipi yazısı için)
hatirlatma_tipi_etiket = Label(frame_ust, background="#add8e6", text="Hatırlatma Tipi", font="Verdena 16 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)  # Etiketi çerçeve içinde hizalıyoruz

# Hatırlatma tipi için bir seçenek menüsü oluşturuyoruz
hatirlatma_tipi_opsiyon = StringVar(frame_ust)  # Seçenek menüsü için değişken
hatirlatma_tipi_opsiyon.set("\t")  # Varsayılan boş seçeneği ayarlıyoruz
hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    "Doğum Günü", "Alışveriş", "Ödeme"  # Seçenekler
)
hatirlatma_tipi_acilir_menu.pack(padx=1, pady=1, side=LEFT)  # Menüyü çerçeve içine yerleştiriyoruz

# Tarih seçici bileşeni ekliyoruz
hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background="orange", foreground="black")
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)  # Tarih seçiciyi hizalıyoruz

# Tarih etiketi ekliyoruz
hatirlatma_tarihi_etiket = Label(frame_ust, background="#add8e6", text="Hatırlatma Tarihi", font="Verdena 16 bold")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)  # Etiketi tarih seçicinin yanına yerleştiriyoruz

#PART 2
Label(frame_alt_sol, background="#add8e6", text="HATIRLATMA YÖNTEMİ", font="Verdena 10 bold").pack(
    padx=10, pady=10, anchor=NW
)

# Radiobutton'lar için seçilen değeri tutacak bir değişken tanımlanıyor
var = IntVar()

R1 = Radiobutton(
    frame_alt_sol,
    text="Sisteme Kaydet",  # Görüntülenecek metin
    variable=var,          # Bağlı değişken
    value=1,               # Bu seçeneğin değeri
    background="#add8e6",  # Arka plan rengi
    font="Verdena 8"       # Yazı tipi ve boyutu
)
R1.pack(anchor=NW, pady=5, padx=15)  # Yerleşim özellikleri

R1 = Radiobutton(
    frame_alt_sol,
    text="E-posta gönder",
    variable=var,
    value=2,
    background="#add8e6",
    font="Verdena 8"
)
R1.pack(anchor=NW, pady=5, padx=15)


var1 = IntVar()
C1 = Checkbutton(
    frame_alt_sol,
    text="Bir gün önce",   # Görüntülenecek metin
    variable=var1,         # Bağlı değişken
    onvalue=1,             # Seçili olduğunda alacağı değer
    offvalue=0,            # Seçili olmadığında alacağı değer
    bg="#add8e6",          # Arka plan rengi
    font="Verdena 8"       # Yazı tipi ve boyutu
)
C1.pack(anchor=NW, pady=2, padx=25)

var2 = IntVar()
C2 = Checkbutton(
    frame_alt_sol,
    text="Bir hafta önce",
    variable=var2,
    onvalue=1,
    offvalue=0,
    bg="#add8e6",
    font="Verdena 8"
)
C2.pack(anchor=NW, pady=2, padx=25)

var3 = IntVar()
C3 = Checkbutton(
    frame_alt_sol,
    text="Aynı gün",
    variable=var3,
    onvalue=1,
    offvalue=0,
    bg="#add8e6",
    font="Verdena 8"
)
C3.pack(anchor=NW, pady=2, padx=25)


def gonder():
    #part 4 de islem yapildi
    son_mesaj=""
    try:
        if var.get():
            if var.get()==1:
                son_mesaj+="Veriniz basariyla sisteme kaydedilmistir."
                tip=hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get()=="" else "Genel"
                tarih=hatirlatma_tarih_secici.get()
                mesaj=metin_alani.get("1.0","end")
                with open("hatirlatmalar.txt","w") as dosya:
                    dosya.write(
                        "{} kategorisinde,{} tarihine ve {} notuyla hatirlatma".format(tip,tarih,mesaj)

                    )
                    dosya.close()

            elif var.get()==2:
                son_mesaj+="E-posta yoluyla hatirlatma size ulasacaktir."
            messagebox.showinfo("Başarılı İşlem",son_mesaj)
        else:
            son_mesaj += "Gerekli alanlarin dolduruldugundan emin olun!"
            messagebox.showwarning("Yetersiz Bilgi",son_mesaj)
    except:
        son_mesaj += "İşlem başarısız oldu."
        messagebox.showerror("Başarısız işlem",son_mesaj)
    finally:
        master.destroy()
    return

# Sağ tarafta hatırlatma mesajı için başlık etiketi
Label(frame_alt_sag, background="#add8e6", text="Hatırlatma Mesajı", font="Verdena 15 bold").pack(
    padx=10, pady=10, anchor=NW
)

metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_configure("style", foreground="#bfbfbf", font=("Verdana", 7, "bold"))
metin_alani.pack()

karsilama_metni = "Mesajını buraya gir..."
metin_alani.insert(END, karsilama_metni, "style")

# Gönderme işlemi için bir buton
gonder_butonu = Button(frame_alt_sag, text="Gönder", command=gonder)
gonder_butonu.pack(anchor=S)
#sonlandir_butonu=Button(frame_alt_sag,text="Sonlandır",command=master.destroy)
# bu buton da islemi sonlandirma komutu master.destroyun islevini gosterir

#part 4

master.mainloop()


# video 43 yani ders 41
print("\n VİDEO 43 \n")
# bu videoda arayuz gelistirmesine devam ediliyor o yuzden islemleri ve notlari bunun yukarisinda yapiyorum
# part 2 olarak geciyor.

# video 44 yani ders 42
print("\n VİDEO 44 \n")
# part3 olarak geciyor

# video 45 yani ders 43
print("\n VİDEO 45 \n")
# part4 olarak geciyor



















