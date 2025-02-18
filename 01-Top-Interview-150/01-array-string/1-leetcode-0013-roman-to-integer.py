def romanToInt(s: str) -> int:
    """
        prev 记录之前一个数字的大小。
        因为LR中L<R的只有四种情况，且这四种情况都是连续的两个字母，所以一个保存一个prev即可判断
        case 1: 如果当前数字大于前一个数字，那么累计和先减去前一个数字进行还原，再加上prev_cur两个字符对应的真实数值即cur-prev，
        case 2: 如果当前数字小于前一个数字，直接累加
    """
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    n = len(s)
    res, prev = dic[s[0]], dic[s[0]]
    for i in range(1,n):
        cur_c = s[i]
        cur = dic[cur_c]
        if prev < cur:
            res = res - prev + cur - prev
        else:
            res += cur
        prev = cur
    return res


if __name__ == '__main__':
    # s = 'III'
    # s = 'IV'
    s = 'IX'
    # s = 'LVIII'
    # s = 'MCMXCIV'
    print(romanToInt(s))
