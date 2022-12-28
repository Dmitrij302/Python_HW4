# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def multi(numList):
    numList = int(numList)
    #print(numList, type(numList))

    # создан список из чисел (от 1 до numList+1)
    numArr = [i for i in range(1, numList+1)]
    #print(numArr, type(numArr))


    arrPrime = []
    for j in numArr:
        if j > 1:
            for n in range(2, j):
                if(j%n) == 0:
                    break
            else:
                #print(f'Простое число: {j}')
                arrPrime.append(j)

    #print(arrPrime) 

    return arrPrime

def addListPrime(numMulti, num):
    num = int(num)
    print(f'На входе список из простых чисел {numMulti}, тип: {type( numMulti[0] )}\n'
          f'Интервал списка: от 1 до {num}, тип: {type(num)} ')

    arrListPrime = []
    for i in numMulti:

        while(num % i == 0):
            num = num / i
            print(f'num={num} , i ={i} ')
            arrListPrime.append(i)
        else:
            continue

    print(f'Простые множители числа {num}: {arrListPrime}')


num = input('Введи число для проверки на простые множители: ')

numMulti = multi(num)

addListPrime(numMulti, num)