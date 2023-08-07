def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_product(target_product):
    for p in range(2, target_product):
        if is_prime(p) and target_product % p == 0:
            q = target_product // p
            if is_prime(q):
                return p, q
    return None

target_product = 177773
result = find_primes_product(target_product)

if result:
    p, q = result
    print(f"p = {p}, q = {q}")
else:
    print("No solution found.")
