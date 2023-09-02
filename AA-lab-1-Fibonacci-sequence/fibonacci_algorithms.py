import math
from decimal import Decimal, getcontext
import numpy as np
import time
import pandas as pd
import decimal
import matplotlib.pyplot as plt


# Implementing the Recursive method.
def recursive_fib(n):
    if n < 2:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


# Implementing the Dynamic method.
def dynamic_fib(n):
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[n]


# Implementing the Iterative method.
def iteration_fib(n):
    if n <= 1:
        return n
    f0, f1 = 0, 1
    for i in range(2, n + 1):
        f0, f1 = f1, f0 + f1
    return f1


# Implementing the Binet method.
def binet_fib(n):
    getcontext().prec = 1000
    p = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
    m = (Decimal(1) - Decimal(5).sqrt()) / Decimal(2)
    return int((p**n - m**n) / Decimal(5).sqrt())


# Implementing the Matrix method.
def multiply(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def power(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        B = power(A, n//2)
        return multiply(B, B)
    else:
        B = power(A, (n-1)//2)
        return multiply(multiply(B, B), A)

def matrix_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    A = [[1, 1], [1, 0]]
    A = power(A, n-1)
    return A[0][0]


# Implementing the Fast Doubling method.
def fast_double_fib(index):
    MOD = 10000000
    if index == 0:
        return (0, 1)
    a, b = fast_double_fib(index // 2)
    c = 2 * b - a
    if c < 0:
        c += MOD
    c = (a * c) % MOD
    d = (a * a + b * b) % MOD
    if index % 2 == 0:
        return (c, d)
    else:
        return (d, c + d)

def double_fib(index):
    return fast_double_fib(index)[0]


# Determines the input seqeunces to be used.
first_sequence = [4,8,11,13,15,18,20,23,25,28,30,33,36,37]
second_sequence = [631,794,1000,1259,1585,1995,2512,3162,3981,5012,6310,7943,10000,12589]
used_sequence = second_sequence

# Finds the run time of the Recursive method.
# recursion_time = []
# for num in first_sequence:
#     start = time.time()
#     recursive_fib(num)
#     end = time.time()
#     ms = (end - start) * 1000
#     recursion_time.append(round(ms, 3))
# print('\n')

# Finds the run time of the Dynamic method.
dynamic_time = []
for num in used_sequence:
    start = time.time()
    dynamic_fib(num)
    end = time.time()
    ms = (end - start) * 1000
    dynamic_time.append(round(ms, 3))
print('\n')

# Finds the run time of the Binet method.
binet_time = []
for num in used_sequence:
    start = time.time()
    binet_fib(num)
    end = time.time()
    ms = (end - start) * 1000
    binet_time.append(round(ms, 3))
print('\n')

# Finds the run time of the Iterative method.
iteration_time = []
for num in used_sequence:
    start = time.time()
    iteration_fib(num)
    end = time.time()
    ms = (end - start) * 1000
    iteration_time.append(round(ms, 3))
print('\n')

# Finds the run time of the Matrix method.
matrix_time = []
for num in used_sequence:
    start = time.time()
    matrix_fib(num)
    end = time.time()
    ms = (end - start) * 1000
    matrix_time.append(round(ms, 3))

# Finds the run time of the Fast doubling method.
double_time = []
for num in used_sequence:
    start = time.time()
    double_fib(num)
    end = time.time()
    ms = (end - start) * 1000
    double_time.append(round(ms, 3))

# Creates the dataframe and prints the table
row_name2 = ['Dynamic', 'Binet', 'Iterative', 'Matrix', 'Double']
data2 = [dynamic_time, binet_time, iteration_time, matrix_time, double_time]
# row_name1 = ['Recursion', 'Dynamic', 'Binet', 'Iteration', 'Matrix', 'Double']
# data1 = [recursion_time, dynamic_time, binet_time, iteration_time, matrix_time, double_time]
df = pd.DataFrame(data2, columns=used_sequence, index=row_name2)
pd.options.display.width = None
pd.options.display.max_columns = None
print(df)

# Plots the obtained above data.
x = used_sequence
plt.plot(x, dynamic_time, label='Dynamic')
plt.plot(x, binet_time, label='Binet')
plt.plot(x, iteration_time, label='Iterative')
plt.plot(x, matrix_time, label='Matrix')
plt.plot(x, double_time, label='Fast doubling')
plt.xlabel('n-th Fibonacci term')
plt.ylabel('Time (ms)')
plt.legend(loc="upper left")
plt.show()