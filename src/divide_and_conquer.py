import matplotlib.pyplot as plt

def titik_tengah(titik_awal, titik_akhir):
    hasil = []
    x_tengah = (titik_awal[0] + titik_akhir[0]) / 2
    y_tengah = (titik_awal[1] + titik_akhir[1]) / 2
    hasil.append(x_tengah)
    hasil.append(y_tengah)
    return hasil

def kurva_bezier(titik_1, titik_2, titik_3, iterasi, arr, kontrol1, kontrol2, kontrol3, total_iterasi_animasi, pakai_animasi):
    if iterasi == 1:
        tengah_1 = titik_tengah(titik_1, titik_2)
        tengah_2 = titik_tengah(titik_2, titik_3)
        tengah_dari_tengah = titik_tengah(tengah_1, tengah_2)

        if arr == []:
            arr.append(titik_1)
            arr.append(tengah_dari_tengah)
            arr.append(titik_3)
        else:
            if arr[-1] == titik_1:
                arr.append(tengah_dari_tengah)
                arr.append(titik_3)
            else:
                arr.append(titik_1)
                arr.append(tengah_dari_tengah)
                arr.append(titik_3)
        if pakai_animasi == 'Y':
            plt.clf()
            plot_kontrol(kontrol1, kontrol2, kontrol3)
            total_iterasi_animasi.append(1)
            plot_kurva(arr)   
    else:
        tengah_1 = titik_tengah(titik_1, titik_2)
        tengah_2 = titik_tengah(titik_2, titik_3)
        tengah_dari_tengah = titik_tengah(tengah_1,tengah_2)

        #ini buat bagian kiri
        kurva_bezier(titik_1, tengah_1, tengah_dari_tengah, iterasi-1, arr, kontrol1, kontrol2, kontrol3, total_iterasi_animasi, pakai_animasi)

        #ini buat bagian kanan
        kurva_bezier(tengah_dari_tengah,tengah_2, titik_3, iterasi-1, arr, kontrol1, kontrol2, kontrol3, total_iterasi_animasi, pakai_animasi)

def plot_kurva(arr):
    titik_x = []
    titik_y = []
    for elemen in arr:
        titik_x.append(elemen[0])
        titik_y.append(elemen[1])
    plt.title("Kurva Bezier")
    plt.plot(titik_x, titik_y, marker = 'o', label = 'kurva bezier')
    plt.legend()
    plt.pause(0.5)

def plot_kurva_no_animasi(arr):
    titik_x = []
    titik_y = []
    for elemen in arr:
        titik_x.append(elemen[0])
        titik_y.append(elemen[1])
    plt.title("Kurva Bezier")
    plt.plot(titik_x, titik_y, marker = 'o', label = 'kurva bezier')
    plt.legend()
    


def plot_kontrol(titik_awal, titik_tengah, titik_akhir):
    x_kontrol = [titik_awal[0], titik_tengah[0], titik_akhir[0]]
    y_kontrol = [titik_awal[1], titik_tengah[1], titik_akhir[1]]        
    plt.plot(x_kontrol, y_kontrol, linestyle="-", marker = 'o', label = 'titik kontrol')
