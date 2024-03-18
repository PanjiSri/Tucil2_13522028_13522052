import matplotlib.pyplot as plt
import bruteforce
import time

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

def animasi(array,xawal,yawal) :
    plt.clf()
    plt.scatter([i[0] for i in array],[i[1] for i in array])
    plt.title("Kurva Bezier")
    plt.plot([i[0] for i in array],[i[1] for i in array], marker = 'o', label = 'kurva bezier')
    plt.plot(xawal, yawal, marker = 'o', label = 'titik kontrol')
    plt.legend()
    plt.pause(0.5)


def Ngaris_BForce(algo):
    titikawal = [] #Titik P0
    titikakhir = [] #Titik Pn
    titikbantu = [] #Semua titik kontrol + titik kurva
    titikbezier = [] # Titik kurva
    xawal = [] # X titik yang masuk di awal
    yawal = [] # Y titik yang masuk di awal

    n = int(input("Masukkan banyak titik: "))
    garis = n-1

    for i in range(n) :
        titik = []
        if i == 0 :
            titik.append(float(input("input x: ")))
            xawal.append(titik[-1])
            titik.append(float(input("input y: ")))
            yawal.append(titik[-1])
            titikawal.append(titik)
            titikbantu.append(titik)
        elif i == n-1 :
            titik.append(float(input("input x: ")))
            xawal.append(titik[-1])
            titik.append(float(input("input y: ")))
            yawal.append(titik[-1])
            titikakhir.append(titik)
            titikbantu.append(titik)
        else :
            titik.append(float(input("input x: ")))
            xawal.append(titik[-1])
            titik.append(float(input("input y: ")))
            yawal.append(titik[-1])
            titikbantu.append(titik)
            
    if algo == '3' :
        x = []
        x.append(titikawal[0][0])
        y = []
        y.append(titikawal[0][1])
        iterasi = int(input("Masukkan iterasi: "))
        mulai = time.time()
        iterasi = 2**iterasi - 1
        t = 1/iterasi
        while t < 1 :
            titik = bruteforce.bexierbruteforce(titikbantu, t)
            x.append(titik[0])
            y.append(titik[1])
            t += 1/iterasi
        akhir = time.time()

    if algo == '2':
        total_iterasi_animasi = 0
        iterasi = int(input("Masukkan iterasi: "))
        pakai_animasi = input("Ingin menggunakan animasi (Y/N): ")
        mulai = time.time()     
        for i in range(iterasi) :
            titikbezier = []
            titikdipakai = 0
            titikbantutemp = titikbantu
            titikbantu = []
            while (titikdipakai < len(titikbantutemp)-1) :
                temp = []
                awal = titikdipakai
                titikdipakai += garis
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
            if pakai_animasi == 'Y' :
                for i in range(0, len(titikbantu), garis) :
                    titikbezier.append(titikbantu[i])
                animasi(titikbezier,xawal,yawal)
                total_iterasi_animasi += 1
            else :
                for i in range(0, len(titikbantu), garis) :
                    titikbezier.append(titikbantu[i])

        x = []
        y = []
        for i in range(len(titikbezier)) :
            x.append(titikbezier[i][0])
            y.append(titikbezier[i][1])
        akhir = time.time()

    plt.clf()
    plt.title("Kurva Bezier")
    plt.plot(x,y, marker = 'o', label = 'kurva bezier')
    plt.scatter(x,y)
    plt.plot(xawal, yawal, marker = 'o', label = 'titik kontrol')
    plt.legend()
    if algo == '2':
        #Mengalami pengurangan karena ada galat ketika menampilkan animasi
        runtime = (akhir - mulai - (total_iterasi_animasi * 0.5)) * 1000
    else:
        runtime = (akhir - mulai) * 1000
    print("Waktu program berjalan: {:.2f} milliseconds".format(runtime))
    plt.show()