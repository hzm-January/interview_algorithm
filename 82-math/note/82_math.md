# 数学-理论

## 上取整

$\lceil \frac{a}{b} \rceil$

分子分母有浮点数时，直接使用`math.ceil(a/b)`。

分子分母都是整数时，为了避免精度丢失问题，将上取整转换为下取整 $\lfloor \frac{a+b-1}{b} \rfloor$。

[参考：【【力扣双周赛 89】二分答案 | 树上统计问题】37:25](https://www.bilibili.com/video/BV1cV4y157BY/?share_source=copy_web&vd_source=5dfd63191b005c5187bf788bd7fa61b3)

## 排序

### python中自定义排序

``` python
nums.sort(key=abs, reverse=True) # 按照绝对值从大到小排序

```