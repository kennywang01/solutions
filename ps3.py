from scipy.stats import binom

# binom.pmf(k, n, p) computes P(X=k) using the binomial PMF with params n and p

def type1(n, k):
    p = 0
    for i in range(k, n + 1): # n is included in this interval
        p += binom.pmf(i, n, 0.5)
    return p

def type2(n, k):
    p = 0
    for i in range(0, k): # k is not included in this interval
        p += binom.pmf(i, n, 0.7)
    return p

def params(n):
    for k in range(0, n + 1):
        alpha = type1(n, k)
        beta = type2(n, k)
        if (alpha < 0.05 and beta < 0.05):
            return [n, k]
    return params(n + 1)

print(params(0))
        


