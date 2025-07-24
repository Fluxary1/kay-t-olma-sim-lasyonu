import time

isim = input("İsminiz: ")
yas = int(input("Yaşınız: "))
eposta = input("E-posta adresiniz: ")
sifre = input("Şifreniz: ")
onay_kodu = 1000
while True:
    if yas < 18:
        print("Üzgünüz, 18 yaşından küçükler kayıt olamaz.")
        break
    print("Kayıt başarılı, hoş geldiniz", isim + ".")

    print("\nYapmak istediğiniz işlemi seçiniz:")
    print("1- Hesap Onaylama")
    print("2- Şifre Değiştirme")
    print("3- Çıkış")

    islem = int(input("Seçiminiz: "))
    if islem == 1:
        eposta_onay = input("E-posta adresinizi onaylamak için lütfen tekrar giriniz: ")
        if eposta_onay == eposta:
            print(eposta, "adresinize onay e-postası gönderildi.")
            print("Gönderilen e-postadaki kodu giriniz.")
            kod = int(input("Onay kodu: "))
            if kod == onay_kodu:
                print("E-posta onaylandı, hesabınız aktif.")
            else:
                print("Onay kodu yanlış, lütfen tekrar deneyin.")
        else:
            print("E-posta adresi eşleşmiyor, lütfen tekrar deneyin.")
    elif islem == 2:
        sifre_onay = input("Eski şifrenizi giriniz: ")
        if sifre_onay == sifre:
            yeni_sifre = input("Yeni şifrenizi giriniz: ")
            print("Şifreniz başarıyla değiştirildi.")
        else:
            print("Şifreler eşleşmiyor, lütfen daha sonra tekrar deneyin.")
            time.sleep(2.5)
            break
    elif islem == 3:
        print("Çıkış yapılıyor, kendinize iyi bakın.")
        time.sleep(0.5)
        break