# 滑动窗口-理论
滑动窗口算法本质：通过窗口滑动（左出右进）O(1)操作，简化暴力搜索中每次迭代都要O(n)对比目标串。

## 滑动窗口-解法
needSum：记录窗口缺少元素总数  
need：字典类型，记录窗口缺少的每个元素的个数  
## 定长滑动窗口
leetcode 0438 找到字符串中所有字母异位词  
leetcode 0567 字符串的排列 

```python
def findAnagrams4(self, s: str, p: str) -> List[int]:
    """
        滑动窗口  窗口长度固定  正规写法 (推荐)
        needSum 记录需要元素总数
        need 记录需要每个元素的个数
        1 右进左出，保证窗口长度不变
            右进：右进字符为目标串中字符，需求-1，总需求-1
            左出：左出字符为目标串中字符，需求+1，总需求+1
        2 needSum==0，表示窗口中的子串匹配上了目标串
    """
    from collections import Counter
    s_len, p_len = len(s), len(p)
    need = dict(Counter(p))
    needSum = p_len
    ans=[]
    for j in range(s_len):
        if s[j] in need:  # 右侧进一个字符
            if need[s[j]] > 0: # 如果need[s[j]]<0，说明当前窗口中有多余的s[j]。如果need[s[j]]==0，说明窗口中s[j]的个数与目标串中s[j]的个数相同，暂时不需要s[j]
                needSum -= 1
            need[s[j]] -= 1
        i = j - p_len # 获取定长窗口 左指针
        if i >= 0 and s[i] in need:  # 左侧出一个字符
            if need[s[i]] >= 0:  # 如果need[s[i]]<0，表示当前窗口中有多余的s[i]，暂时不需要s[i]
                needSum += 1 # 如果need[s[i]]==0，表示当前窗口中s[j]个数与目标串中s[j]的个数相同，但是现在左侧要弹出一个是s[j]，窗口中从刚好不需要就变成需要一个s[j]
            need[s[i]] += 1
        if needSum==0:
            ans.append(i+1)
    return ans
```


代码模板：  
## 不定长滑动窗口

最最大/最长  
求最小/最短  
求子数组个数   

[灵茶山艾府-题目分类列表](https://leetcode.cn/discuss/post/3578981/ti-dan-hua-dong-chuang-kou-ding-chang-bu-rzz7/)

leetcode 0209 长度最小的子数组  
leetcode 0076 最小覆盖子串
```python
""" 该题答案可作为模板 """
""" 长度最小的子数组 """
def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
    """ 滑动窗口 O(n) O(1) """
    n = len(nums)
    min_len = n + 1
    i = 0
    total = 0
    for j in range(n): # 右指针滑动一格
        # 右进
        total += nums[j] # 右进，窗口计数处理
        while total >= target: # 左出
            min_len = min(min_len, j - i + 1) # 最小长度处理
            # 左出
            total -= nums[i] # 左出，窗口计数处理
            i += 1 # 左指针滑动一格
    return min_len if min_len != n + 1 else 0
```

```python
def minWindow(self, s: str, t: str) -> str:
    """ leetcode 0076 最小覆盖子串 """
    from collections import Counter
    n, m = len(s), len(t)
    i = 0
    need = dict(Counter(t))
    needSum = m
    minLen = n + 1
    minSub = None
    for j in range(n):
        """ 右进 """
        if s[j] not in need:  # 右进字符不在目标串中
            continue
        # 如果need[s[j]]<0，说明当前窗口中有多余的s[j]。如果need[s[j]]==0，说明窗口中s[j]的个数与目标串中s[j]的个数相同，暂时不需要s[j]
        if need[s[j]] > 0:
            needSum -= 1  # 右进
        need[s[j]] = need.get(s[j], 0) - 1  # 右进
        """ 左出 """
        while needSum <= 0:
            if minLen > j - i + 1:
                minLen = j - i + 1
                minSub = s[i:j + 1]
            # 左出
            if s[i] not in need:
                i += 1
                continue
            # 如果need[s[i]]<0，表示当前窗口中有多余的s[i]，暂时不需要s[i]
            # 如果need[s[i]]==0，表示当前窗口中s[j]个数与目标串中s[j]的个数相同，但是现在左侧要弹出一个是s[j]，窗口中从刚好不需要就变成需要一个s[j]
            if need[s[i]] >= 0: 
                needSum += 1
            need[s[i]] = need.get(s[i], 0) + 1  # 左出
            i += 1   # 左侧出一个字符
    return minSub if minSub else ""
```


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
## 1 长度固定的窗口
leetcode 0438 找到字符串中所有字母异位词  
leetcode 0567 字符串的排列  

## 2 长度不固定的窗口
leetcode 0076 最小覆盖子串


# 滑动窗口-相关题目
leetcode 0209 长度最小的子数组  
注：该题窗口为target，即窗口内元素总和刚好大于等于target，如果窗口内元素总和大于target很多，需要移动左边界，如果窗口内元素总和小于target时，需要移动右边界。  


