from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """ 双指针 寻找第一个非负整数下标 """
        n = len(nums)
        ans = []
        # 找到第一个非负整数索引
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        # 从第一个非负整数索引处，向两边遍历
        # 平方较小的先加入结果集
        p, q = i - 1, i
        while p >= 0 and q < n:
            if -nums[p] > nums[q]:
                ans.append(nums[q] ** 2)
                q += 1
            else:
                ans.append(nums[p] ** 2)
                p -= 1
        for i in range(q, n):
            ans.append(nums[i] ** 2)
        for i in range(p, -1, -1):
            ans.append(nums[i] ** 2)

        return ans

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        """
            双指针 左右指针
            该写法速度较慢，因为每次要在数组下标0插入
        """
        n = len(nums)
        ans=[]
        p,q = 0, n - 1
        while p <= q:
            if nums[p]**2 > nums[q]**2:
                ans.insert(0,nums[p] ** 2)
                p+=1
            else:
                ans.insert(0,nums[q] ** 2)
                q-=1
        return ans
    def sortedSquares3(self, nums: List[int]) -> List[int]:
        """
            双指针 左右指针 优化版
        """
        n = len(nums)
        ans=[0]*n
        k = n-1
        p,q = 0, n - 1
        while p <= q:
            if nums[p]**2 > nums[q]**2:
                ans[k]=nums[p] ** 2
                p+=1
            else:
                ans[k]=nums[q] ** 2
                q-=1
            k-=1
        return ans

if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
    print(Solution().sortedSquares2(nums))
    print(Solution().sortedSquares3(nums))
