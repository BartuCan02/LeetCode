def longestSubarray(nums: List[int]) -> int:
    left, current, max_, count_zero = 0, 0, 0, 0 

    for right in range(len(nums)):
            if nums[right] != 1:
                count_zero += 1

            while count_zero > 1:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1

            current = (right - count_zero) - left + 1
            max_ = max(current, max_)

    if max_ == 0:
         return 0
    elif count_zero == 0:
         return len(nums) - 1
    
    return 0


print(longestSubarray(nums=[1,1,0,1]))
print(longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))
print(longestSubarray(nums = [1,1,1]))

            
