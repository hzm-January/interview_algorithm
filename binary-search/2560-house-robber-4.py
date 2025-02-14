def minCapability(nums: list[int], k: int) -> int:
    """
        最小化 最大值
        从一系列最大值中找出最小值。

    :param nums: 每间房屋存放的现金金额
    :param k: 至少窃取k间房
    :return: 最小窃取能力
    """

    def valid(target: int) -> bool:
        cnt = 0  # 房屋窃取数
        prev = False  # 前一个房屋的房屋没有取（相邻房屋不能同时取）
        for num in nums:
            if num <= target and prev == False:  # 只要小于等于target，取当前房间i，最后min(max(房间i...),,...,max(房间j...))一定小于等于target。
                cnt += 1
                prev = True
            else:  # 只要大于target，就不能取当前房间i，因为最后min(max(房间i...),...,max(房间j...))有可能大于target。
                prev = False
        return cnt >= k  # 窃取至少k个房间

    # 二分查找
    # 在所有可能的最大值中，找最小值
    l, r = 0, max(nums)  # 1 左闭右闭
    ans = max(nums)
    while l <= r:  # 2 左闭右闭
        mid = l + (r - l) // 2
        if valid(mid): # mid满足条件，继续在[l, mid-1]找更小
            ans = mid
            r = mid - 1
        else: # 不满足条件，继续在[mid+1, r]找
            l = mid + 1
    return ans


if __name__ == '__main__':
    nums, k = [2, 3, 5, 9], 2
    ans = minCapability(nums, k)
    print(ans)
