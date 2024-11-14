def merge_1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.

    optimize merge method
    """
    p, q, i = m - 1, n - 1, m + n - 1
    while q >= 0:
        if p >= 0 and nums1[p] > nums2[q]:
            nums1[i] = nums1[p]
            p -= 1
        else:
            nums1[i] = nums2[q]
            q -= 1
        i -= 1
    print([i for i in nums1])


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p, q, i = m - 1, n - 1, m + n - 1
    while p >= 0 and q >= 0:
        if nums1[p] < nums2[q]:
            nums1[i] = nums2[q]
            q -= 1
        else:
            nums1[i] = nums1[p]
            p -= 1
        i -= 1
    assert (p == -1 or q == -1), "error algorithm."
    while i >= 0 and q >= 0:
        nums1[i] = nums2[q]
        q -= 1
        i -= 1

    print([i for i in nums1])


if __name__ == "__main__":
    # nums1 = [1, 2, 2, 3, 3, 4, 0, 0, 0, 0, 0]
    # nums2 = [2, 3, 4, 4, 5]

    # nums1 = [0]
    # nums2 = [1]

    # nums1 = [2, 0]
    # nums2 = [1]

    nums1 = [1, 0]
    nums2 = [2]
    # merge(nums1, len(nums1) - nums1.count(0), nums2, len(nums2))
    merge_1(nums1, len(nums1) - nums1.count(0), nums2, len(nums2))
