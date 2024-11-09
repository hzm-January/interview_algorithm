import torch


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p, q, d = m - 1, n - 1, m + n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[d] = nums1[p]
                p -= 1
            else:
                nums1[d] = nums2[q]
                q -= 1
            d -= 1
        while q >= 0:
            nums1[d] = nums2[q]
            q -= 1
            d -= 1


if __name__ == "__main__":
    solution = Solution()
    # case 1
    # nums1 = [3, 3, 3, 0, 0, 0, 0]
    # nums2 = [1, 2, 5, 6]
    # m, n = 3, 4

    # case 2
    # nums1 = [1]
    # nums2 = []
    # m, n = 1, 0

    # case 2
    nums1 = [0]
    nums2 = [1]
    m, n = 0, 1

    solution.merge(nums1, m, nums2, n)
    print('----- list -----')
    print(' '.join(map(str, nums1)))
