def majorityElement_boyer_moore_2(nums: list[int]) -> int:
    """ boyer moore 时间O(n) 空间O(1)"""
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if candidate == num else -1)
    return candidate


def majorityElement_boyer_moore(nums: list[int]) -> int:
    """ boyer moore 时间O(n) 空间O(1)"""
    candidate, count = nums[0], 1
    for num in nums[1:]:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate = num
            count = 1
        else:
            count -= 1
    return candidate


def majorityElement(nums: list[int]) -> int:
    """ sort 时间O(nlogn) 空间(logn)"""
    nums.sort()
    return nums[len(nums) // 2]


def majorityElement_hash(nums: list[int]) -> int:
    hs = [0] * 10
    # hs = [0] * (10 ** 9) # 内存超限
    maxn, ans = 0, nums[0]
    for num in nums:
        hs[num] += 1
        if maxn < hs[num]:
            maxn = hs[num]
            ans = num
    return ans


def majorityElement_hash_2(nums: list[int]) -> int:
    import collections
    counts = collections.Counter(nums)
    print(counts)
    return max(counts.keys(), key=counts.get)


def majorityElement_sort(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


def majorityElement_Rec(nums: list[int]) -> int:
    # def countInRange(nums: list[int], num: int, lo: int, hi: int) -> int:
    #     count = 0
    #     for i in range(lo, hi):
    #         if nums[i] == num:
    #             count += 1
    #     return count
    def majorityElementRec(lo: int, hi: int) -> int:
        if (lo == hi):
            return nums[lo]
        mid = lo + (hi - lo) // 2
        left = majorityElementRec(lo, mid)
        right = majorityElementRec(mid+1, hi)
        if left == right:
            return left
        # left_count = countInRange(nums, left, lo, hi)
        # right_count = countInRange(nums, right, lo, hi)
        left_count = sum(1 for i in range(lo,hi+1) if nums[i]==left)
        right_count = sum(1 for i in range(lo,hi+1) if nums[i]==right)
        return left if left_count > right_count else right

    return majorityElementRec(0, len(nums) - 1)


if __name__ == '__main__':
    # nums = [7, 6, 5, 4, 3, 2, 1]
    nums = [1, 1, 1, 1, 2, 2, 3]
    # nums = [1, 1, 1, 3, 3, 2, 2, 2]
    # nums = [1, 1, 1, 3, 3, 2, 2, 2, 2]
    print(f"nums org: {nums}")
    # me = majorityElement_boyer_moore(nums)
    # me = majorityElement_boyer_moore_2(nums)
    # me = majorityElement_hash(nums)
    # me = majorityElement_hash_2(nums)
    # me = majorityElement_sort(nums)
    me = majorityElement_Rec(nums)
    print(f"nums me: {me}")
