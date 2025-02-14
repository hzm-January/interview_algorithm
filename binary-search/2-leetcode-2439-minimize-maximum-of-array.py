def minimizeArrayValue(nums: list[int]) -> int:
    ans = 10**9+1
    def valid(cur:int) -> bool:
        nums[cur]-=1
        nums[cur-1]+=1
        return

    l,r = 1, len(nums)-1 # 左闭右闭
    while l<=r:
        mid = l+(r-l)//2
        if valid(mid):
            r = mid-1
        else:
            l = mid+1
    return -1

if __name__ == '__main__':
    nums = [3,7,1,6]
    ans = minimizeArrayValue(nums)
    print(ans)