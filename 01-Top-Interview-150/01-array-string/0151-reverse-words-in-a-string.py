def reverseWords(s: str) -> str:
    def trim_space(s: str) -> list[str]:
        l, r = 0, len(s) - 1
        # 删除字符串开头的空格
        while l <= r and s[l] == ' ':
            l += 1
        # 删除字符串结尾的空格
        while r >= l and s[r] == ' ':
            r -= 1

        # 删除中间多余空格
        output = []
        while l <= r:
            if s[l] != ' ':
                output.append(s[l])
            elif output[-1] != ' ': # 因为上面处理了两端的空格，所以不可能出现output为空的情况。如果是全空字符串，上面处理结束后l>r，不会走到这里
                output.append(s[l])
            l += 1
        return output

    def reverse(s: list[str], l, r): # 这里不能传子串进来，否则外部调用这里执行后没有修改原始串
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

    def reverseWord(s: list[str]):
        """快慢指针"""
        l, r, n = 0, 0, len(s)
        while l < n:
            # 找到一个单词的末尾
            while r < n and s[r] != ' ':
                r += 1
            reverse(s, l, r - 1)
            l = r + 1
            r += 1
    _s = trim_space(s)
    # print(_s)
    reverse(_s, 0, len(_s) - 1)
    # print(_s)
    reverseWord(_s)
    # print(_s)
    return ''.join(_s)


if __name__ == '__main__':
    # s = "the sky is blue"
    # s = "  hello world  "
    s = "     "
    print(reverseWords(s))
