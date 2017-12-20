a = [1, 2, 3, 4]
b = [4, 2, 3, 1]
c = [4, 3, 2, 1]

def sort_in_place(array):
    j = 0
    for i in range(len(array)):
        if array[i] < array[j]:
            j, i = i, j
            array[j], array[i] = array[i], array[j]

