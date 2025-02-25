from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0
        totalSum = 0
        start = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0:
            return -1
        return start

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        """
            从全局进行贪心选择，情况如下：

            情况一：如果gas的总和小于cost总和，那么无论从哪里出发，一定是跑不了一圈的

            情况二：rest[i] = gas[i]-cost[i]为一天剩下的油，i从0开始计算累加到最后一站，如果累加没有出现负数，说明从0出发，油就没有断过，那么0就是起点。

            情况三：如果累加的最小值是负数，汽车就要从非0节点出发，从后向前，看哪个节点能把这个负数填平，能把这个负数填平的节点就是出发节点。

        """
        curSum = 0
        minSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            minSum = min(minSum, curSum)
        if curSum < 0:
            return -1
        if minSum > 0:
            return 0
        # minSum < 0
        for i in range(len(gas) - 1, -1, -1):
            minSum += gas[i] - cost[i]
            if minSum >= 0:
                return i

        return -1

    def canCompleteCircuit3(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n: # 任意选一个位置开始搜索，这里选0开始
            gasSum = 0
            costSum = 0
            cnt = 0
            while cnt < n: # 从i开始往后寻找积累为负值的站
                j = (i + cnt) % n
                gasSum += gas[j]
                costSum += cost[j]
                if costSum > gasSum:
                    break
                cnt += 1
            if cnt == n: # 从i开始走了一圈，完成任务
                return i
            else: # 从i开始没有完成一圈，从下一个位置，继续寻找
                i = i + cnt + 1
        return -1


if __name__ == '__main__':
    gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    # gas, cost = [2, 3, 4], [3, 4, 3]
    # print(Solution().canCompleteCircuit(gas, cost))
    print(Solution().canCompleteCircuit3(gas, cost))
