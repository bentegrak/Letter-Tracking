def bilgi():
    Ad="Furkan"
    Soyad="Teğrak"
    Numara="211213082"
    Not="Hello World!"

    print("Adı:",Ad)
    print("Soyadı:",Soyad)
    print("Numarası:",Numara)
    print("Notu:",Not)

def harf_mi(karakter):
    if karakter.isalpha():
        print(f"'{karakter}' bir harftir.")
        return True
    else:
        print(f"'{karakter}' bir harf değildir.")
        return False

def kucuge_cevir(harf):
    if harf.isupper():
        harf2=harf.lower()
        print("Girilen Harf:",harf)
        print("Cevrilen Harf:",harf2)
    else:
        print("Girilen Harf:",harf)

def harf_siklik_metni_hesapla(metin):
    harf_sayilari = {}
    toplam_harf_sayisi = 0

    # metindeki harf sayılarını hesapla
    for harf in metin:
        if harf.isalpha():
            harf = harf.lower()  # büyük-küçük harf duyarlılığını
            harf_sayilari[harf] = harf_sayilari.get(harf, 0) + 1
            toplam_harf_sayisi += 1

    # harf sıklıklarını yüzdelerle hesapla
    harf_sikliklari = {harf: (sayi / toplam_harf_sayisi * 100) for harf, sayi in harf_sayilari.items()}

    return harf_sayilari, harf_sikliklari


bilgi()
print("-----------------------------------------------------------")
harf_mi('0')
print("-----------------------------------------------------------")
kucuge_cevir('a')
print("-----------------------------------------------------------")
harf_sayilari, harf_siklikleri = harf_siklik_metni_hesapla('vécudesдочериeinsamerdifférentsAJSAHVCasjhvvdsj')

    # harf sayılarını ve sıklıklarını ekrana yazdır
print("Harf Sayıları:")
for harf, sayi in harf_sayilari.items():
    print(f"{harf}: {sayi}")

print("\nHarf Sıklıkları:")
for harf, yuzde in harf_siklikleri.items():
    print(f"{harf}: %{yuzde:.2f}")









