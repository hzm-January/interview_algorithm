def longestCommonPrefix(strs: list[str]) -> str:
    """ 横向搜索 """

    def getCommonPrefix(str1, str2):
        n, m = len(str1), len(str2)
        length = min(n, m)
        index = 0
        for i in range(length):
            if str1[i] == str2[i]:
                index += 1
            else:
                break
        return str1[:index]

    n = len(strs)
    prefix = strs[0]
    for i in range(1, n):
        prefix = getCommonPrefix(strs[i], prefix)
        if len(prefix) == 0:
            return ""
    return prefix


def longestCommonPrefix2(strs: list[str]) -> str:
    """ 纵向搜索 """
    n = len(strs)
    for i in range(0, len(strs[0])):
        c = strs[0][i]
        for j in range(1, n):
            if i >= len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]  # i位置的字符不匹配，或者i已经是某个字符串的长度
    return strs[0]  # 所有字符都合格


def longestCommonPrefix3(strs: list[str]) -> str:
    """ 分治 """
    def lcp(left, right):
        if left == right:  # 递归终止条件
            return strs[left]
        mid = left + (right - left) // 2
        # divide
        left_prefix = lcp(left, mid)
        right_prefix = lcp(mid + 1, right)
        # merge -> conquer
        n = min(len(left_prefix), len(right_prefix))
        index = 0
        for i in range(n):
            if left_prefix[i] == right_prefix[i]:
                index += 1
        return left_prefix[:index]

    return lcp(0, len(strs) - 1)


def longestCommonPrefix4(strs: list[str]) -> str:
    """ 二分查找 """
    def valid(id):
        for i in range(1, len(strs)):
            if strs[i][:id] != strs[0][:id]:
                return False
        return True

    n = len(min(strs, key=len))
    l, r = 0, n  # 左闭右开
    while l < r:
        mid = l + (r - l + 1) // 2
        if valid(mid):
            l = mid
        else:
            r = mid - 1

    return strs[0][:l]


if __name__ == '__main__':
    # strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    # print(longestCommonPrefix(strs))
    # print(longestCommonPrefix3(strs))
    strs = ['a']
    print(longestCommonPrefix4(strs))
