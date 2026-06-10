def pivotIndex(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total - left_sum - num

        if left_sum == right_sum:
            return i

        left_sum += num

    return -1

print(pivotIndex(nums =[-1,-1,-1,-1,-1,0]))
print(pivotIndex(nums=[1,7,3,6,5,6]))
print(pivotIndex(nums=[-1,-1,-1,0,1,1]))