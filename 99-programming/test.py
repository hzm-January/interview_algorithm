def valid_path(tmp,s):
    path, ans = [], []
    used = [0] * len(s)

    def backtracking(tmp):
        if len(''.join(path)) == len(s):
            print('path',path)
            if ''.join(path) == s:
                print('final',path)
                ans.append(path.copy())
                print('ans',ans)
                tmp = path.copy()
                return ans
        for i in range(0, len(tmp)):
            if used[i] == 1: continue
            path.append(tmp[i])
            used[i] = 1
            backtracking(tmp)
            used[i] = 0
            path.pop()

    backtracking(tmp)
    return ans[0] if ans else[]

if __name__ == '__main__':
    tmp = ['leet','code']
    s = 'leetcode'
    print(valid_path(tmp,s))