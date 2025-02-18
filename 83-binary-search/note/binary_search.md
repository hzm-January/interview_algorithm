# 1 二分查找基础理论
**适用题目：有序序列中是否存在满足某条件的元素**

易错点1：`while(lef<right)` 还是 `while(lef<=right)`?\
易错点2：`if(arr\[mid]>target)` 是 `right = mid` 还是 `right = mid-1`?\
易错点3：`right` 初始化 是 `right=len(arr)` 还是  `right=len(arr)-1`?

确定区间类型（是左闭右开还是左闭右闭）？ - 确定区间类型才能确定三个易错点的内容，确定区间类型后，整个算法编写过程都要遵循这个区间类型\

易错点1：左闭右开`while(lef<right)`，左闭右闭`while(lef<=right)`\
易错点2：左闭右开`right = mid`，左闭右闭`right = mid-1`\
易错点3：左闭右开`right=len(arr)`，左闭右闭`right=len(arr)-1`

循环不变量：不变量是指区间定义。在二分查找的过程中，保持区间定义不变，即在while寻找中每一次边界的处理都要坚持根据区间的定义来操作，这就是循环不变量规则。
>通俗理解：如果区间是左闭右开，在所有处理中，都保持左闭右开。如果区间是左闭右闭，在所有处理中，都保持左闭右闭。  

## 1.1 二分查找基础题目

```python
def search(nums: list[int], target: int) -> int:
    """
        左闭右闭
    """
    left, right = 0, len(nums) - 1  # 右闭，所以right=len(arr)-1
    while left <= right:  # 右闭，所以right必须能访问到
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1  # 右闭，因为已经判断mid>target，所以右边界不能是mid，必须是mid-1
    return -1
```

```python
def search(nums: list[int], target: int) -> int:
    """
        左闭右开
    """
    left, right = 0, len(nums)  # 右开，所以定义为len(nums)，下一轮右开区间一定不包含mid
    while left < right:  # 右开，所以right不能被访问到
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # 右开，并且已经判断了nums[mid]>target，所以下一轮右开区间一定不包含mid
    return -1
```

特殊情况1：lower_bound，求序列中第一个大于等于x的元素的位置（寻找有序序列第一个满足“值大于等于x”的元素的位置）

```python
def lowerbound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)  # 左闭右开，有可能最后一个元素都小于target，所以最后一个元素必须能访问到。
    while left < right:
        mid = left + (right - left) // 2
        # 注意这里没有 nums[mid] == target，整个算法需要[left,right]夹住答案
        if nums[mid] >= target:  # 注意这一步，必须有等号
            right = mid
        else:
            left = mid + 1
    return left # 如果数组中所有元素都小于target，最后left=right=n
```

特殊情况2：upper_bound，求序列中第一个大于x的元素的位置（寻找有序序列第一个满足“值大于x”的元素的位置）

```python
def upperbound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)  # 左闭右开，有可能最后一个元素都小于target，所以最后一个元素必须能访问到。
    while left < right:
        mid = left + (right - left) // 2
        # 注意这里没有 nums[mid] == target，整个算法需要[left,right]夹住答案
        if nums[mid] > target:  # 注意这一步，没有等号
            right = mid
        else:
            left = mid + 1
    return left # 如果数组中所有元素都小于target，最后left=right=n
```

特殊情况3：寻找有序序列第一个满足“条件!=C”的元素的位置。\
使用上面的满足“条件==C”的方法求解index后，再减一。

特殊情况4：递减序列。\
使用上面的方法，将`nums[mid]>x`修改为`nums[mid]<x`

## 快速幂
### 理论
```python
def myPow(x: float, n: int) -> float:
        if x==0.0:return 0.0 # 处理底数为0的情况
        if n < 0: x, n = 1 / x, -n
        ret = 1
        while n:
            if n&1: ret = ret * x # 奇数处理 x^5=x(x^2)^2
            x = x * x # 偶数翻倍
            n = n>>1 # 除以2
        return ret
```
### 题目
0050 pow(x,n) - 1 快速幂

## 最小化最大值
### 理论
```python
def minCapability(nums: list[int], k: int) -> int:
    """
        最小化 最大值
        从一系列最大值中找出最小值。

    :param nums: 每间房屋存放的现金金额
    :param k: 至少窃取k间房
    :return: 最小窃取能力
    """

    def valid(target: int) -> bool:
        cnt = 0  # 房屋窃取数
        prev = False  # 前一个房屋的房屋没有取（相邻房屋不能同时取）
        for num in nums:
            if num <= target and prev == False:  # 只要小于等于target，取当前房间i，最后min(max(房间i...),,...,max(房间j...))一定小于等于target。
                cnt += 1
                prev = True
            else:  # 只要大于target，就不能取当前房间i，因为最后min(max(房间i...),...,max(房间j...))有可能大于target。
                prev = False
        return cnt >= k  # 窃取至少k个房间

    # 二分查找
    # 在所有可能的最大值中，找最小值
    l, r = 0, max(nums)  # 1 左闭右闭
    ans = max(nums)
    while l <= r:  # 2 左闭右闭
        mid = l + (r - l) // 2
        if valid(mid): # mid满足条件，继续在[l, mid-1]找更小
            ans = mid
            r = mid - 1
        else: # 不满足条件，继续在[mid+1, r]找
            l = mid + 1
    return ans
```
### 相关题目
leetcode 2560 打家劫舍4 \


## 题目

0274 H 指数
0035 搜索插入位置\
0074 搜索二维矩阵
0162 寻找峰值\
0033 搜索旋转排序数组\
0034 在排序数组中查找元素的第一个和最后一个位置\


# 相关题目
0035 搜索插入位置 - 1 二分查找 O(logn) O(1)

0074 搜索二维矩阵 - 1 行、列-两次二分查找 O(logn+logm)=O(lognm) O(1)；2 索引映射-一次二分查找O(logmn) O(1)

0162 寻找峰值 - 1 寻找最大值 O(n) O(1)；2 迭代爬坡 O(n) O(1)；3 二分查找 O(logn) O(1) 

<u>0033 搜索旋转排序数组 - 1 二分查找 O(logn) O(1) </u>

0034 在排序数组中查找元素的第一个和最后一个位置 - 1 二分查找 O(logn) O(1) lowerbound and upperbound

