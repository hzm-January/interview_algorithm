import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """ 堆 """
        n, m = len(nums1), len(nums2)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(n, k))]
        ans = []
        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)  # 最小堆，堆顶
            ans.append([nums1[i], nums2[j]])
            if j + 1 < m:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans

    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """ 二分查找 """

        def check(mid):
            n, m = len(nums1), len(nums2)
            r, c = n - 1, 0
            cnt = 0
            while r >= 0 and c < m:
                if nums1[r] + nums2[c] <= mid:
                    cnt += r + 1  # 如果matrix[r][c]满足条件，那么该元素所在列在0~r行的元素都满足条件，总共r+1个元素
                    c += 1 # 继续判断当前行下一列的最后一个元素是否满足条件
                else:
                    r -= 1
            return cnt >= k

        def lowerBound(left, right): # 寻找第一个大于等于k的元素
            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    right = mid - 1  # 左闭右闭
                else:
                    left = mid + 1
            return left

        left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        pairSum = lowerBound(left, right)  # 满足条件k对最小和时的和为pairSum

        # 寻找小于pairSum的元素对
        # 以下写法超时
        ans = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 < pairSum:
                    ans.append([num1, num2])
                if len(ans) == k:
                    return ans
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 == pairSum:
                    ans.append([num1, num2])
                if len(ans) == k:
                    return ans


if __name__ == '__main__':
    # nums1, nums2, k = [1, 7, 11], [2, 4, 6], 3
    nums1, nums2, k = [1, 1, 2], [1, 2, 3], 2
    # print(Solution().kSmallestPairs(nums1, nums2, k))
    print(Solution().kSmallestPairs2(nums1, nums2, k))
