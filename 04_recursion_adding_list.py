# Adding numbers in a list recursively.
def add(array):
    # Define my base case
    i = len(array) - 1
    if len(array) == 1:
        return array[0]
    # Define the recursive step
    else:
        return array[i] + add(array[:i])

print (add([1, 2, 3]))