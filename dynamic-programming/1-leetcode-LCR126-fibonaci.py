def fib(n: int) -> int:
    MOD = 10 ** 9 + 7  # 注意这里需要mod
    dp = [-1] * 110  # 注意110是题目已知
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD  # 注意这里需要mod
    return dp[n]


def fib2(n: int) -> int:
    if n < 2: return n
    MOD = 10 ** 9 + 7
    p, q, r = 0, 1, 1
    for i in range(2, n + 1):
        r = (p + q) % MOD
        p = q
        q = r
    return r

def fib3(n: int) -> int:
    if n < 2: return n
    MOD = 10 ** 9 + 7
    def multiply(a,b):
        c=[[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                c[i][j]=(a[i][0]*b[0][j]+a[i][1]*b[1][j])%MOD
        return c

    def matrix_pow(a, n):
        ret=[[1,0],[0,1]]
        while n>0:
            if n&1:
                ret = multiply(ret, a)
            n = n>>1
            a = multiply(a,a)
        return ret
    res = matrix_pow([[1,1],[1,0]], n-1)
    return res[0][0]

if __name__ == '__main__':
    print(fib(45))
    print(fib2(45))
    print(fib3(45))
