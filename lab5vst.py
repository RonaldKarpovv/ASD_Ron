import random


def insertion_sort(nums): 
    for i in range(1, len(nums)): # Рассматриваем массив от 2 элемента
        insert = nums[i] # Текущий элемент
        # Перемещаем элементы nums [0… i-1], которые больше значения, на одну позицию впереди их текущей позиции.
        j = i - 1 
        while j >= 0 and nums[j] > insert: # Проверяем j и jый элемент сравниваем с текущим
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = insert 

n = 10 
mas = [random.randint(1, 100) for i in range(n)]
insertion_sort(mas)
print(mas)
