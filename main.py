from divide_and_conquer import *


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

def main():
    titik = input_titik()
    iterasi = int(input("Masukkan jumlah iterasi: "))   
    arr = []
    kurva_bezier(titik[0], titik[1], titik[2], iterasi, arr)
    plt.title("Kurva Bezier")
    plot_kurva(arr)

if __name__ == "__main__":
    main()