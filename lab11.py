def sort(array):
    if len(array)> 1:
        pivot=array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (sort(smlr_lst) + equal_lst + sort(grtr_lst))
    else:
        return array

array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
array=sort(array)
print("Отсортированный массив: ", array)
