def trailingZeroes(n: int) -> int:
    """
        数学  O(n) O(1)
        思路：求1~n，所有10的倍数个数。即2的倍数和5的倍数中较小的数，又因2的倍数个数一定大于5的倍数个数，所以求5的倍数个数即可。
    :param n:
    :return:
    """
    ans = 0
    for i in range(n, 0, -1): # 遍历从n到1
        while i % 5 == 0: # 5的倍数
            i //= 5
            ans += 1
    return ans

def trailingZeros(n: int) -> int:
    """
        数学 优化版本 O(logn) O(1)
    :param n:
    :return:
    """
    ans = 0
    while n:
        n//=5 # 递推公式 n/p^k = (n/p^(k-1))/p
        ans +=n # 求累加和
    return ans


if __name__ == "__main__":
    print(trailingZeroes(3))
    print(trailingZeroes(5))
    print(trailingZeroes(0))
