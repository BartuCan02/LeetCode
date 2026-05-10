def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):                
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1

                        
moveZeroes([1, 2, 3, 0, 4])
