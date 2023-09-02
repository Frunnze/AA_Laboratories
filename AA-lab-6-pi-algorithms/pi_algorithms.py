import mpmath
import time
import matplotlib.pyplot as plt

def bbp(n):
    mpmath.mp.dps = n + 2
    total = mpmath.mpf(0)

    for k in range(n):
        numerator = (mpmath.mpf(1) / 16 ** k) * (
            (mpmath.mpf(4) / (8 * k + 1))
            - (mpmath.mpf(2) / (8 * k + 4))
            - (mpmath.mpf(1) / (8 * k + 5))
            - (mpmath.mpf(1) / (8 * k + 6))
        )
        total += numerator

    pi = total
    return str(pi)[-2]


def chudnovsky(n):
    mpmath.mp.dps = n + 2 
    a = mpmath.mpf(13591409)
    b = mpmath.mpf(545140134)
    c = mpmath.mpf(-262537412640768000)
    total = mpmath.mpf(0)

    for k in range(n):
        numerator = mpmath.fac(6 * k) * (a + b * k)
        denominator = mpmath.fac(3 * k) * (mpmath.fac(k) ** 3) * c ** k
        term = numerator / denominator
        total += term

    pi = (mpmath.mpf(426880) * mpmath.sqrt(mpmath.mpf(10005))) / total
    return str(pi)[-2]


def machin(n):
    mpmath.mp.dps = n + 2
    term1 = 4 * mpmath.atan(mpmath.mpf(1)/mpmath.mpf(5))
    term2 = mpmath.atan(mpmath.mpf(1)/mpmath.mpf(239))
    pi = 4 * (term1 - term2)
    return str(pi)[-2]


bbp_times = []
for n in range(1, 5001):
    start = time.time()
    bbp(n)
    end = time.time()
    ms = (end - start) * 1000
    bbp_times.append(ms)        

chudnovsky_times = []
for n in range(1, 5001):
    start = time.time()
    chudnovsky(n)
    end = time.time()
    ms = (end - start) * 1000
    chudnovsky_times.append(ms)  

machin_times = []
for n in range(1, 5001):
    start = time.time()
    machin(n)
    end = time.time()
    ms = (end - start) * 1000
    machin_times.append(ms)                                        


# Plot the results.
x = [i for i in range(1, 5001)]
plt.plot(x, bbp_times, label = 'BBP Algorithm')
plt.plot(x, chudnovsky_times, label = 'Chudnovsky Algorithm')
plt.plot(x, machin_times, label = 'Machin Algorithm')
plt.xlabel('N-th decimal')
plt.ylabel('Time (ms)')
plt.legend(loc = 'upper left')
plt.show()