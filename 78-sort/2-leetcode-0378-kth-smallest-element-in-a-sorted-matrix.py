from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """ 二分查找 """

        def check(mid):
            n, m = len(matrix), len(matrix[0])
            cnt = 0
            i, j = n - 1, 0
            while i >= 0 and j < m:
                if matrix[i][j] <= mid:
                    cnt += i + 1  # 如果matrix[r][c]满足条件，那么该元素所在列在0~r行的元素都满足条件，总共r+1个元素
                    j += 1  # 继续判断当前行下一列的最后一个元素是否满足条件
                else:
                    i -= 1
            return cnt >= k

        def lowerBound(left, right):
            while left <= right:  # 左闭右闭
                mid = left + (right - left) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        return lowerBound(matrix[0][0], matrix[-1][-1])

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        """ 小顶堆 """
        import heapq
        n, m = len(matrix), len(matrix[0])
        heap = [(matrix[i][0], i, 0) for i in range(n)] # 这里不用堆化，因为按这个逻辑加入堆，堆顶一定是最小的
        cnt = 1
        while heap and cnt < k:
            _, i, j = heapq.heappop(heap)
            cnt += 1
            if j + 1 < m:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return heapq.heappop(heap)[0]


if __name__ == '__main__':
    # matrix, k = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8
    matrix, k = [[1, 5, 9], [10, 11, 13], [0, 13, 15]], 8
    # matrix, k = [[-5]], 1
    print(Solution().kthSmallest(matrix, k))
    print(Solution().kthSmallest2(matrix, k))
