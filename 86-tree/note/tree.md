# 1 二叉树
## 1.1 二叉树理论基础
### 1.1.1 二叉树种类
#### 1.1.1.1 满二叉树
定义：一个二叉树，如果每一个层的结点数都达到最大值，则这个二叉树就是满二叉树。

满二叉树节点数：$N = 2^0 + 2^1 + 2^2 + \cdots + 2^{h-1} = 1 \cdot \frac{2^{h} - 1}{2 - 1} = 2^h - 1$

#### 1.1.1.2 完全二叉树
定义：一棵深度为k的有n个结点的二叉树，对树中的结点按从上至下、从左到右的顺序进行编号，编号为i（1≤i≤n）的结点与满二叉树中编号为i的结点在二叉树中的位置相同。

数据结构-堆-本质上是完全二叉树

#### 1.1.1.3 二叉搜索树
定义：一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值。

节点值有顺序，所以便于搜索。节点结构没有要求。

左子树<根<右子树

搜索复杂度 $O(logn)$

#### 1.1.1.4 平衡二叉搜索树
定义：平衡二叉搜索树的任何结点的左子树和右子树高度最多相差1。

### 1.1.2 二叉树存储方式
链式存储、线性存储


### 1.1.3 二叉树定义
```python
""" python TreeNode """
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    root = TreeNode(1)
    root.val = 101
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(7)
```

### 1.1.4 二叉树遍历
注：两个逻辑：访问节点，处理节点

#### 1.1.4.1 递归法
回溯三部曲：\
1 确定递归函数参数及返回值：返回值一般是void，递归函数参数一般是当前节点cur和result结果数组\
2 确定递归终止条件：遇到空节点`cur==None`\
3 确定单层搜索逻辑

关于是否有返回值的考虑：  
1 如果不需要遍历树中所有路径，且需要返回标记，就带返回值。  
2 如果需要遍历树种所有路径，就不带返回值。  

关于终止条件的考虑：  
1 如果题目要求叶子节点，则递归终止条件应该为`node.left is None and node.right is None`。  
易错样例：路径总和，求根节点到叶子节点的路径总和为target，`tree=[1,2], target=1`时，
应该返回`False`，因为根节点`1`不是叶子节点，该树到叶子节点的路径只有一条，其路径总和为`1+2=3`  
2 如果题目没有要求叶子节点，则递归终止条件为`node is None`。


关于找到目标值即终止的考虑：  
1 定义一个标记值  
2 在递归终止条件处增加判断标记值  
3 当找到目标值时，修改该标记值  
```python
def kthSmallest(root, k: int) -> int:
    """ 递归中序遍历 """
    cnt = [0]
    ans = [-1] # 结果集-标记值

    def inorder(root):
        if not root or ans[-1] != -1:  # 递归终止条件增加标记值判断 ans[-1]!=-1是剪枝，没有也能AC，只是耗时长
            return  # ans[-1] != -1 剪枝的是 找到结果后 return 上层再执行inorder(root.right)
        inorder(root.left)
        cnt[0] += 1
        if cnt[0] == k:
            ans[0] = root.val # 找到目标值，并标记
            return
        inorder(root.right)

    inorder(root)
    return ans[0]
```
```python
graph ={}
ans= []
visited={}
def dfs(s1, s2, weight):
    # 带返回值，防止错误：s1,s2都在图中，但是不在同一个集合，没有s1到s2的路径，这时需要给结果集中添加-1.0
    if s1 not in graph or s2 not in graph:
        ans.append(-1.0)
        return True
    if s1 == s2:
        ans.append(weight)
        return True
    visited[s1] = True
    result = False
    for key, val in graph[s1].items():
        if key in visited: continue
        result = dfs(key, s2, weight * val)
        if result: return True
    return result
```


#### 1.1.4.2 迭代法
栈模拟递归，注意先进后出。

迭代法：空指针法、bool标记法、无标记法  

迭代法都需要借助栈实现遍历  

#### 1.1.4.3 深度优先遍历
前序遍历（中左右）：递归法、迭代法 [二叉树前序遍历-递归法-迭代法](../01-binary-tree/0144-binary-tree-preorder-traversal.py)

中序遍历（左中右）：递归法、迭代法 [二叉树中序遍历-递归法-迭代法](../01-binary-tree/0094-binary-tree-inorder-traversal.py)

后序遍历（左右中）：递归法、迭代法 [二叉树后序遍历-递归法-迭代法](../01-binary-tree/0145-binary-tree-postorder-traversal.py)


##### 带标记的dfs
```python
graph ={}
ans= []
visited={}
def dfs(s1, s2, weight):
    # 带返回值，防止错误：s1,s2都在图中，但是不在同一个集合，没有s1到s2的路径，这时需要给结果集中添加-1.0
    if s1 not in graph or s2 not in graph:
        ans.append(-1.0)
        return True
    if s1 == s2:
        ans.append(weight)
        return True
    visited[s1] = True
    result = False
    for key, val in graph[s1].items():
        if key in visited: continue
        result = dfs(key, s2, weight * val)
        if result: return True
    return result
```

#### 1.1.4.4 广度优先遍历
层序遍历：队列+迭代法

[二叉树层序遍历-栈](../01-binary-tree/0102-binary-tree-level-order-traversal.py)

#### 1.1.4.5 二叉树遍历总结
二叉树的 DFS 有两个要素：「访问相邻结点」和「判断 base case」

1 访问相邻结点  

二叉树的相邻结点非常简单，只有左子结点和右子结点两个。
二叉树本身就是一个递归定义的结构：一棵二叉树，它的左子树和右子树也是一棵二叉树。
那么 DFS 遍历只需要递归调用左子树和右子树即可。 

2 判断 base case   

一般来说，二叉树遍历的 base case 是 root == null。
这样一个条件判断其实有两个含义：一方面，这表示 root 指向的子树为空，不需要再往下遍历了。
另一方面，在 root == null 的时候及时返回，可以让后面的 root.left 和 root.right 操作不会出现空指针异常。

### 二叉树深度
二叉树节点深度：指从根节点到该节点的最长简单路径边的条数  
根节点深度为1，从上往下计数，依次递归，使用前序遍历（）  
### 二叉树高度
二叉树节点高度：指从该节点到叶子节点的最长简单路径边的条数  
叶子节点高度为1，从下往上计数，依次回溯，使用后序遍历（要比较当前节点的左右子树的高度）  
注：根节点的高度是二叉树的最大深度  

## 1.2 二叉树相关题目
### 1.2.1 二叉树前中后序遍历
leetcode 0144 二叉树前序遍历

leetcode 0094 二叉树中序遍历

leetcode 0145 二叉树后序遍历
### 1.2.2 二叉树层序遍历
leetcode 0102 二叉树的层序遍历

leetcode 0107 二叉树的层序遍历2

### 1.2.3 二叉树深度搜索DFS
leetcode 0101 对称二叉树  
两棵二叉树对称条件：  
1 根节点值相同  
2 每个树的右子树都与另一个树的左子树镜像对称  





