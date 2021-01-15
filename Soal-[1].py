#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Minta Nama
while True:
    nama = input("Masukkan nama anda : ")
    if not nama.replace(' ','').isalpha():
        print("Bukan Huruf! Masukkan Huruf.")
        continue
    if nama.replace(' ','').isalpha():
        break
#Minta Umur
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Bukan Angka Bulat! Coba lagi.")
       continue
    else:
       return userInput 
       break


umur = inputNumber("Berapa usia anda? ")
#Minta Tinggi
def inputNumber(message):
  while True:
    try:
       userInput = float(input(message))       
    except ValueError:
       print("Bukan Angka! Coba lagi.")
       continue
    else:
       return userInput 
       break


tinggi = inputNumber("Berapa tinggi anda? ")
#Akhir
print("Data telah dimasukkan!")
print("Nama saya {} umur saya {} tahun tinggi saya {} cm".format(nama,umur,tinggi))
