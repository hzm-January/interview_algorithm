# 滑动窗口-理论
滑动窗口算法中只有一层循环，且该循环中`for j in range(n)`中`j`一定是终止位置，该算法的精妙之处在于如何移动起始位置`i`。
> 如果`j`是起始位置，跟暴力解法就完全相同了。  
> ```python 
> """ 暴力 解法 """
> for j in range(n):
>   for i in range(j,n):
>       [j, i] # 左闭右闭 
> ```

```python
""" 长度最小的子数组 """
def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
    """ 滑动窗口 O(n) O(1) """
    n = len(nums)
    min_len = n + 1
    i = 0
    total = 0
    for j in range(n):
        total += nums[j]
        while total >= target:
            min_len = min(min_len, j - i + 1)
            total -= nums[i]
            i += 1
    return min_len if min_len != n + 1 else 0
```


# 滑动窗口-相关题目
leetcode 0209 长度最小的子数组


