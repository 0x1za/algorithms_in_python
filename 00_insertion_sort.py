def insertion(array):
    for i in range(1, len(array)):
        j = i -1
        while array[j] > array[j+1] and j >= 0:
            array[j], array[j+1] = array[j+1], array[j]
            j-=1
    return array

print (insertion([7, 8, 5, 4, 9, 2]))