"""
    桶排序
"""
def bucketSort(nums: list[int]) -> list[int]:
    # 1 确定数组元素的值域范围
    n = len(nums)
    min_val = min(nums)  # 最小值
    max_val = max(nums)  # 最大值
    # 2 划分子区间
    bucketSize = 10
    bucketCount = (max_val - min_val) // bucketSize + 1
    buckets = [[] for _ in range(bucketCount)]
    for num in nums:
        buckets[(num - min_val) // bucketSize].append(num)
    # 3 对每个子区间O(nlogn)排序
    ans = []
    for bucket in buckets:
        ans.extend(sorted(bucket))
    return ans


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 100) for _ in range(100)]
    print(nums)
    print(bucketSort(nums))
