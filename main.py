import os
import time
import matplotlib.pyplot as plt
import pandas as pd

fayl_adi = "xercler.csv"

while True:
    print("1. Xərc əlavə et")
    print("2. Hesabata və Qrafikə bax")
    print("3. Çıxış")
    secim = input("Seçiminiz: ")

    if secim == "1":
        print("xerc elave etmeye daxil olduz! indi baslayaq! \n")
        kategoriya = input(
            "xercin kategoriyasini yazin \n meselen (yemek,neqliyat,...)\n"
        )
        kategoriyachecking = kategoriya.isalpha()
        if not kategoriyachecking:
            print("kategoriya normalda soznen ifade edilmeldir, sadece sozle islet\n")
            continue

        megleb = input("buna ne qeder megleb xerclemisiz? (manat) \n")
        meglebchecking = megleb.isdigit()
        if not meglebchecking:
            print(
                "megleb nece herf veya bele simbol ola biler? reqem ola biler ancaq yeniden \n"
            )
            continue

        mebleg = int(megleb)
        print(
            f"tebrikler qrafikde sizin {kategoriya} --buraya--> {megleb} ugurla qeyd edildi\n"
        )
        yeni_xerc = {"Kategoriya": [kategoriya], "Mebleg": [mebleg]}
        df = pd.DataFrame(yeni_xerc)

        if os.path.exists(fayl_adi):
            df.to_csv(fayl_adi, mode="a", header=False, index=False)
        else:
            df.to_csv(fayl_adi, mode="w", header=True, index=False)

        print(f"-> Məlumat '{fayl_adi}' faylına uğurla yazıldı!\n")

    elif secim == "2":
        print("Grahplara baxmaga daxil olduz! indi baslayaq! \n")

        if not os.path.exists(fayl_adi):
            print("siz hecbir data elave etmemisiz cenab\n")
            continue

        if os.path.exists(fayl_adi):
            oxunanfayl = pd.read_csv(fayl_adi)
            qruplasdirmaq = oxunanfayl.groupby("Kategoriya")["Mebleg"].sum().reset_index()

            plt.figure(figsize=(6, 6))
            plt.pie(
                qruplasdirmaq["Mebleg"],
                labels=qruplasdirmaq["Kategoriya"],
                autopct="%1.1f%%",
                startangle=140,
            )
            plt.title("Xərclərinizin Kateqoriyalara Görə Bölgüsü")
            plt.show()

            print("\n" + "=" * 40)
            print("--- QRAFİK GÖSTƏRİLDİ. ANA MENYUYA QAYIDILIR ---")
            print("=" * 40 + "\n")
            time.sleep(2)

    elif secim == "3":
        print("çıxış elədiz")
        break
    else:
        print(f"1-2-3 ile bir reqem secin, {secim} 1-2-3 den hecbiri deyil \n")
        continue
