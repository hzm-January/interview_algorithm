def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    path, ans = [], []

    def backstacking(cur, sum):
        if sum > target: return  # 剪枝1
        if sum == target:
            tmp = path.copy()
            ans.append(tmp)
        for i in range(cur, len(candidates)):
            path.append(candidates[i])
            sum += candidates[i]
            backstacking(i, sum)
            path.pop()
            sum -= candidates[i]

    backstacking(0, 0)
    return ans


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    path, ans = [], []

    def backstacking(cur, sum):
        if sum > target: return  # 剪枝1
        if sum == target:
            tmp = path.copy()
            ans.append(tmp)
        i = cur
        while i < len(candidates) and sum + candidates[i] <= target: # 剪枝2：
            path.append(candidates[i])
            sum += candidates[i]
            backstacking(i, sum)
            path.pop()
            sum -= candidates[i]
            i += 1

    candidates.sort()
    backstacking(0, 0)
    return ans


if __name__ == "__main__":
    candidates, target = [2, 3, 6, 7], 7
    # ans = combinationSum(candidates=candidates, target=target)
    ans = combinationSum2(candidates=candidates, target=target)
    print(ans)
