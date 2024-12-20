
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


if __name__ == '__main__':
    # nums = [7, 6, 5, 4, 3, 2, 1]
    nums = [1, 1, 1, 1, 2, 2, 3]
    # nums = [1, 1, 1, 3, 3, 2, 2, 2]
    # nums = [1, 1, 1, 3, 3, 2, 2, 2, 2]
    print(f"nums org: {nums}")
    # me = majorityElement_boyer_moore(nums)
    me = majorityElement_boyer_moore_2(nums)
    print(f"nums me: {me}")
