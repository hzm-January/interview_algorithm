def searchMatrix(matrix: list[list[int]], target: int) -> bool:  # 错误代码，死循环
    row_n, col_n = len(matrix), len(matrix[0])
    left_r, left_c, right_r, right_c = 0, 0, row_n - 1, col_n - 1
    while left_r < right_r or (left_r == right_r and left_c <= right_c):
        mid_r = left_r + (right_r - left_r) // 2
        mid_c = left_c + (right_c - left_c) // 2
        if matrix[mid_r][mid_c] == target:
            return True
        if matrix[mid_r][mid_c] < target:
            if mid_c < col_n - 1:
                left_r = mid_r
                left_c = mid_c + 1
            else:
                left_c = 0
                if mid_r < row_n - 1:
                    left_r = mid_r + 1
                else:
                    return False
        else:
            if mid_c > 0:
                right_r = mid_r
                right_c = mid_c - 1
            else:
                if mid_r > 0:
                    right_r = mid_r - 1
                else:
                    return False
                right_c = col_n - 1
    return False


def searchMatrix2(matrix: list[list[int]], target: int) -> bool:  #
    """
        一维索引 到 二维索引 映射
    """
    row_n, col_n = len(matrix), len(matrix[0])
    n_1d = row_n * col_n
    left, right = 0, n_1d - 1
    while left <= right:
        mid = left + (right - left) // 2
        row, col = mid // col_n, mid % col_n
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == '__main__':
    target, matrix = 13, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # target, matrix = 3, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # ans = searchMatrix(matrix, target)
    ans = searchMatrix2(matrix, target)
    print(ans)
