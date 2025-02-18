# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        p = head
        ans = [[0] * n for _ in range(m)]
        level = n // 2 + n % 2
        cur = 0
        cnt = 0
        for i in range(level):
            for j in range(cur, n - cur):
                if cnt > m * n: break
                if not p:
                    ans[cur][j] = -1
                else:
                    ans[cur][j] = p.val
                    p = p.next
                cnt += 1
            for j in range(cur + 1, m - 1 - cur):
                if cnt > m * n: break
                if not p:
                    ans[j][n - 1 - cur] = -1
                else:
                    ans[j][n - 1 - cur] = p.val
                    p = p.next
                cnt += 1
            for j in range(n - 1 - cur, cur - 1, -1):
                if cnt > m * n: break
                if not p:
                    ans[m - 1 - cur][j] = -1
                else:
                    ans[m - 1 - cur][j] = p.val
                    p = p.next
                cnt += 1
            for j in range(m - 2 - cur, cur, -1):
                if cnt > m * n: break
                if not p:
                    ans[j][cur] = -1
                else:
                    ans[j][cur] = p.val
                    p = p.next
                cnt += 1
        return ans


if __name__ == '__main__':
    m, n, head = 3, 5, [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    s = Solution()
    print(s.spiralMatrix(m, n, head))
