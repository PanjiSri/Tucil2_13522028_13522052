import matplotlib.pyplot as plt
import bruteforce

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

def animasi(array) :
    plt.clf()
    plt.scatter([i[0] for i in array],[i[1] for i in array])
    plt.plot([i[0] for i in array],[i[1] for i in array])
    plt.pause(2)

titikawal = [] #Titik P0
titikakhir = [] #Titik Pn
titikbantu = [] #Semua titik kontrol + titik kurva
titikbezier = [] # Titik kurva
xawal = [] # X titik yang masuk di awal
yawal = [] # Y titik yang masuk di awal

n = int(input("Masukkan banyak garis: "))
algo = int(input("Masukkan algoritma: "))


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

if algo == 1 :
    x = []
    x.append(titikawal[0][0])
    y = []
    y.append(titikawal[0][1])
    iterasi = int(input("Masukkan iterasi: "))
    iterasi = 2**iterasi - 1
    t = 1/iterasi
    while t < 1 :
        titik = bruteforce.bexierbruteforce(titikbantu, t)
        x.append(titik[0])
        y.append(titik[1])
        t += 1/iterasi

if algo == 2:
    iterasi = int(input("Masukkan iterasi: "))
    for i in range(iterasi) :
        titikbezier = []
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
        for i in range(0, len(titikbantu), n) :
            titikbezier.append(titikbantu[i])
        animasi(titikbezier)

    x = []
    y = []
    for i in range(len(titikbezier)) :
        x.append(titikbezier[i][0])
        y.append(titikbezier[i][1])

plt.clf()
plt.plot(x,y)
plt.scatter(x,y)
plt.show()