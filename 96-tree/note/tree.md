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
#### 1.1.4.2 迭代法
栈模拟递归，注意先进后出。



#### 1.1.4.1 深度优先遍历
前序遍历（中左右）：递归法、迭代法
```python
def preorderTraversal(root: TreeNode) -> list[int]:
    """ 回溯 前序遍历 """
    # 回溯函数
    def pre_traverse(root, ans): # 1 回溯参数列表和返回值
        if not root: # 2 终止条件
            return
        # 3 单层搜索逻辑
        ans.append(root.val)
        pre_traverse(root.left, ans)
        pre_traverse(root.right, ans)
        
    ans = [] # 结果保存数组
    pre_traverse(root, ans)
    return ans

```
```python
def preorderTraversal3(root: TreeNode) -> list[int]:
    """
        非递归 统一写法 前序遍历
    """
    stack, ans = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur) # 访问中，左
            ans.append(cur.val) # 处理中，左 # 处理右
            cur = cur.left
        cur = stack.pop() # 访问右
        cur = cur.right
    return ans
```

中序遍历（左中右）：递归法、迭代法
```python
def inorderTraversal(root: TreeNode) -> list[int]:
    """ 回溯 中序遍历 """
    def traverse(cur, ans): # 1 参数列表与返回值
        if not cur: return # 2 终止条件
        # 3 单层搜索逻辑
        if cur.left: traverse(cur.left, ans)
        ans.append(cur.val)
        if cur.right: traverse(cur.right, ans)
    ans =[]
    traverse(root, ans)
    return ans
```
```python
def inorderTraversal3(root: TreeNode) -> list[int]:
    """ 迭代 统一写法 中序遍历"""
    stack,ans=[],[]
    cur = root
    while cur or stack:
        while cur: # 访问 中，左，右
            stack.append(cur)
            cur = cur.left
        cur = stack.pop() # 处理 左，中，右
        ans.append(cur.val) # 处理 左，中，右
        cur = cur.right # 访问右
    return ans
```
后序遍历（左右中）：递归法、迭代法
```python
def postorderTraversal(root: TreeNode) -> list[int]:
    """ 回溯 后序遍历 """
    def traverse(cur, ans): # 1 回溯函数参数列表与返回值
        if not cur: return # 2 终止条件
        # 3 单层搜索逻辑
        if cur.left: traverse(cur.left, ans)
        if cur.right: traverse(cur.right, ans)
        ans.append(cur.val)
    ans=[]
    traverse(root, ans)
    return ans
```
```python
def postorderTraversal3(root: TreeNode) -> list[int]:
    """ 迭代 统一写法 后序遍历 """
    stack, ans = [], []
    cur = root
    prev = None
    while cur or stack:
        while cur: # 访问 中，左， 右
            stack.append(cur)
            cur = cur.left
        cur = stack[-1]
        if cur.right and cur.right!=prev: # right 已经处理过
            cur = cur.right
        else:
            ans.append(cur.val) # 处理 左，右， 中
            stack.pop()
            prev = cur
            cur = None
    return ans
```

#### 1.1.4.2 广度优先遍历
层序遍历：队列+迭代法

