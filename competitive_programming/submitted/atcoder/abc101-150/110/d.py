# abc 110 d - Factorization
# ref https://img.atcoder.jp/abc110/editorial.pdf
# ref https://note.nkmk.me/python-math-factorial-permutations-combinations/
# ref https://note.nkmk.me/python-prime-factorization/

from operator import mul
from functools import reduce
import collections

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n, m = map(int, input().split())
c = collections.Counter(prime_factorize(m))
#print(c)
ans = 1
for it in c.items():
    #print(it)
    ans *= combinations_with_replacement_count(n, it[1])
mo = 10**9+7
ans %= mo
print(ans)
