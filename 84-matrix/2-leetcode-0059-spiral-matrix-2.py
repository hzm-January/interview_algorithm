from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        level = n // 2 + n % 2
        cur = 0
        cnt = 1
        for i in range(level):
            for j in range(cur, n-cur):
                if cnt> n**2: break
                ans[cur][j] = cnt
                cnt+=1
            for j in range(cur+1, n-1-cur):
                if cnt > n ** 2: break
                ans[j][n-1-cur] = cnt
                cnt+=1
            for j in range(n-1-cur, cur-1, -1):
                if cnt > n ** 2: break
                ans[n-1-cur][j]=cnt
                cnt+=1
            for j in range(n-2-cur, cur, -1):
                if cnt > n ** 2: break
                ans[j][cur]=cnt
                cnt+=1
            cur+=1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))