# 1. Вычислить число c заданной точностью d.

import math 
from decimal import Decimal 

def calcLevel(d):

    arr1 = [0 for i in range( int(d) )]
    #print(arr1, type(arr1[0])) # ---> [0, 0, 0, 0] <class 'int'>

    numer = ''
    for i in arr1:
        numer +=str(i)
    numer = '1.'+numer
    #print(numer, type (numer))

    return numer

def calcPi(numlevel):

    num = Decimal( math.pi)
    print(f'Число π (Без точности в кол-ве знаков): {num}')

    numOut = num.quantize( Decimal(numlevel) )
    print(f'Число π (C точностью до {len(numlevel)-2} знаков): {numOut}')



d = input("Укажите точность (кол-во знаков после запятой ) : ")
numlevel = calcLevel(d)

calcPi(numlevel)