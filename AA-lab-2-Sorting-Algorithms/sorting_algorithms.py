import time
import matplotlib.pyplot as plt
import pandas as pd


# Implement Quicksort algorithm.
def quick_sort(array, low, high):
    if low < high:
        # Pick a pivot.
        pivot = array[high]

        # Point towards the first great element in the array.
        i = low - 1

        # Compare each element with the pivot.
        for j in range(low, high):
            if array[j] < pivot:
                # Change the first great element with the one smaller than the pivot.
                i += 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

        # Bring the pivot to its place.
        i += 1
        temp = array[i]
        array[i] = pivot
        array[high] = temp

        # Sort the left partition (smaller than pivot).
        quick_sort(array, low, i - 1)

        # Sort the right partition (greater than pivot).
        quick_sort(array, i + 1, high)
    return array


def merge_sort(array):
    if len(array) > 1:
        # Find the half of the array.
        half = len(array) // 2

        # Create the new arrays.
        left_array = array[:half]
        right_array = array[half:]

        # Sort the arrays.
        merge_sort(left_array)
        merge_sort(right_array)

        # Compare each element of the two arrays and insert the values to the array.
        l_len, r_len = len(left_array), len(right_array)
        i = j = item = 0
        while i < l_len and j < r_len:
            if left_array[i] < right_array[j]:
                array[item] = left_array[i]
                i += 1
            else:
                array[item] = right_array[j]
                j += 1
            item += 1

        # Insert into the main array the remaining elements of an array.
        while i < l_len:
            array[item] = left_array[i]
            i += 1
            item += 1

        while j < r_len:
            array[item] = right_array[j]
            j += 1
            item += 1
    return array


# Implement the Heapsort.
def heapify(array, n, i):
    # Initialize largest as root and find the right and left children.
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Find if left child of root exists and is greater than root
    if l < n and array[i] < array[l]:
        largest = l

    # Find if right child of root exists and is greater than root
    if r < n and array[largest] < array[r]:
        largest = r

    # Change root, if necessary.
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):
    # Find the length on the array.
    n = len(array)

    # Make the maxheap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Extract elements one by one and swap them.
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array


# Implement counting sort.
def counting_sort(array):
    # Create a temp array and initialize it.
    temp = [0]*(max(array) + 1)

    # Go through each item and mark it in the temp array.
    for number in array:
        temp[number] += 1

    # Create the final array by adding the indexes of the temp.
    sorted_array = []
    for index, value in enumerate(temp):
        if value != 0:
            sorted_array += [index] * value

    return sorted_array


with open('lists.txt', 'r') as file:
    lines = file.readlines()

quick_sort_time = []
for line in lines:
    numbers = [int(num) for num in line.split()]
    start = time.time()
    quick_sort(numbers, 0, len(numbers) - 1)
    end = time.time()
    ms = (end - start) * 1000
    quick_sort_time.append(round(ms, 3))

merge_sort_time = []
for line in lines:
    numbers = [int(num) for num in line.split()]
    start = time.time()
    merge_sort(numbers)
    end = time.time()
    ms = (end - start) * 1000
    merge_sort_time.append(round(ms, 3))

heap_sort_time = []
for line in lines:
    numbers = [int(num) for num in line.split()]
    start = time.time()
    heap_sort(numbers)
    end = time.time()
    ms = (end - start) * 1000
    heap_sort_time.append(round(ms, 3))

counting_time = []
for line in lines:
    numbers = [int(num) for num in line.split()]
    start = time.time()
    counting_sort(numbers)
    end = time.time()
    ms = (end - start) * 1000
    counting_time.append(round(ms, 3))

# Creates the dataframe and prints the table
x = [5000*i for i in range(1, 11)]
row_name = ['Quicksort', 'Mergesort', 'Heapsort', 'CountingSort']
data = [quick_sort_time, merge_sort_time, heap_sort_time, counting_time]
df = pd.DataFrame(data, columns=x, index=row_name)
pd.options.display.width = None
pd.options.display.max_columns = None
print(df)

# Plots the obtained above data.
plt.plot(x, quick_sort_time, label='Quicksort')
plt.plot(x, merge_sort_time, label='Mergesort')
plt.plot(x, heap_sort_time, label='Heapsort')
plt.plot(x, counting_time, label='CountingSort')
plt.xlabel('List size')
plt.ylabel('Time (ms)')
plt.legend(loc="upper left")
# plt.scatter(x, counting_time)
plt.show()