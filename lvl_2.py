def insertion_sort(sortlist):
    for i in range(1, len(sortlist)):
        temp = sortlist[i]
        j = i - 1
        while j >= 0 and temp < sortlist[j]:
            sortlist[j + 1] = sortlist[j]
            j -= 1
        sortlist[j + 1] = temp
    return sortlist


new_list = [7, 3, 2, 35, 15, 7]
a = insertion_sort(new_list)

print(a)