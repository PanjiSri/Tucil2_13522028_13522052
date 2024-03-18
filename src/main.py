from divide_and_conquer import *
from dnc import *
import time

def input_titik():
    titik = []
    for i in range(3):
        if i == 0:
            x = float(input(f"Masukkan koordinat x untuk titik kontrol awal: "))
            y = float(input(f"Masukkan koordinat y untuk titik kontrol awal: "))
        elif i == 1:
            x = float(input(f"Masukkan koordinat x untuk titik kontrol antara: "))
            y = float(input(f"Masukkan koordinat y untuk titik kontrol antara: "))
        else:
            x = float(input(f"Masukkan koordinat x untuk titik kontrol akhir: "))
            y = float(input(f"Masukkan koordinat y untuk titik kontrol akhir: "))
        titik.append([x, y])
    return titik


def pilihan():
    while True:

        print("Pilih opsi:")
        print("1. Divide and Conquer 2 Garis (3 Titik)")
        print("2. Divide and Conquer N Garis (N+1 Titik)")
        print("3. BruteForce")

        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan in ['1', '2', '3']:
            break 
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

    return pilihan



def main():
    algo = pilihan()
    print("")
    if algo == '1':
        titik = input_titik()
        iterasi = int(input("Masukkan jumlah iterasi: "))   
        arr = []
        total_iterasi_animasi = []
        mulai = time.time()
        kurva_bezier(titik[0], titik[1], titik[2], iterasi, arr, titik[0], titik[1], titik[2], total_iterasi_animasi)
        selesai = time.time()
        # print(len(total_iterasi_animasi))
        print("Waktu program berjalan: {:.2f} milliseconds".format((selesai- mulai - (len(total_iterasi_animasi) * 0.5)) * 1000))
        plt.show()

    elif algo == '2' or algo == '3':
        Ngaris_BForce(algo)



if __name__ == "__main__":
    main()