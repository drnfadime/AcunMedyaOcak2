yas = int(input("Lütfen yaşınızı giriniz:"))
if yas >= 0 and yas <= 12:
    print("Yaş grubunuz 'Çocuk' ")
elif yas >=13 and yas <= 19:
    print("Yaş grubunuz 'Genç' ")
elif yas >= 20 and yas <= 59:
    print("Yaş grubunuz 'Yetişkin' ")
elif yas >= 60:
    print("Yaş grubunuz 'Yaşlı' ")
else:
    print("Geçersiz giriş !")