def yeni_kullanici():   #yeni kullanıcı eklemek için fonksiyon
    try:
        with open("BIL104 -projeKullanıcılar.txt", "r+") as f:  # dosyayı hem okuma hem yazma modunda açma
            # Fonksiyon kodu devam ediyor...
            satirlar = f.readlines()  #dosyanın mevcut satırlarını okuma
            son_satir = ""  #dosyadaki son satırı tutacak değişken atama
            while True:
                #dosyanın son satırı boş ise
                if satirlar[-1].strip() == "":        
                    satirlar.pop()   # dosyanın son satırını sil
                    f.seek(0, 0)     # dosya başına git
                    f.writelines(satirlar)  #yeni satırları yaz
                else:
                    son_satir = satirlar[-1]  # dosyanın son satırını değişkene ata
                    break
            yeni_id = int(son_satir.split(",")[0]) + 1    # yeni kullanıcı idsini ata
            ad = input("Adinizi giriniz: ")
            soyad = input("Soyadinizi giriniz: ")
            dogum_tarihi = input("Doğum tarihinizi (gün-ay-yil) girin: ")
            dogum_yeri = input("Doğum yerinizi giriniz: ")
            f.write(f"{yeni_id},{ad},{soyad},{dogum_tarihi},{dogum_yeri}\n")   #yeni kullanıcının bilgilerini al
    except IOError: 
        print("Dosya yazma hatasi!!!")   # hata varsa yazdır

def kullanici_getir():
    while True:
        try:
            id=input("Lutfen ID yi giriniz: ")
            with open("BIL104 -projeKullanıcılar.txt","r") as f:   # dosyayı okuma modunda açma
                icerik= f.readlines()    #dosyanın tüm içeriğini okuma
                for satir in icerik[1:]:    # ilk satırı atlama
                    satir=satir.replace("\n","").replace("\t","")  #satırdaki boşlukları boş karakterle değiştirme
                    if satir:   #satır boş değilse
                        satir_id =int(satir[0])    #satırın ilk karakterini id ye atıyoruz
                        if satir_id == int(id):    
                            print(satir) 
                            return
            print("Gecersiz id girdiniz.Tekrar deneyin.")
        except IOError :
            print("Dosya okuma hatasi!!!")      #hata varsa yazdır

def kullaniciAdi_sifre_uret():
    try:
        with open("BIL104 -projeKullanıcılar.txt", "r") as f:  # dosyayı okuma modunda açma
            satirlar = f.readlines()[1:]    # dosyanın içeriğini satırlara ayır ve ilk satırı atla
            kullaniciadiListesi = []
            sifreListesi = []
            for satir in satirlar:
                if len(satir) >=2:
                    satir = satir.lower().replace("\n", "").replace("\t", "").replace(" ", "").split(",")
                    adimlar_sonuc = adimlar(satir)  # adimlar() fonksiyonunu çağırma
                    kullaniciadiListesi.append(adimlar_sonuc[0])  # oluşturulan kullanıcı adını listeye ekle
                    sifreListesi.append(adimlar_sonuc[1])   # oluşturulan şifreyi listeye ekle

        with open("kullaniciAdi_sifre.txt", "a") as f:   # dosyayı ekleme modunda açma
            id = 0
            for i in range(len(kullaniciadiListesi)):
                id += 1    # id sayacı oluşturma
                kullanici_adi = str(kullaniciadiListesi[i])
                sifre = str(sifreListesi[i])   
                satir = str(id) + ", " + kullanici_adi + ", " + sifre + "\n"
                f.write(satir)    # dosyaya kullanıcı adını ve şifreyi yaz
    except IOError:
        print("Dosya okuma/yazma hatasi oluştu.\n")
import random
def adimlar(satir):
    kullaniciadiListesi = []
    sifreListesi = []
    if len(satir) >=2:    # eğer satırın içeriği 2 den fazlaysa devam et
        ad = satir[1]
        soyad = satir[2]
        dogum_tarihi = satir[3]
        dogum_yeri = satir[4]
        dogum_yeri = str(dogum_yeri).replace("-", "")
        dogum_tarihi = str(dogum_tarihi).split("-")
        gun = int(dogum_tarihi[0])
        ay = int(dogum_tarihi[1])
        yil = int(dogum_tarihi[2])

        Adim1 = ad[1] + ad[3]
        Adim2 = soyad[-3:].replace(soyad[-2], soyad[0])
        Adim3 = str(ay + gun) + str(yil)[-2:]

        kullanici_adi = Adim2 + Adim1 + Adim3
        kullaniciadiListesi.append(kullanici_adi)   # oluşturulan kullanıcı adını listeye ekleme

        ozel_karakter = ["*", "/", "!", "_", "(", ")", "&", "%", "+", "-", ".", ",", "<", ">"]

        yeni_karakter = random.choice(ozel_karakter)    # rastgele karakter seçimi
        adim1 = ad[0] + ad[-1].upper()
        adim2 = soyad[-2:].replace(soyad[-2], yeni_karakter)
        adim3 = str(yil)[-2:] + str(ay ** 2)
        adim4 = dogum_yeri[1:-2].title() + dogum_yeri[-2].upper()
        adim5 = random.randint(10, 99)

        sifre = adim4 + str(adim5) +adim1 + adim3 + str(adim2)

        sifreListesi.append(sifre)     # oluşturulan şifreyi listeye ekleme
        return kullaniciadiListesi, sifreListesi
def anlik_uret():    # kullanıcıdan alınan bilgilerle anlık üretme
    ad = input("Adiniz: ").lower()
    soyad = input("Soyadiniz: ").lower()
    dogum_tarihi = input("Doğum tarihini giriniz(gg-aa-yy): ").lower()
    dogum_yeri = input("Doğum yerinizi giriniz: ").lower()

    satir = str(0) + "," + ad + "," + soyad + "," + dogum_tarihi + "," + dogum_yeri    # oluşturlan satırın formatını ve elemanlarını belirleme
    satir = satir.replace(" ", "").split(",")    # satırdaki elemanları virgüle göre elemanlarına ayırma

    adimlar_sonuc = adimlar(satir)    # adimlar fonksiyonunu çağırma
    if adimlar_sonuc is None:
        print(" Kullanici adi ve şifre oluşturulamadi.")
    else:
        kullanici_adi, sifre = adimlar_sonuc
        print("Kullanici adi: ", kullanici_adi)
        print("Şifre: ", sifre)
        return
