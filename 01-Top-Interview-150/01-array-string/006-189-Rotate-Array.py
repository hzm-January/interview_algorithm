def rotate_reverse(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = len(nums) - k % len(nums)
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    nums[:] = nums[::-1]
    print(nums)


def rotate_iter(nums: list[int], k: int) -> None:
    new_nums = [-1] * len(nums)
    for i in range(len(nums)):
        new_nums[(i + k) % len(nums)] = nums[i]
    nums[:] = new_nums

def rotate_iter2(nums: list[int], k: int) -> None:
    import math
    n = len(nums)
    gcd = math.gcd(n, k)
    for i in range(gcd):
        cur = i
        prev = nums[i]
        flag = True
        while flag or cur != i:
            _next_ = (cur + k) % n
            temp = nums[_next_]
            nums[_next_] = prev
            cur = _next_
            prev = temp
            flag = False



def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    # rotate_reverse(nums, 3)
    # rotate_iter(nums, 3)
    rotate_iter2(nums, 3)
    print(nums)


if __name__ == '__main__':
    main()
