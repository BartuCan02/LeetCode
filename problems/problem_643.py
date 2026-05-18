def findMaxAverage(nums: List[int], k: int) -> float:
    window_avg = sum(nums[:k]) / k
    best = window_avg

    for i in range(k,len(nums)):
        window_avg = window_avg + (nums[i] / k) - (nums[i - k]) / k
        if window_avg > best:
            best = window_avg


    return best

print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
