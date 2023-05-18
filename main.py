#"islemler" dosyasından gerekli fonksiyonları çağırıyoruz
from islemler import yeni_kullanici, kullanici_getir, kullaniciAdi_sifre_uret , anlik_uret
#menuyu ekrana yazdıran fonksiyon
def menu_goruntule():
    print("\n1.Yeni kullanici bilgileri girme")
    print("2.Kullanici bilgilerini ekrana yazdirma")
    print("3.Dosyadaki bilgilerle kullanici adi ve sifre üret")
    print("4.Anlik girdiyle kullanici adi ve sifre üret ")
#ana fonksiyon
def main():
        while True:
            menu_goruntule()  #menüyü ekrana yazdırma
            secim=input("Seciminizi giriniz:")
#kullanıcı seçimine göre fonskiyon çağırma
            if secim=="1":
                yeni_kullanici()
            elif secim=="2":
                kullanici_getir()
            elif secim=="3":
                kullaniciAdi_sifre_uret()
            elif secim=="4":
                anlik_uret()
            else:
                print("Gecersiz secim yaptiniz!\n")
main()  # ana fonskiyonu çağırma islemi
