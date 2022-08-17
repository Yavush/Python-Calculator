
def toplama(sayi1,sayi2):
    return sayi1+sayi2
def cikarma(sayi1,sayi2):
    return sayi1-sayi2
def carpma(sayi1,sayi2):
    return sayi1*sayi2
def bolme(sayi1,sayi2):
    return sayi1/sayi2

islem = int(input("Yapmak istediğiniz işlemi seçiniz \n"
              "1-Toplama \n"
              "2-Çıkarma \n"
              "3-Çarpma \n"
              "4-Bölme "
              ))
sayi1 = int(input("Birinci sayı Giriniz : "))
sayi2 = int(input("İkinci sayıyı Giriniz : "))

if islem == 1:
  print(sayi1 , "+" , sayi2 , "=" ,  toplama(sayi1,sayi2))
if islem == 2:
  print(sayi1, "-", sayi2, "=", cikarma(sayi1,sayi2))
if islem == 3:
  print(sayi1, "*", sayi2, "=", carpma(sayi1,sayi2))
if islem == 4:
  print(sayi1, "/", sayi2, "=", bolme(sayi1,sayi2))
else:
    print("Geçersiz bir sayı girdiniz")