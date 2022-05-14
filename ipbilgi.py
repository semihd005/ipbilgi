#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
#tool yerine kendi toolunuzun ismini yazın.
os.system("figlet Seonly ip sorgu")

print("""
Hos Geldiniz. Islemler:

1- Hizli Tarama
2- Servis ve Versiyon Bilgisi

""")

no = input("Bir Islem Seciniz: ")

if(no == "1"): #eğer no = 1 ise asagidaki islemleri yap.
    ip = input("Hedef IP: ") #ip değerini girilecek ip adresine esitliyoruz.
    os.system("nmap " + ip) #terminalden nmap'de calisacak komutu yaziyoruz.
elif(no == "2"):
    ip = input("Hedef IP: ")
    os.system("nmap -sS -sV " + ip)
else:
    print("Hatali Secim.")
