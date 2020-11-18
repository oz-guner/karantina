hafta_ici=['Pazartesi', 'Sali', 'Carsamba', 'Persembe', 'Cuma']
hafta_sonu=['Cumartesi', 'Pazar']

gun=input("Gun giriniz: ")

if gun in hafta_ici:
    calisiyor=input("Calisiyor musunuz? (evet/hayir): ")
    if calisiyor=='evet':
        print("Calisabilirsiniz.")
    else:
        yasiniz = input("Yasinizi giriniz: ")
        if 20<=int(yasiniz)<65:
            print("Cikabilirsiniz.")
        else:
            saat = input("Saat giriniz: ")
            if 10<=round(float(saat))<16:
                print("Cikabilirsiniz.")
            else:
                print("Cikamazsiniz.")

elif gun in hafta_sonu:
    saat = input ("Saat giriniz: ")
    if 10<round(float(saat))<20:
        yasiniz = input("Yasinizi giriniz: ")
        if 20<int(yasiniz)<65:
            print("Cikabilirsiniz.")
        else:
            print("Cikamazsiniz.")
    else:
        print("Cikamazsiniz.")
else:
    print("Yanlis deger. Tekrar deneyin.")
