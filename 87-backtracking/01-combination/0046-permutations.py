def permute(nums: list[int]) -> list[list[int]]:
    path, ans = [], []
    used = [0] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            tmp = path.copy()
            ans.append(tmp)
            return
        for i in range(len(nums)):
            if used[i]: continue
            path.append(nums[i])
            used[i] = 1
            backtrack()
            used[i] = 0
            path.pop()

    backtrack()
    return ans


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # nums = [0,1]
    nums = [1]
    ans = permute(nums)
    print(ans)
