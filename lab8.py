 def sort(array) :
    length = len(str(max(array)))
    rang = 10
    for i in range(length):
        arr = [[] for k in range(rang)]
        for x in array:
            figure = x // 10**i % 10
            arr[figure].append(x)
        array = []
        for k in range(rang):
            array = array + arr[k]
    return array
array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
array=sort(array)
print("Отсортированный массив: ", array)
