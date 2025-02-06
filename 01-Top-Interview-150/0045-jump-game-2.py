def canJump(nums: list[int]) -> int:
    n = len(nums)
    if n == 1: return 0
    i, cnt, cover = 0, 0, nums[0]
    while i < n - 1:
        if cover >= n - 1:
            return cnt + 1
        max_next = i + nums[i]
        max_next_i = i
        for j in range(i, cover + 1):
            if max_next < j + nums[j]:
                max_next = j + nums[j]
                max_next_i = j
        cnt += 1
        if max_next != cover:
            i = max_next_i
            cover = max_next
        else:
            i = cover
            cover = cover + nums[cover]
    return cnt


def canJump2(nums: list[int]) -> int:  #
    n = len(nums)
    if n == 1: return 0
    _cur, _next, ans = 0, 0, 0
    for i in range(n):
        _next = max(_next, i + nums[i])
        if i == _cur:
            _cur = _next
            ans += 1
            if _cur>=n-1: break
    return ans


def canJump2_2(nums: list[int]) -> int:  #
    n = len(nums)
    if n == 1: return 0
    _cur, _next, ans = nums[0], 0, 0
    for i in range(n-1):
        _next = max(_next, i + nums[i])
        if i == _cur:
            _cur = _next
            ans += 1
            if _cur>=n-1:
                break
    return ans+1

def canJump3(nums: list[int]) -> int:  #
    n = len(nums)
    if n == 1: return 0
    _cur, _next, ans = 0, 0, 0
    for i in range(n-1): # 只要跳到n-2位置，要么n-2是cur边界再跳一步（if中的ans+1）到cur，要么n-2未到cur（已经跳过这一步了，因为_cur初始为0）
        _next = max(_next, i + nums[i])
        if i == _cur:  # 遇到当前覆盖范围边界
            ans += 1  # 跳一步，跳到当前覆盖范围边界
            _cur = _next  # 更新覆盖范围边界
    return ans

def canJump3_2(nums: list[int]) -> int:  #
    n = len(nums)
    if n == 1: return 0
    _cur, _next, ans = nums[0], 0, 0
    for i in range(n-1): # 只要跳到n-2位置，要么n-2是cur边界先跳一步到cur再跳一步（最后的ans+1），要么n-2未到cur再跳一步（最后的ans+1）
        _next = max(_next, i + nums[i])
        if i == _cur: # 遇到当前覆盖范围边界
            ans += 1  # 跳一步，跳到当前覆盖范围边界
            _cur = _next # 更新覆盖范围边界
    return ans+1

if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # nums = [2,3,0,1,4]
    # nums = [1]
    # nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    # nums = [1, 2, 3]
    nums = [1, 2]
    # nums = [1, 2, 3, 4, 5]
    # nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    # nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    # step = canJump(nums)
    # step = canJump2(nums)
    # step = canJump3(nums)
    # step = canJump3_2(nums)
    step = canJump2_2(nums)
    print(step)
