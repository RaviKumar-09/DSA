#The Bubble Sort algorithm can be improved a little bit more.

#Imagine that the array is almost sorted already, with the lowest numbers at the start, like this for example:

my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
      if my_array[j] > my_array[j+1]:
        my_array[j], my_array[j+1] = my_array[j+1],my_array[j]
        swapped = True
    if not swapped:
      break
print("Sorted array:", my_array)
 