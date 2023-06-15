import os
os.system("cls")
kitap_liste = list()
menu = ("""

1) Kitap Ekle
2) Kitap Çıkar
3) Kitapları Listele
0) Çıkış





""")

def KitapEkle(liste,kitap):
    liste += [kitap]
    print("{} Adlı Kitap Başarıyla Eklendi\a\1 ".format(kitap))
    input("Ana Menüye Dönmek İçin Enter'a Tıklayınız. : ")

def KitapCikar():
    pass

def listele(kitap_liste):
    for a in kitap_liste:
        print("Kitap Adı => {}\a".format(a))
    input("Ana Menüye Dönmek İçin Enter'a Tıklayınız. : ")

def cikis():
    quit()

while True:
    print(menu)
    secim = input("Yapmak İstediğiniz İşlemin Numarasını Giriniz. : ")

    if secim == "1":
        kitap_adi = input("Eklemek İstediğiniz Kitabın İsmini Giriniz. : ")
        KitapEkle(kitap_liste,kitap_adi)

    elif secim == "2":
        KitapCikar()

    elif secim == "3":
        listele(kitap_liste)

    elif secim == "0":
        print("Güle Güle \3\a\a")
        quit()

    else:
        print("Geçersiz Seçim")
        input("Ana Menüye Dönmek İçin Enter'a Tıklayınız. : ")

