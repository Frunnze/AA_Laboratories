import time
import matplotlib.pyplot as plt
import pandas as pd
import math


# Implement the algorithm nr. 1.
def alg_1(c):
    c[0] = c[1] = False
    i, n = 2, len(c) - 1
    # Go through each cell of the array.
    while i <= n:
        if c[i]:
            j = 2 * i
            # Mark the multiples of the current number.
            while j <= n:
                c[j] = False
                j += i
        i += 1
    return c


# Implement the algorithm nr. 2.
def alg_2(c):
    c[0] = c[1] = False
    i, n = 2, len(c) - 1
    # Go trough each cell and mark the multiples.
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    return c


# Implement the algorithm nr. 3.
def alg_3(c):
    c[0] = c[1] = False
    i, n = 2, len(c) - 1
    # Go trough each cell.
    while i <= n:
        # Check if it is marked.
        if c[i]:
            j = i + 1
            # Find the multiples of the i and mark them.
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    return c


# Implement the algorithm nr. 4.
def alg_4(c):
    c[0] = c[1] = False
    i, n = 2, len(c) - 1
    # Check each cell.
    while i <= n:
        j = 2
        # Find if there are divisors for i.
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


# Implement the algorithm nr. 5.
def alg_5(c):
    c[0] = c[1] = False
    i, n = 2, len(c) - 1
    # Check each cell.
    while i <= n:
        j = 2
        # Find if there are divisors for i for 2 to strt(i).
        while j <= math.sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


alg_1_times = []
for i in range(1, 6):
    array = [True] * i * pow(10, 3)
    start = time.time()
    alg_1(array)
    end = time.time()
    ms = (end - start) * 1000
    alg_1_times.append(round(ms, 3))

alg_2_times = []
for i in range(1, 6):
    array = [True] * i * pow(10, 3)
    start = time.time()
    alg_2(array)
    end = time.time()
    ms = (end - start) * 1000
    alg_2_times.append(round(ms, 3))

alg_3_times = []
for i in range(1, 6):
    array = [True] * i * pow(10, 3)
    start = time.time()
    alg_3(array)
    end = time.time()
    ms = (end - start) * 1000
    alg_3_times.append(round(ms, 3))

alg_4_times = []
for i in range(1, 6):
    array = [True] * i * pow(10, 3)
    start = time.time()
    alg_4(array)
    end = time.time()
    ms = (end - start) * 1000
    alg_4_times.append(round(ms, 3))

alg_5_times = []
for i in range(1, 6):
    array = [True] * i * pow(10, 3)
    start = time.time()
    alg_5(array)
    end = time.time()
    ms = (end - start) * 1000
    alg_5_times.append(round(ms, 3))


# Creates the dataframe and prints the table
x = [i * pow(10, 3) for i in range(1, 6)]
row_name = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4', 'Algorithm 5']
data = [alg_1_times, alg_2_times, alg_3_times, alg_4_times, alg_5_times]
df = pd.DataFrame(data, columns=x, index=row_name)
pd.options.display.width = None
pd.options.display.max_columns = None
print(df)

# Plots the obtained above data.
plt.plot(x, alg_1_times, label='Algorithm 1')
plt.plot(x, alg_2_times, label='Algorithm 2')
plt.plot(x, alg_3_times, label='Algorithm 3')
plt.plot(x, alg_4_times, label='Algorithm 4')
plt.plot(x, alg_5_times, label='Algorithm 5')
plt.xlabel('Array size')
plt.ylabel('Time (ms)')
plt.legend(loc="upper left")
plt.show()