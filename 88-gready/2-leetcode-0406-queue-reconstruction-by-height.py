from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """ 两个维度 贪心 """
        people.sort(key=lambda x: (-x[0], x[1]))
        print('sorted', people)
        for i in range(len(people)):
            tmp = people[i]
            index = people[i][1]
            j = i
            while j > index:
                people[j] = people[j - 1]
                j -= 1
            people[index] = tmp
        print('insert', people)
        return people

    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        """ 两个维度 贪心 """

        def custom_sort(item):
            return -item[0], item[1]

        people.sort(key=custom_sort)
        print('sorted', people)
        for i in range(len(people)):
            tmp = people[i]
            index = people[i][1]
            j = i
            while j > index:
                people[j] = people[j - 1]
                j -= 1
            people[index] = tmp
        print('insert', people)
        return people

    def reconstructQueue3(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        print('sorted', people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]  # list insert 写法，值得学习
        print('insert', ans)
        return ans


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))
    print(Solution().reconstructQueue2(people))
    print(Solution().reconstructQueue3(people))
