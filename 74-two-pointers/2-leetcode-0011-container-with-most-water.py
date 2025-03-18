from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p, q = 0, len(height) - 1
        ans = (0, 0, -1)
        while p < q:
            area = min(height[p], height[q]) * (q - p)
            if area > ans[2]:
                ans = (p, q, area)
                # print(ans)
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return ans[2]

    def maxArea2(self, height: List[int]) -> int:
        """ 双指针：小的边向中间移动 """
        p, q = 0, len(height) - 1
        ans = -1
        while p < q:
            area = min(height[p], height[q]) * (q - p)
            ans = max(ans, area)
            if height[p] <= height[q]:  # < 或 <= 都可以
                p += 1
            else:
                q -= 1
        return ans


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
    print(Solution().maxArea2(height))
