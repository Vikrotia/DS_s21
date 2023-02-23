def bubble_sort(lst):
    N = len(lst)
    for i in range(N - 1):
        for j in range(N - i -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

# Запуск
lst = [9,8,7,6,5,4,3,2,1]
lst1 = bubble_sort(lst)
print(lst1)