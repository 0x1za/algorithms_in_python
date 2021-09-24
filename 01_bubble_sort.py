def bubbleSort(arr):
    # This is the bubble sort algorithm implementation.

    ind = 0
    while ind < len(arr):
        x = 0
        while x < len(arr):
            if arr[x] > arr[ind]:
                temp = arr[ind]
                arr[ind] = arr[x]
                arr[x] = temp
            x+=1
        ind+=1

    return arr

print (bubbleSort([54,26,93,17,77,31,44,55,20]))