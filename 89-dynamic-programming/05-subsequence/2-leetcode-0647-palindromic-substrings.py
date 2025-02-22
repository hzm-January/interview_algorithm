class Solution:
    def countSubstrings(self, s: str) -> int:
        """
            动态规划
            1 dp数组定义：dp[i][j]表示s从i到j的子串是否是回文子串
            2 递推公式
            3 dp数组初始化
            4 遍历顺序：从下到上，从左到右。因为当前值是从左下推导。最终dp数组应该是上三角
            5 打印
        """
        n = len(s)
        # print(n)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1: # 同一字符i==j，相邻两个字符i+1=j且s[i]==s[j]
                        dp[i][j] = True
                        ans += 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                        if dp[i][j]: ans += 1
                    # print('--------------',i,j)
                # print(i,j,dp)
            print(dp)
        return ans

    def countSubstrings2(self, s: str) -> int:
        """
            动态规划
            1 dp数组定义：dp[i][j]表示s从i到j的子串是否是回文子串。i为左指针，j为右指针
            2 递推公式：dp[i][j]=dp[i+1][j-1]
            3 dp初始化
            4 遍历顺序：从下到上，从左到右。因为递推公式是从左下退出当前
        """
        n = len(s)
        # print(n)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = 0 # 注意这里是0
        for i in range(n - 1, -1, -1): # 左边界
            for j in range(i, n): # 右边界
                print(i, j, s[i:j + 1])
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1
        return ans

    def countSubstrings3(self, s: str) -> int:
        """
            动态规划
            1 dp数组定义：dp[i][j]表示s从i到j的子串是否是回文子串。i为左指针，j为右指针
            2 递推公式：dp[i][j]=dp[i+1][j-1]
            3 dp初始化
            4 遍历顺序：从下到上，从左到右。因为递推公式是从左下推出当前
            该写法的好处，避免了数组越界情况的处理，即j-i<=1
        """
        n = len(s)
        dp = [[True for _ in range(n)] for _ in range(n)]
        ans = n # 对角线上都是单个字符，都是回文子串
        # 遍历方向，从右下到左上，先遍历行再遍历列，列遍历从对角线右边一列开始遍历。
        for i in range(n - 2, -1, -1): # 左边界 # dp[n-1][n-1]是单个字符一定为True，与默认值相同，不需要更新
            for j in range(i+1, n): # 右边界 # 从对角线右边一列开始遍历，例如第n-2行，j从n-1列开始遍历。
                dp[i][j] = s[i]==s[j] and dp[i + 1][j - 1]
                if dp[i][j]: ans += 1
        return ans

    def countSubstrings4(self, s: str) -> int:
        """
            dp[i][j] i到j的子串是否是回文串
            遍历方向：从左上到右下。先遍历列，后遍历行
            该写法的好处：不用处理数组越界的情况，即从右下到左上遍历方法中的j-i<=1
        """
        n = len(s)
        dp = [[True] * n for _ in range(n)] # 全部初始为True
        ans = n # 对角线上都是单个字符，都是回文子串
        # 遍历方向，从左上到右下，先遍历列再遍历行，行遍历到对角线上一行。
        for j in range(1, n): # 第0列用到两个值，dp[0][0]为True不需要遍历，dp[1][0]会用到，默认值就是True，
            for i in range(j):
                # 当j=1时，最后一个i是i=0，此时dp[1][0]，看起来是非法切割，从1到0的字符，但这也是单个字符，默认为True
                # 当j=2时，最后一个i是i=1，此时dp[2][1]，看起来是非法切割，从2到1的字符，但这也是单个字符，默认为True
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]: ans += 1
        return ans


if __name__ == '__main__':
    s = "aaa"
    # s = "abc"
    # s = "ababa"
    # s = "fdsklf"
    print(Solution().countSubstrings(s))
    # print(Solution().countSubstrings2(s))
