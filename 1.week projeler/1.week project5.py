    # STUDENT GRADING SYSTEM  Ogrenci notlandirma sistemi
print("LUTFEN OGRENCININ NOTUNU GIRINIZ: ")
for i in range(3):
    print(f"---{i+1}. ogrenci---")
    ogrenci_adi=input("ogrenci adini giriniz: ").strip().capitalize()
    notlar=[]
    for j in range(3):
        while True:
            try:
                not_degeri= int(input(f"{j+1}. Notu girin (0-100 arasi):"))
                if 0<= not_degeri <= 100 :
                    notlar.append(not_degeri)
                    break
                else:
                    print("lutfen notu 0 ile 100 arasinda girin.")
            except ValueError:
                print( "lutfen gecerli bir sayi giriniz.")
    ogrenciler[ogrenci_adi]=notlar

print("==== OGRENCI NOT ORTALAMALARI===")
en_yuksek_ortalama= -1
en_basarili_ogrenci= " "
for ad,notlar_listesi in ogrenciler.items():
    toplam_not= sum(notlar_listesi)
    ortalama=toplam_not / len(notlar_listesi)
    ortalama_yuvarlanmis= round(ortalama,2)
    print(f"{ad}: Notlar {notlar_listesi} -> ortalama: {ortalama_yuvarlanmis}")
    if ortalama > en_yuksek_ortalama:
        en_yuksek_ortalama = ortalama
        en_basarili_ogrenci = ad

print(f"En yuksek ortalamaya({round(en_yuksek_ortalam,2)}) sahip ogrenci: {en_basarili_ogrenci}")

