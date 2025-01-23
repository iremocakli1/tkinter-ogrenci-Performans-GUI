import matplotlib.pyplot as plt
ders_isimleri = ['DERİN ÖĞRENME', 'VERİ MADENCİLİĞİ', 'YAPAY ZEKA']
def harf_notu(vize, final):
    sonuc = vize * 0.4 + final * 0.6
    if sonuc >= 90:
        return 'AA', 4.0
    elif sonuc >= 85:
        return 'BA', 3.5
    elif sonuc >= 80:
        return 'BB', 3.0
    elif sonuc >= 75:
        return 'CB', 2.5
    elif sonuc >= 70:
        return 'CC', 2.0
    elif sonuc >= 60:
        return 'DC', 1.5
    elif sonuc >= 50:
        return 'DD', 1.0
    elif sonuc >= 40:
        return 'FD', 0.5
    else:
        return 'FF', 0.0

ogrenci_renkleri = ['skyblue', 'pink', 'yellow']

ogrenciler = []
ogrenci_sayisi = int(input("Kaç öğrenci var? "))
for i in range(ogrenci_sayisi):
    ogrenci_adi = input(f"{i+1}. öğrencinin adını girin: ")
    ogrenci_bilgisi = {'isim': ogrenci_adi, 'notlar': []}
    
    for ders in ders_isimleri:
        while True:
            try:
                vize = float(input(f"{ogrenci_adi} için {ders} dersinin vize notunu girin (0-100): "))
                if not (0 <= vize <= 100):
                    print("Vize notu 0 ile 100 arasında olmalıdır.")
                    continue
                final = float(input(f"{ogrenci_adi} için {ders} dersinin final notunu girin (0-100): "))
                if not (0 <= final <= 100):
                    print("Final notu 0 ile 100 arasında olmalıdır.")
                    continue
                harf, puan = harf_notu(vize, final)
                ogrenci_bilgisi['notlar'].append({'ders': ders, 'vize': vize, 'final': final, 'harf': harf, 'puan': puan})
                break
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
    
    ogrenciler.append(ogrenci_bilgisi)

plt.figure(figsize=(10, 6))

for idx, ogrenci in enumerate(ogrenciler):
    ders_notlari = [not_bilgisi['puan'] for not_bilgisi in ogrenci['notlar']]
    plt.plot(ders_isimleri, ders_notlari, marker='o', label=ogrenci['isim'], color=ogrenci_renkleri[idx])


plt.xlabel('Dersler', fontsize=12)
plt.ylabel('Not Ortalaması (4.0 Üzerinden)', fontsize=12)
plt.title('Öğrencilerin Ders Performansları', fontsize=14)
plt.ylim(0, 4.0)
plt.legend(title="Öğrenciler")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


plt.show()
