from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
            贪心 求局部峰值/谷底
            注1：处理首尾
            注2：处理平坡
            注3：同一递进方向中有平坡[1,2,2,2,3,3]
        """
        n = len(nums)
        if n <= 1: return n
        # 与判断条件中的prev<=0和prev>=0共同解决初始摆动
        # 测试样例[0,0,0] 一个摆动
        # 测试样例[3,3,3,2,5] 两个摆动 0->3->2->5 + 结尾默认有的1个
        prev = 0  # pre diff 指的是前一个递进方向
        cnt = 1  # 结果集，默认最后一定有一个摆动
        for i in range(1, n):
            if (nums[i] > nums[i - 1] and prev <= 0) or (nums[i] < nums[i - 1] and prev >= 0):
                cnt += 1  # 计入结果集
                # 注：pre diff 只能在峰值或谷底处，递进方向改变时更新，不能随着遍历一直更新，即这一行不能放到if外面
                # 测试样例 [1,2,2,2,3,3]
                prev = nums[i] - nums[i - 1]  # update pre diff
        return cnt

    # def wiggleMaxLength2(self, nums: List[int]) -> int:
    #     """
    #         错误代码：这个写法 有两个测试点没通过
    #         动态规划
    #         1 dp数组含义：以 nums[i] 为结尾的摆动子序列最大长度为 dp[i]
    #         2 递推公式：如果是峰值或谷底：dp[i] = dp[i - 1] + 1；如果不是dp[i]=dp[i - 1]
    #         3 dp数值初始化：dp[0]=1
    #         4 遍历顺序：从前到后
    #         5 打印
    #     """
    #     n = len(nums)
    #     if n < 2: return n
    #     dp = [0] * n
    #     dp[0] = 0 if nums[0] == nums[1] else 1
    #     for i in range(1, n - 1):
    #         if (nums[i - 1] <= nums[i] and nums[i] > nums[i + 1]) or (nums[i - 1] >= nums[i] and nums[i] < nums[i + 1]):
    #             dp[i] = dp[i - 1] + 1
    #         else:
    #             dp[i] = dp[i - 1]
    #         print(dp)
    #     return dp[-2] + 1

    def wiggleMaxLength3(self, nums: List[int]) -> int:
        """
            动态规划
            1 dp数组定义：
                dp[i][0] 考虑0到i子序列中以i作为山峰的 摆动序列最大长度
                dp[i][1] 考虑0到i子序列中以i作为山谷的 摆动序列最大长度
            2 状态转移方程：
                dp[i+1][0]=max(dp[i][0], dp[j][1]+1)
                dp[i+1][1]=max(dp[i][1], dp[j][0]+1)
            3 dp数组初始化：
                dp[0][0]=1
                dp[0][1]=1
            4 遍历顺序
            5 打印
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [1, 1]
        for i in range(1, n):
            dp[i][0] = dp[i][1] = 1
            for j in range(i): # 寻找 i 之前的波峰
                if nums[j] > nums[i]:  # i是波谷，接在波峰后面
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            for j in range(i): # 寻找 i 之前的波谷
                if nums[j] < nums[i]:  # i是波峰，接在波谷后面
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)

        return max(dp[-1][0],dp[-1][1])


if __name__ == '__main__':
    # nums = [1, 7, 4, 9, 2, 5]
    # nums = [1,1, 7, 4,4,4, 9, 2, 5,5]
    # nums= [1,17,5,10,13,15,10,5,16,8]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # nums = [0, 1]
    # nums = [0, 0]
    # nums = [0, 0, 0]
    # nums = [3, 3, 3, 2, 5]
    nums = [372, 492, 288, 399, 81, 2, 320, 94, 416, 469, 427, 117, 265, 357, 399, 456, 496, 337, 355, 219, 475, 295,
            457, 350, 490, 470, 281, 127, 131, 36, 430, 412, 442, 174, 128, 253, 1, 56, 306, 295, 340, 73, 253, 130,
            259, 223, 14, 79, 409, 384, 209, 151, 317, 441, 156, 275, 140, 224, 128, 250, 290, 191, 161, 472, 477, 125,
            470, 230, 321, 5, 311, 23, 27, 248, 138, 284, 215, 356, 320, 194, 434, 136, 221, 273, 450, 440, 28, 179, 36,
            386, 482, 203, 24, 8, 391, 21, 500, 484, 135, 348, 292, 396, 145, 443, 406, 61, 212, 480, 455, 78, 309, 318,
            84, 474, 209, 225, 177, 356, 227, 263, 181, 476, 478, 151, 494, 395, 23, 114, 395, 429, 450, 247, 245, 150,
            354, 230, 100, 172, 454, 155, 189, 33, 290, 187, 443, 123, 59, 358, 241, 141, 39, 196, 491, 381, 157, 157,
            134, 431, 295, 20, 123, 118, 207, 199, 317, 188, 267, 335, 315, 308, 115, 321, 56, 52, 253, 492, 97, 374,
            398, 272, 74, 206, 109, 172, 471, 55, 452, 452, 329, 367, 372, 252, 99, 62, 122, 287, 320, 325, 307, 481,
            316, 378, 87, 97, 457, 21, 312, 249, 354, 286, 196, 43, 170, 500, 265, 253, 19, 480, 438, 113, 473, 247,
            257, 33, 395, 456, 246, 310, 469, 408, 112, 385, 53, 449, 117, 122, 210, 286, 149, 20, 364, 372, 71, 26,
            155, 292, 16, 72, 384, 160, 79, 241, 346, 230, 15, 427, 96, 95, 59, 151, 325, 490, 223, 131, 81, 294, 18,
            70, 171, 339, 14, 40, 463, 421, 355, 123, 408, 357, 202, 235, 390, 344, 198, 98, 361, 434, 174, 216, 197,
            274, 231, 85, 494, 57, 136, 258, 134, 441, 477, 456, 318, 155, 138, 461, 65, 426, 162, 90, 342, 284, 374,
            204, 464, 9, 280, 391, 491, 231, 298, 284, 82, 417, 355, 356, 207, 367, 262, 244, 283, 489, 477, 143, 495,
            472, 372, 447, 322, 399, 239, 450, 168, 202, 89, 333, 276, 199, 416, 490, 494, 488, 137, 327, 113, 189, 430,
            320, 197, 120, 71, 262, 31, 295, 218, 74, 238, 169, 489, 308, 300, 260, 397, 308, 328, 267, 419, 84, 357,
            486, 289, 312, 230, 64, 468, 227, 268, 28, 243, 267, 254, 153, 407, 399, 346, 385, 77, 297, 273, 484, 366,
            482, 491, 368, 221, 423, 107, 272, 98, 309, 426, 181, 320, 77, 185, 382, 478, 398, 476, 22, 328, 450, 299,
            211, 285, 62, 344, 484, 395, 466, 291, 487, 301, 407, 28, 295, 36, 429, 99, 462, 240, 124, 261, 387, 30,
            362, 161, 156, 184, 188, 99, 377, 392, 442, 300, 98, 285, 312, 312, 365, 415, 367, 105, 81, 378, 413, 43,
            326, 490, 320, 266, 390, 53, 327, 75, 332, 454, 29, 370, 392, 360, 1, 335, 355, 344, 120, 417, 455, 93, 60,
            256, 451, 188, 161, 388, 338, 238, 26, 275, 340, 109, 185]
    s = Solution()
    # print(s.wiggleMaxLength(nums))
    print(s.wiggleMaxLength2(nums))
    print(s.wiggleMaxLength3(nums))
