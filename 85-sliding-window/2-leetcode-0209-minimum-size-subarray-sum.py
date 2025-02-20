from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """ 暴力  超时 """
        n = len(nums)
        min_len = n + 1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    min_len = min(min_len, j - i + 1)
        return min_len if min_len != n + 1 else 0

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        """ 滑动窗口 O(n) O(1) """
        n = len(nums)
        min_len = n + 1
        i = 0
        total = 0
        for j in range(n):
            total += nums[j]
            while total >= target:
                min_len = min(min_len, j - i + 1)
                total -= nums[i]
                i += 1
        return min_len if min_len != n + 1 else 0

    def minSubArrayLen3(self, target: int, nums: List[int]) -> int:
        """ 前缀和 + 二分查找 """

        def lower_bound(sums, t):
            # 二分查找
            l, r = 0, n - 1  # 左闭右闭
            while l <= r:
                mid = l + (r - l) // 2
                if sums[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1  # 左闭右闭
            return l if sums[l] >= t else -1

        # 前缀和
        n = len(nums)
        sum = [0] * (n + 1)
        sum[0] = nums[0]
        ans = n + n
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]  # sum[i]为nums[0]到nums[i-1]的元素和

        for i in range(1, n + 1):  # 遍历前缀和
            _target = target + sum[i - 1]  #
            bound = lower_bound(sum, _target)
            if bound >= 0:
                ans = min(ans, bound - i + 1)
        return ans if ans != n + n else 0

    def minSubArrayLen4(self, target: int, nums: List[int]) -> int:
        """
            前缀和 + 二分查找
            优化前缀和生成代码
         """
        def lower_bound(sums, t):
            # 二分查找
            l, r = 0, n - 1  # 左闭右闭
            while l <= r:
                mid = l + (r - l) // 2
                if sums[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1  # 左闭右闭
            return l if sums[l] >= t else -1

        # 前缀和
        n = len(nums)
        sum = [0]
        ans = n + 1
        for i in range(1, n + 1):
            sum.append(sum[-1] + nums[i - 1])  # sum[i]为nums[0]到nums[i-1]的元素和

        for i in range(1, n + 1):  # 遍历前缀和
            _target = target + sum[i - 1]  #
            bound = lower_bound(sum, _target)
            if bound >= 0:
                ans = min(ans, bound - i + 1)
        return ans if ans != n + 1 else 0


if __name__ == '__main__':
    # nums, t = [2,3,1,2,4,3],7
    # nums,t = [1,4,4], 4
    # nums, t = [1, 1, 1, 1, 1, 1, 1, 1], 11
    nums, t = [2, 3, 1, 2, 4, 3], 7
    s = Solution()
    print(s.minSubArrayLen(t, nums))
    print(s.minSubArrayLen2(t, nums))
    #
