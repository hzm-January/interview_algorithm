def mySqrt(x: int) -> int:
    import math
    if x == 0: return 0
    ans = int(math.exp(1 / 2 * math.log(x)))
    return ans + 1 if (ans + 1) ** 2 <= x else ans


def mySqrt2(x: int) -> int:
    """
        二分查找
        寻找第一个大于平方大于x的元素，再减一，就是根号x取整的数字
    """
    if x <= 1: return x  # 该写法必须加这个条件，否则测试样例[0]输出错误-1
    left, right = 0, x  # 左闭右开
    while left < right:  # 左闭右开
        mid = left + (right - left) // 2
        if mid ** 2 > x:
            right = mid  # 左闭右开
        else:
            left = mid + 1
    return left - 1


# def mySqrt3(x: int) -> int: # 错误写法
#     x_next, x_cur, C = 0, float(x), float(x)
#     while abs(x_cur - x_next) > 1e-7: # 这里是错误的，所有测试样例第二次迭代前都会推出循环，因为第一次迭代会将x_cur赋值为x_next，x_cur-x_next=0
#         x_next = 1 / 2 * (x_cur + C / x_cur)
#         x_cur = x_next # 这里对x_cur赋值为x_next，下一轮while的条件一定不满足，因为x_cur-x_next=0
#     return int(x_cur)

def mySqrt4(x: int) -> int:
    if x==0:return 0 # 这里必须有判断，因为x0=x作为分母，如果x=0，会报除0异常
    xi, x0, C = 0, float(x), float(x)
    while True:
        xi = 0.5 * (x0 + C / x0)
        if abs(x0 - xi) < 1e-7:
            break
        # print(x0, xi)
        x0 = xi
    return int(x0)

if __name__ == "__main__":
    # print(mySqrt(4))
    # print(mySqrt(8))
    # print(mySqrt2(4))
    # print(mySqrt2(8))
    # print(mySqrt3(4))
    # print(mySqrt3(8))

    print(mySqrt4(4))
    print(mySqrt4(8))