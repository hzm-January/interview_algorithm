def myPow(x: float, n: int) -> float:
    """
        快速幂
    """
    if x==0.0:return 0.0
    if n < 0: x, n = 1 / x, -n
    ret = 1
    while n:
        if n&1: ret = ret * x
        x = x * x
        n = n>>1
    return ret

def myPow2(x: float, n: int) -> float:
    """
        递归写法
    """
    if x==0.0:return 0.0
    def quickMul(N):
        if N ==0:
            return 1
        y = quickMul(N//2)
        return y*y if N%2==0 else y*y*x
    return quickMul(n) if n>=0 else 1.0/quickMul(-n)

if __name__ == '__main__':
    # ans = myPow(2.0, 10)
    # ans = myPow(2.1, 3)
    # ans = myPow(2.0, -2)
    ans = myPow2(0.0, -2)
    print(ans)
