def factorial (num) :
    angka = 1
    for i in range(1,num + 1) :
        angka *= i
    return angka

def combination (leftnum, rightnum) :
    return round(factorial(leftnum) / (factorial(rightnum) * factorial(leftnum-rightnum)))

def bexierbruteforce(array, t) :
    # Array = banyak titik
    titik = []
    garis = len(array)-1 # jumlah garis
    x = 0
    y = 0
    for i in range(garis+1) :
        x += round(combination(garis,i) * ((1-t)**(garis-i)) * (t**i) * array[i][0], 3)
        y += round(combination(garis,i) * ((1-t)**(garis-i)) * (t**i) * array[i][1], 3)
    titik.append(round(x,3))
    titik.append(round(y,3))
    return titik
