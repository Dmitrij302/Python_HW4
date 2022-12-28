# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 
# до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

import random

def randomList(k):

    arr = [] 

    for i in range(0, k+1):
        rnd_el = random.randint(0,101)
        #print(rnd_el)
        arr.append(rnd_el)

    return arr 



def polynomial(valueArr):


    acc = ''

    for i in valueArr:
          idx = valueArr.index(i) 

          acc += (f'{i}*{"x"}**{idx}')

          if idx < len(valueArr)-1:
              acc +=' + '



    acc = " 0 = " + acc 
    print( acc)   
    return acc

def createFile(valuePoly):
    with open('dz33.txt', 'a') as poly: 
        poly.write(valuePoly) 
        poly.write('\n')      


k = int(input('укажи степень многочлена : '))

valueArr = randomList(k)

valuePoly = polynomial(valueArr)

createFile(valuePoly)