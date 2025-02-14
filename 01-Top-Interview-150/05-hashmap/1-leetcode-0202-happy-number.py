def isHappy(n: int) -> bool:
    """ 快慢指针 """

    def bitSquareSum(n: int) -> int:
        sum = 0
        while n:
            bit = n % 10
            n = n // 10
            sum += bit * bit
        return sum

    slow, fast = bitSquareSum(n), bitSquareSum(bitSquareSum(n))
    while slow != fast:
        slow = bitSquareSum(slow)
        fast = bitSquareSum(fast)
        fast = bitSquareSum(fast)

    return slow == 1


def isHappy2(n: int) -> bool:
    def bitSquareSum(n: int) -> int:
        sum = 0
        while n > 0:
            bit = n % 10
            n = n // 10
            sum += bit ** 2
        return sum
    hash = {}
    while n!=1 and n not in hash:
        hash[n] = 1
        n = bitSquareSum(n)
    return n == 1


if __name__ == '__main__':
    print(isHappy(19))
    print(isHappy(2))
    print(isHappy2(19))
    print(isHappy2(2))
