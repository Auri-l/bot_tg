import random

array = []
for i in range(0,100):
    array.append(int(random.random()*200))
array.sort()

print(array)

def poisk_1(x):
    chislo = x

    for chislo in array:
        if chislo == x:
            print(f'Число {x} есть(поиск_1)')




def poisk_2(x):
    index_array = []

    for i in range(0,len(array),5):
        index_array.append(array[i])
    for i in index_array:
        if i>=x:
            index = index_array.index(i)
            mass_index_1 = index
            if(index_array[index-1])<=x:
                mass_index_2 = index-1
                for j in range ((mass_index_1-1)*5,mass_index_1*5):
                    if array[j] == x:
                        print(f"Число {x} , Id {j} (поиск_2)")




def poisk_3(x):
    value = x

    mid = len(array) // 2
    low = 0
    high = len(array) - 1

    while array[mid] != value and low <= high:
        if value > array[mid]:
            low = mid+1
        else:
            high = mid-1
        mid = (low + high) // 2

    if low > high:
        print(f'Числа {x} нет(поиск_3)')
    else:
        print('Id', mid, ',' f' Число {x} (поиск_3)')

poisk_1(85)
poisk_2(85)
poisk_3(85)