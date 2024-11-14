def removeElement_1(nums: list[int], val: int) -> int:
    p, q = 0, len(nums)-1
    while p <= q:
        if nums[p] == val:
            nums[p] = nums[q]
            q -= 1
        else:
            p += 1

    print([v for i, v in enumerate(nums) if i < p])
    return p


def removeElement(nums: list[int], val: int) -> int:
    p, q = 0, 0
    while q < len(nums):
        if nums[q] != val:
            nums[p] = nums[q]
            p += 1
        q += 1

    print([v for i, v in enumerate(nums) if i < p])
    return p


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    # removeElement(nums, 11)
    removeElement_1(nums, 11)

