class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if not stack:
                    return False
                top = stack.pop()
                if s[i] == ')' and top != '(': return False
                elif s[i] == '}' and top != '{': return False
                elif s[i] == ']' and top != '[': return False
            else:
                stack.append(s[i])
            print(stack)
        return True if not stack else False

    def isValid2(self, s: str) -> bool:
        n = len(s)
        stack = []
        dic = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        for c in s:
            if c in dic.keys():
                if not stack: return False
                top = stack.pop()
                if dic[c] != top: return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == '__main__':
    s = "()[]{}"
    # print(Solution().isValid(s))
    print(Solution().isValid2(s))
