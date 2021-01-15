#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Penghitungan ujian teori
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


teori = inputNumber("Penghitungan kelulusan nilai siswa\nMasukkan nilai ujian teori : ")
#Penghitungan ujian praktek
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


praktek = inputNumber("Masukkan nilai ujian praktek : ")
#Jumlah
#Kelulusan
if (teori+praktek)/2 >= 70 :
    print("Selamat, anda lulus!")
elif teori >= 70 and praktek < 70 :
    print("Anda harus mengulang ujian praktek.")
elif teori < 70 and praktek >= 70 :
    print ("Anda harus mengulang ujian teori.")
else :
    print ("Anda harus mengulang ujian teori dan praktek.")


# In[ ]:




