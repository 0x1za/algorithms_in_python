# def selectionSort(arr):
#     index = 0
#     while index < len(arr[index:]):
#         smallest = arr[index]
#         inner_index = 0
#         while inner_index < len(arr[index:]):
#             if arr[inner_index] < smallest:
#                 temp = arr[index]
#                 temp_index = inner_index
#                 smallest = arr[inner_index]
#             inner_index+=1
#         arr[index] = smallest
#         arr[temp_index] = temp
#         index+=1
#
#     print (arr)
#
# selectionSort([54,26,93,17,77,31,44,55,20])