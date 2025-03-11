class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
            KMP: O(n+m)
            旋转问题：双倍数组拼接

        """
        if len(s) != len(goal): return False
        sarr = list(s) + list(s)
        n, m = len(sarr), len(goal)

        # 1 生成next数组
        def getNext():
            nxt = [-1]*m
            k = -1
            for i in range(1,m):
                while k!=-1 and sarr[k+1]!=sarr[i]:
                    k=nxt[k]
                if sarr[k+1]==sarr[i]:
                    k+=1
                nxt[i]=k
            return nxt
        nxt = getNext()
        j = 0
        for i in range(n):
            while j>0 and sarr[i]!=goal[j]:
                j=nxt[j-1]+1
            if sarr[i]==goal[j]:
                j +=1
            if j==m:
                return True
        return False

    def rotateString2(self, s: str, goal: str) -> bool:
        """
            暴力 BF
            旋转问题：双倍数组拼接
        """
        if len(s) != len(goal): return False
        sarr = list(s) + list(s)
        n, m = len(sarr), len(goal)


        for i in range(n-m+1):
            sub = ''.join(sarr[i:i+m])
            if sub==goal:return True
        return False

    def rotateString3(self, s: str, goal: str) -> bool:
        """ 模拟 """
        n,m = len(s), len(goal)
        for i in range(n): # 旋转次数
            flag = True
            for j in range(m):
                if s[(i+j)%n]!=goal[j]:
                    flag = False
                    break
            if flag: return True
        return False



if __name__ == '__main__':
    s,goal="abcde",'cdeab'
    print(Solution().rotateString(s, goal))
    print(Solution().rotateString2(s, goal))
    print(Solution().rotateString3(s, goal))