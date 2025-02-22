class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False  # 负数都不是回文
        if x>0 and x % 10 == 0: return False  # 末尾为0不是回文
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
            print(x, y)
            if x <= y: break
        return x == y or x == y // 10


if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))
