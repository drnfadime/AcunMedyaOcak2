dersNotu = int(input("Sınav notunuzu giriniz:"))
if dersNotu >= 90 and dersNotu <= 100:
    print("Harf notunuz 'A' Aferiiinn böyle devam. ")
elif dersNotu >= 80 and dersNotu <= 89:
    print("Harf notunuz 'B' ")
elif dersNotu >= 70 and dersNotu <= 79:
    print("Harf notunuz 'C' ")
elif dersNotu >= 60 and dersNotu <= 69:
    print("Harf notunuz 'D' ")
elif dersNotu >= 0 and dersNotu <= 59:
    print("Harf notunuz 'F' Üzgünüm dersten kaldınız. ")
else:
    print("Geçersiz not girdiniz !")




