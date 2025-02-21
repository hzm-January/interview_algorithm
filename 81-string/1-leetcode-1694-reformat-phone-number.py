class Solution:
    def reformatNumber(self, number: str) -> str:
        # 预处理，删除非数字字符
        s = ''
        for c in number:
            if c.isdigit():
                s += c
        # 格式化
        m = len(s)
        ans = ''
        cnt = 0 # 已处理数字的数量
        for i in range(m):
            ans += s[i]
            cnt += 1
            if cnt == m: continue # 已到达末尾
            if m - cnt >= 4 and cnt % 3 == 0: # 当前已处理数字数量是3的倍数，且距离末尾大于4
                ans += '-'
            elif m % 3 == 0 and cnt % 3 == 0: # 当前已处理数字数量是3的倍数，且数字总数为3的倍数
                ans += '-'
            elif m % 3 == 2 and m - cnt == 2: # 当前距离末尾2个数字，且数字总数模3剩余2
                ans += '-'
            elif m % 3 == 1 and m - cnt == 2:
                ans += '-' # 数字总数模3剩余1，且当前距离末尾2个数字
        return ans


if __name__ == '__main__':
    # numbers = "1-23-45 6"
    numbers = "123 4-567"
    # numbers = "123 4-5678"
    print(Solution().reformatNumber(numbers))
