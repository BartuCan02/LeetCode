def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    count_zero = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            count_zero += 1

        while count_zero > k:
            if nums[left] == 0:
                count_zero -= 1
            left += 1

        current_len = right - left + 1
        max_len = max(max_len, current_len)

    return max_len

    return max_




print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))