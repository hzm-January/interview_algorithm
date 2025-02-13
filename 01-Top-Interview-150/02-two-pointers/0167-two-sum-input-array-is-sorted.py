def twoSum(numbers: list[int], target: int) -> list[int]:
    """
        双指针
    """
    p, q = 0, len(numbers) - 1
    while p < q:
        if numbers[p] + numbers[q] == target:
            return [p + 1, q + 1]
        if numbers[p] + numbers[q] < target:
            p += 1
        else:
            q -= 1


def twoSum2(numbers: list[int], target: int) -> list[int]:
    """
        二分查找
        该版本代码处理 “避免重复” 问题时，方法使用的不好，但是可以AC。
    """
    for i in range(len(numbers)):
        b = target - numbers[i]
        # 二分查找
        l, r = 0, len(numbers) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] == b:
                if mid != i:
                    return [i + 1, mid + 1]
                else:
                    # 测试样例：[1,2,3,4,4,9,56,90] 8
                    l = mid + 1
                    # r = mid + 1 # 修改r不行，上述测试样例会返回[5,4]，但是答案是[4,5]。为什么会这样？
            elif numbers[mid] > b:
                r = mid - 1
            else:
                l = mid + 1


def twoSum3(numbers: list[int], target: int) -> list[int]:
    """
        二分查找
        为了避免重复，即避免两个数取到同一个数组元素。
        方法：查找第二个数时，只在第一个数的右侧查找。
        为什么可以这样做？
    """
    for i in range(len(numbers)):
        b = target - numbers[i]
        # 二分查找
        l, r = i+1, len(numbers) - 1 # 注意left初始化为i+1
        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] == b:
                return [i + 1, mid + 1]
                # 测试样例：[1,2,3,4,4,9,56,90] 8
            elif numbers[mid] > b:
                r = mid - 1
            else:
                l = mid + 1

if __name__ == "__main__":
    # numbers, target = [2, 7, 11, 15], 9
    # numbers, target = [2, 3, 4], 6
    # numbers, target = [-1, 0], -1
    numbers, target = [1, 2, 3, 4, 4, 9, 56, 90], 8
    # ans = twoSum(numbers, target)
    ans = twoSum2(numbers, target)
    print(ans)
