def letterCombinations(digits: str) -> list[str]:
    if len(digits) == 0: return []
    path,ans = [],[]
    dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r','s'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    def backtracking(cur):
        if len(path) == len(digits):
            tmp = path.copy()
            ans.append(''.join(tmp))
            return
        for i in range(cur, len(digits)):
            for item in dic[digits[i]]:
                path.append(item)
                backtracking(i+1)
                path.pop()
    backtracking(0)
    return ans


if __name__ == '__main__':
    # digits = '23'
    digits = ''
    # digits = '2'

    ans = letterCombinations(digits)
    print(ans)
