import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

print


a = []
for i in range(1000, 10000+1):
    x = sum(list(divisorGenerator(i))[:-1])
    if i < x:
        a.append(abs(i-x))
print(sum(a))
