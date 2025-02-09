def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    """
        回溯 - used数组去重
    :param candidates:
    :param target:
    :return:
    """
    path, ans = [], []
    used = [False] * len(candidates)

    def backtrack(cur, sum):
        if sum > target: return
        if sum == target:
            tmp = path.copy()
            ans.append(tmp)
            return
        i = cur
        while i < len(candidates) and sum + candidates[i] <= target:
            if i > 0 and candidates[i] == candidates[i - 1] and (not used[i - 1]):
                i += 1
                continue
            path.append(candidates[i])
            sum += candidates[i]
            used[i] = True
            backtrack(i + 1, sum)  # 这里是从i+1开始，用过的不能再用
            used[i] = False
            sum -= candidates[i]
            path.pop()
            i += 1


    candidates.sort()  # 该题目必须排序，因为有重复数组
    backtrack(0, 0)
    return ans

def combinationSum2_2(candidates: list[int], target: int) -> list[list[int]]:
    """
        回溯 - used数组去重
    :param candidates:
    :param target:
    :return:
    """
    path, ans = [], []

    def backtrack(cur, sum):
        if sum > target: return
        if sum == target:
            tmp = path.copy()
            ans.append(tmp)
            return
        i = cur
        while i < len(candidates) and sum + candidates[i] <= target:
            if i > cur and candidates[i] == candidates[i - 1]:
                i += 1
                continue
            path.append(candidates[i])
            sum += candidates[i]
            backtrack(i + 1, sum)  # 这里是从i+1开始，用过的不能再用
            sum -= candidates[i]
            path.pop()
            i += 1

    candidates.sort()  # 该题目必须排序，因为有重复数组
    backtrack(0, 0)
    return ans

if __name__ == "__main__":
    candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
    # ans = combinationSum2(candidates, target)
    ans = combinationSum2_2(candidates, target)
    print(ans)
