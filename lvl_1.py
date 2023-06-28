def find_in_list(lst, num):
    low = 0
    high = len(lst) - 1
    res = False

    while low <= high and not res:
        middle = (low + high) // 2
        m = lst[middle]
        if m == num:
            res = True
            return res
        if m > num:
            high = middle - 1
        else:
            low = middle + 1
    return res



lst = [1, 7, 22, 48, 51, 69, 70, 88]
num = int(input("Введите число для поиска: "))
status = find_in_list(lst, num)
if status == True:
    print("Элемент найден!")
else:
    print("Элемент не найден!")

