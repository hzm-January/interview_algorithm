class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        st = set()  # 验证当前元素是否在窗口内有重复元素
        j = 0  # 右指针
        max_len = 0
        for i in range(0, n):
            if i != 0:
                st.remove(s[i - 1])  # 左指针右移一位，删除窗口内第一个字符
            while j < n and s[j] not in st:  # 更新右指针，右移右指针
                st.add(s[j])
                j += 1
            max_len = max(max_len, j - i)  # 更新结果
            # print(st)
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        n = len(s)
        st = []  # 验证当前元素是否在窗口内有重复元素
        j = 0  # 右指针
        max_len = 0
        for i in range(0, n):
            if i != 0:
                st.remove(s[i - 1])  # 左指针右移一位，删除窗口内第一个字符
            while j < n and s[j] not in st:  # 更新右指针，右移右指针
                st.append(s[j])
                j += 1
            max_len = max(max_len, j - i)  # 更新结果
        return max_len


if __name__ == '__main__':
    # s = "abcabcbb"
    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))
