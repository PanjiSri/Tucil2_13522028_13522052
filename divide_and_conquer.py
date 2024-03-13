import matplotlib.pyplot as plt


def titik_tengah(titik_awal, titik_akhir):

    hasil = []
    x_tengah = (titik_awal[0] + titik_akhir[0]) / 2
    y_tengah = (titik_awal[1] + titik_akhir[1]) / 2
    hasil.append(x_tengah)
    hasil.append(y_tengah)

    return hasil


def kurva_bezier(titik_1, titik_2, titik_3, iterasi, arr):

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
    else:
        tengah_1 = titik_tengah(titik_1, titik_2)
        tengah_2 = titik_tengah(titik_2, titik_3)
        tengah_dari_tengah = titik_tengah(tengah_1,tengah_2)

        #ini buat bagian kiri
        kurva_bezier(titik_1, tengah_1, tengah_dari_tengah, iterasi-1, arr)

        #ini buat bagian kanan
        kurva_bezier(tengah_dari_tengah,tengah_2, titik_3, iterasi-1, arr)



def plot_kurva(arr):
    titik_x = []
    titik_y = []
    for elemen in arr:
        titik_x.append(elemen[0])
        titik_y.append(elemen[1])

    # print(titik_x)
    # print(titik_y)
    plt.plot(titik_x, titik_y, linestyle="-")
    plt.show()



