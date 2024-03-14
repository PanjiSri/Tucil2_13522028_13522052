import matplotlib.pyplot as plt
import numpy as np

def midpoint(x1,y1,x2,y2) :
    koordinat = []
    koordinat.append((x1+x2) / 2)
    koordinat.append((y1+y2) / 2)
    return koordinat

def list_midpoint(list_of_titik) :
    daftar_midpoint = []
    for i in range(len(list_of_titik)-1) :
        daftar_midpoint.append(midpoint(list_of_titik[i][0], list_of_titik[i][1], list_of_titik[i+1][0], list_of_titik[i+1][1]))
    return daftar_midpoint

def slicing(list, awal, akhir) :
    array = []
    for i in range (awal,akhir) :
        array.append(list[i])
    return array

def expandarray(array1, array2) :
    for i in range(len(array2)) :
        array1.append(array2[i])
    return array1

titikawal = []
titikakhir = []
titikbantu = []
titikbezier = []

n = int(input("Masukkan banyak garis: "))

for i in range(n+1) :
    titik = []
    if i == 0 :
        titik.append(float(input()))
        titik.append(float(input()))
        titikawal.append(titik)
        titikbantu.append(titik)
    elif i == n :
        titik.append(float(input()))
        titik.append(float(input()))
        titikakhir.append(titik)
        titikbantu.append(titik)
    else :
        titik.append(float(input()))
        titik.append(float(input()))
        titikbantu.append(titik)

for i in range(3) :
    titikdipakai = 0
    titikbantutemp = titikbantu
    titikbantu = []
    while (titikdipakai < len(titikbantutemp)-1) :
        temp = []
        awal = titikdipakai
        titikdipakai += n
        # print(titikbantutemp[awal:titikdipakai+1])
        kumpulantitik = slicing(titikbantutemp,awal,titikdipakai+1)
        kumpulantitik = list_midpoint(kumpulantitik)
        ulang = 0
        while len(kumpulantitik) > 1 :
            temp.insert(ulang,kumpulantitik[0])
            temp.insert(len(temp)-ulang,kumpulantitik[len(kumpulantitik)-1])
            ulang += 1
            kumpulantitik = list_midpoint(kumpulantitik)
        temp.insert(ulang,kumpulantitik[0])
        temp.append(titikbantutemp[titikdipakai])
        titikbantu = expandarray(titikbantu,temp)
    titikbantu.insert(0,titikawal[0])

print(titikbantu)

for i in range(0,len(titikbantu),n) :
    titikbezier.append(titikbantu[i])

print(titikbezier)