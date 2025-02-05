def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    # print(type(obstacleGrid))
    print(obstacleGrid)
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    ans = [[0] * n for _ in range(m)]
    print('ans:', ans)
    flag = False
    for i in range(m):
        if flag:
            ans[i][0] = 0
            continue
        if obstacleGrid[i][0] == 1:
            ans[i][0] = 0
            flag = True
        else:
            ans[i][0] = 1
    print('m:', ans)
    flag = False
    for i in range(n):
        if flag:
            ans[0][i] = 0
            continue
        if obstacleGrid[0][i] == 1:
            ans[0][i] = 0
            flag = True
        else:
            ans[0][i] = 1
    print('n:', ans)
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                ans[i][j] = 0
            else:
                ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
    return ans[-1][-1]


def uniquePathsWithObstacles_2(obstacleGrid: list[list[int]]) -> int:
    """
        优化初始化
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    ans = [[0] * n for _ in range(m)]
    print('ans:', ans)
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        ans[i][0] = 1
    print('m:', ans)
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        ans[0][i] = 1
    print('n:', ans)
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                ans[i][j] = 0
            else:
                ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
    return ans[-1][-1]


def uniquePathsWithObstacles_3(obstacleGrid: list[list[int]]) -> int:
    """
        优化空间复杂度，滚动数组
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    ans = [0] * n
    print('ans:', ans)
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        ans[i] = 1
    print('n:', ans)
    for i in range(1, m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                ans[j] = 0
            elif j > 0:
                ans[j] = ans[j - 1] + ans[j]
    return ans[-1]


def uniquePathsWithObstacles_4(obstacleGrid: list[list[int]]) -> int:
    """
        优化空间复杂度，滚动数组
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    ans = [0] * n
    print('ans:', ans)
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        ans[i] = 1
    print('n:', ans)
    for i in range(1, m):
        for j in range(n): # 这里必须从0开始，例如[[0],[1]]需要更新dp数组的第2行的第1列为0
            if obstacleGrid[i][j] == 1: # 这里会更新j=0位置的dp数组
                ans[j] = 0
            elif j > 0:
                ans[j] = ans[j - 1] + ans[j]
    return ans[-1]


if __name__ == '__main__':
    # obstacleGrid = [[0, 1, 0], [1, 1, 0], [0, 0, 0]]
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # obstacleGrid = [[1,0]]
    obstacleGrid = [[0], [1]]
    # obstacleGrid = [[0,1],[0,0]]
    # n = uniquePathsWithObstacles(obstacleGrid)
    # n = uniquePathsWithObstacles_2(obstacleGrid)
    # n = uniquePathsWithObstacles_3(obstacleGrid)
    n = uniquePathsWithObstacles_4(obstacleGrid)
    print(n)
