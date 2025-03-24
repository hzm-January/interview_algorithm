from typing import List
"""
    leetcode 0128 最长连续序列
    原数组没有排序
    思路：
    1 遍历所有元素，以每一个元素为起点查找下一个元素是否在数组中，并记录最长连续长度。  
    2 优化：判断过 x,x+1,...,x+y，就不在需要判断 x+1,...,x+y，前者包含后者，前者的长度一定大于后者  
    3 如何判断当前元素是否需要判断与搜索？ - 判断x-1是否在数组中 
    
    易错：该题原始数组中有重复元素，所以在遍历元素时，不能使用nums，而要使用nums_set，
    
    有一个测试样例，重复数字有25000个，使用nums遍历会超时
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)  # 哈希set去重
        max_len = 0  # 结果
        for num in nums_set: # 这里必须使用去重后的num_set，因为nums中有重复元素，如果使用for num in nums，有测试样例会超时
            if num - 1 not in nums_set:  # 如果num-1在哈希表中，统计num-1的结果包含了统计num的结构，跳过。
                cur_len = 1
                cur = num
                while cur + 1 in nums_set:  # 依次寻找+1是否在哈希表中
                    cur_len += 1
                    cur = cur + 1
                max_len = max(max_len, cur_len)
        return max_len

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums_set = set(nums)  # 哈希set去重
        max_len = 0  # 结果
        for num in nums_set:
            if num - 1 in nums_set: continue  # 如果num-1在哈希表中，统计num-1的结果包含了统计num的结构，跳过。
            cur_len = 1
            cur = num
            while cur + 1 in nums_set:  # 依次寻找+1是否在哈希表中
                cur_len += 1
                cur = cur + 1
            max_len = max(max_len, cur_len)
        return max_len


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    # print(Solution().longestConsecutive(nums))
    print(Solution().longestConsecutive2(nums))
