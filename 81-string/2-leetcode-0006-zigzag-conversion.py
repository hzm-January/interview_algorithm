class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        p = 0
        while p < len(s):
            for i in range(numRows):
                if p >= len(s):
                    break
                ans[i].append(s[p])
                p += 1
            if p >= len(s): break
            for j in range(numRows - 2, 0, -1):
                if p >= len(s): break
                ans[j].append(s[p])
                p += 1
        return ''.join([''.join(s) for s in ans])

    def convert2(self, s: str, numRows: int) -> str:
        ans = ['' for _ in range(numRows)]
        p = 0
        while p < len(s):
            for i in range(numRows):
                if p >= len(s):
                    break
                ans[i] += s[p]
                p += 1
            if p >= len(s): break
            for j in range(numRows - 2, 0, -1):
                if p >= len(s): break
                ans[j] += s[p]
                p += 1
        return ''.join(ans)

    def convert3(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        ans = ['' for _ in range(numRows + 1)]
        i, j = 0, 0
        flag = 1
        while i < len(s):
            ans[j] += s[i]
            j += flag
            if j == numRows - 1 or j == 0:  # 值得学习，遇到边界修改累加量，达到Z字形效果
                flag = -flag
            i += 1
        return ''.join(ans)

    def convert4(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        ans = ['' for _ in range(numRows + 1)]
        i, j = 0, 0
        flag = -1
        while i < len(s):
            ans[j] += s[i]
            if j == numRows - 1 or j == 0:
                flag = -flag
            j += flag
            i += 1
        return ''.join(ans)


if __name__ == "__main__":
    s, numRows = "PAYPALISHIRING", 3
    print(Solution().convert(s, numRows))
    print(Solution().convert2(s, numRows))
    print(Solution().convert3(s, numRows))
    print(Solution().convert4(s, numRows))
