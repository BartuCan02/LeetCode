def increasingTriplet(nums:List[int])->bool:
        
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n

            elif n <= second:
                second = n

            else:
                return True

        return False

print(increasingTriplet([2,1,1,1,3]))