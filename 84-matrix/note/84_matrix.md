# 矩阵-理论
完美模板，适用于方阵和非方阵。  

注：只需要根据【列数】处理奇偶情况。列为奇数时若不处理会出错，行为奇数时若不处理按照以下的遍历方式可以通过测试。  
注：需要一个变量记录访问/处理节点的个数，到达边界后，停止访问/处理。示例中`cnt`。  
注：从左到右`[0,m-1]`左闭右闭，从上到下`[1,n-2]`左闭右闭，从右到左`[m-1,0]`左闭右闭，左下到上`[n-2,1]`左闭右闭，必须按照这样的顺序和范围处理，否则奇数列会出现问题。
```python
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    n, m = len(matrix), len(matrix[0])
    ans = []
    cur = 0
    cnt = 0
    level = m // 2 + m % 2 # 只需根据 【列数】 处理奇偶情况
    while cur < level:
        for i in range(cur, m - cur):
            if cnt >= n * m: break
            ans.append(matrix[cur][i])
            cnt+=1
        for i in range(cur + 1, n - 1 - cur):
            if cnt >= n * m: break
            ans.append(matrix[i][m - 1 - cur])
            cnt += 1
        for i in range(m - 1 - cur, cur - 1, -1):
            if cnt >= n * m: break
            ans.append(matrix[n - 1 - cur][i])
            cnt += 1
        for i in range(n - 2 - cur, cur, -1):
            if cnt >= n * m: break
            ans.append(matrix[i][cur])
            cnt += 1
        cur += 1
    return ans
```

# 矩阵-相关题目
leetcode 0054 螺旋矩阵\
注：不一定是方阵，访问。

leetcode 0059 旋转矩阵II\
注：方阵填充。

leetcode 2326 螺旋矩阵IV\
注：非方阵填充。

