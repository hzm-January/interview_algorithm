from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)  # 哈希set去重
        max_len = 0  # 结果
        for num in nums_set:
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
