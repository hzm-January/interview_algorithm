# def fib(n: int) -> int:
#     if (n < 2): return n
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i]= dp[i - 1] + dp[i - 2]
#     return dp[n]


# def fib(n: int) -> int:
#     if (n < 2): return n
#     p, q, r = 0, 0, 1
#     for i in range(2, n+1):
#         p = q
#         q = r
#         r = p + q
#     return r

def fib(n: int) -> int:
    if (n < 2): return n
    p, q = 0, 1
    for i in range(2, n+1):
        r = p + q
        p = q
        q = r
    return r

if __name__ == '__main__':
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(10))
