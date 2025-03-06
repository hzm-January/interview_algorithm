# 图理论

# 图相关问题
## 岛屿问题
> 回顾二叉树遍历的两个要素：「访问相邻结点」和「判断 base case」  
> 二叉树DFS中结点的相邻结点是左右子节点，base case 是当前节点为None。

网格遍历的两个要素：「访问相邻结点」和「判断 base case」  

> 1 访问相邻结点  
> 
> 网格结点的相邻结点是上下左右四个。对于格子 (r, c) 来说（r 和 c 分别代表行坐标和列坐标），
> 四个相邻的格子分别是 (r-1, c)、(r+1, c)、(r, c-1)、(r, c+1)。换句话说，网格结构是「四叉」的。
> 
> 2 判断base case  
> 
> base1: 索引超出网格；  
> base2：结点已被访问过；防止重复访问进入无限循环；  
> base3：结点有效（例如岛屿问题中的1表示陆地有效，0表示海水无效）  

如何避免重复访问？  

> 标记已经遍历过的格子。以岛屿问题为例，需要在所有值为 1 的陆地格子上做 DFS 遍历。每走过一个陆地格子，就把格子的值改为 2，这样当我们遇到 2 的时候，就知道这是遍历过的格子了。也就是说，每个格子可能取三个值：
> 
> 0 —— 海洋格子  
> 1 —— 陆地格子（未遍历过）  
> 2 —— 陆地格子（已遍历过）  
> 
> 注意事项：
> 
> 在一些题解中，可能会把「已遍历过的陆地格子」标记为和海洋格子一样的 0，「陆地沉没方法」，
> 即遍历完一个陆地格子就让陆地「沉没」为海洋。  
> 这种方法有很大隐患，因为这样就无法区分「海洋格子」和「已遍历过的陆地格子」。如果题目更复杂一点，这很容易出 bug。


```python
def numIslands(grid: list[list[str]]) -> int:
    n, m = len(grid), len(grid[0])
    
    def inArea(row, col):
        return 0 <= row < n and 0 <= col < m
    
    def backtrack(row, col):
        if not inArea(row, col):  return # base case1 超界
        if grid[row][col] != '1': return # base case2 结点无效
        grid[row][col] = '2' # 标记结点已被访问
        backtrack(row + 1, col)
        backtrack(row - 1, col)
        backtrack(row, col + 1)
        backtrack(row, col - 1)
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '1':continue # base case3 结点已被访问
            ans+=1
            backtrack(i, j)
    return ans
```
