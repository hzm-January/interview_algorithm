def hIndex2(citations: list[int]) -> int:
    """
     计数排序
    :param citations:
    :return:
    """
    hl_max = max(citations)
    hs = [0] * (hl_max + 1)
    for i, citation in enumerate(citations):
        hs[1:citation + 1] = [x + 1 for x in hs[1:citation + 1]]
    # print(hs)
    ans = 0
    for i in range(1, hl_max + 1):
        if hs[i] >= i:
            ans = i
    return ans


def hIndex2_2(citations: list[int]) -> int:
    """
    计数排序 优化计数数组
    :param citations:
    :return:
    """
    hl_max = len(citations)  # 使用citation的长度即可，超过该长度的引用数记为citation长度位置的计数加1
    hs = [0] * (hl_max + 1)
    for i, citation in enumerate(citations):
        if citation > hl_max: citation = hl_max  # 如果citation超过了论文总数量，则将该citation记为论文总数量位置的引用。
        hs[1:citation + 1] = [x + 1 for x in hs[1:citation + 1]]
    # print(hs)
    ans = 0
    for i in range(1, hl_max + 1):
        if hs[i] >= i:
            ans = i
    return ans


def hIndex2_3(citations: list[int]) -> int:
    """
    计数排序 优化计数逻辑
    :param citations:
    :return:
    """
    hl_max = len(citations)  # 使用citation的长度即可，超过该长度的引用数记为citation长度位置的计数加1
    hs = [0] * (hl_max + 1)
    for i, citation in enumerate(citations):
        if citation > hl_max: citation = hl_max  # 如果citation超过了论文总数量，则将该citation记为论文总数量位置的引用。
        hs[citation] += 1
    # print(hs)
    ans, cnt = 0, 0
    for i in range(hl_max, 0, -1):
        cnt += hs[i]
        if cnt >= i:
            ans = i
            break
    return ans


def hIndex2_4(citations: list[int]) -> int:
    """
    计数排序 优化代码逻辑
    :param citations:
    :return:
    """
    hl_max = len(citations)  # 使用citation的长度即可，超过该长度的引用数记为citation长度位置的计数加1
    hs = [0] * (hl_max + 1)
    for i, citation in enumerate(citations):
        if citation > hl_max: citation = hl_max  # 如果citation超过了论文总数量，则将该citation记为论文总数量位置的引用。
        hs[citation] += 1
    # print(hs)
    cnt = 0
    for i in range(hl_max, 0, -1):
        cnt += hs[i]
        if cnt >= i:
            return cnt  # 直接返回引用数量
    return 0  # 如果倒序遍历完成后没有找到h，则返回0


def hIndex1(citations: list[int]) -> int:
    """
        排序
    """
    citations = sorted(citations, reverse=True)
    print(citations)
    i, h = 0, 0
    while i < len(citations) and citations[i] > h:
        h += 1
        i += 1
    return h


def hIndex1_1(citations: list[int]) -> int:
    """
        排序 优化计数变量
    """
    citations = sorted(citations, reverse=True)
    i = 0
    while i < len(citations) and citations[i] > i:
        i += 1
    return i


def hIndex3(citations: list[int]) -> int:
    """
        二分查找
        难点：target是变化的。
        思想：在文章数量范围[0, len(arr)]中二分查找h。
        每个子区间内都需要求target：每个h的合理范围左闭右闭[left,right]区间内统计大于h=mid的文章数量。
        时间复杂度：O(nlogn)
        空间复杂度：O(1)
    """
    left, right = 0, len(citations) # 文章总数在合理范围内，所以可以访问到len(citations)，左闭右闭
    while left <= right: # O(logn)
        mid = left + (right - left) // 2
        cnt = 0
        for i in range(len(citations)): #O(n)
            if citations[i] >= mid:
                cnt+=1
        if cnt == mid:
            return mid
        elif cnt > mid:
            left = mid + 1
        else:
            right = mid - 1
    return left-1


if __name__ == '__main__':
    # hl = [3, 0, 6, 1, 5]
    hl = [0]
    # hl = [1, 3, 1]
    # h = hIndex(hl)
    # h = hIndex2_3(hl)
    # h = hIndex1(hl)
    h = hIndex3(hl)
    print(h)
