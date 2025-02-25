def mergeSort(nums: list[int]) -> list[int]:
    def merge(left, right):
        sorted = []
        p, q, k = 0, 0, 0
        while p < len(left) and q < len(right):
            if left[p] <= right[q]:
                sorted.append(left[p])
                p += 1
            else:
                sorted.append(right[q])
                q += 1
            k += 1

        while p < len(left):
            sorted.append(left[p])
            p += 1
        while q < len(right):
            sorted.append(right[q])
            q += 1
        return sorted  # 必须用副本，否则tmp修改，nums也会被修改

    def backtrack(arr):
        if len(arr) <= 1:
            return arr
        l, r = 0, len(arr)
        mid = l + (r - l) // 2
        left_half = backtrack(arr[:mid])
        right_half = backtrack(arr[mid:])
        return merge(left_half, right_half)

    return backtrack(nums)


if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(mergeSort(nums))
