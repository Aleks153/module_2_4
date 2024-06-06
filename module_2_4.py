# Reshenie 1
print('Решение №1:')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1 or i == 2:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)

print('__________')

# Reshenie 2
print('Решение №2:')
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
not_primes = set(not_primes)
primes = numbers.difference(not_primes, {1, 2})

print('Простые числа из представленного списка:', primes)
print('Непростые числа из представленного списка: ', not_primes)
