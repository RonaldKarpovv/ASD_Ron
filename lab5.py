def sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key 


array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
sort(array)
print ("Отсортированный массив: ", array)

