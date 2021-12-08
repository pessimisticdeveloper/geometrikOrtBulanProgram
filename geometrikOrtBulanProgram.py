#sıfır girene kadar girilen sayıların geomekrik ortalamasını bulan program

ort=1
n=-1
sayi=1
while(sayi !=0):
    ort=ort*sayi
    n=n+1
    sayi=int(input("sayi giriniz:"))
ort=pow(ort,1/n)

print("geometrik ortalama= %s"%ort)