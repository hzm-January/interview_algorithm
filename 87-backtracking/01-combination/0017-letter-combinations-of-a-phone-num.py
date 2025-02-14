def letterCombinations(digits: str) -> list[str]:
    """
        回溯 这种写法更通俗易懂
    :param digits:
    :return:
    """
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

def letterCombinations2(digits: str) -> list[str]:
    """ 回溯 - 写法优化 -cur """
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
    """
        回溯模板写法中：cur是来标记一个数组中cur之前的元素都已被使用过，不能再继续使用。只能使用cur之后的元素，即从cur+1往后。
        该题目中：字符是依顺序从不同的数组中抽取，cur标记的是cur之前的数组已被使用过，不能再继续使用，只能使用cur之后的数组，即从cur+1往后。
    """
    def backtracking(cur):
        if len(path) == len(digits):
            tmp = path.copy()
            ans.append(''.join(tmp))
            return
        for item in dic[digits[cur]]:
            path.append(item)
            backtracking(cur+1)
            path.pop()
    backtracking(0)
    return ans

def letterCombinations3(digits: str) -> list[str]:
    """ 回溯 - 写法优化 - 隐藏回溯 """
    if len(digits) == 0: return []
    s,ans = [],[]
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
    """
        回溯模板写法中：cur是来标记一个数组中cur之前的元素都已被使用过，不能再继续使用。只能使用cur之后的元素，即从cur+1往后。
        该题目中：字符是依顺序从不同的数组中抽取，cur标记的是cur之前的数组已被使用过，不能再继续使用，只能使用cur之后的数组，即从cur+1往后。
    """
    def backtracking(cur, s):
        if len(s) == len(digits):
            ans.append(s)
            return
        for item in dic[digits[cur]]:
            backtracking(cur+1, s+item) # 隐藏回溯
    backtracking(0, '')
    return ans

if __name__ == '__main__':
    digits = '23'
    # digits = ''
    # digits = '2'

    # ans = letterCombinations(digits)
    # ans = letterCombinations2(digits)
    ans = letterCombinations3(digits)
    print(ans)
