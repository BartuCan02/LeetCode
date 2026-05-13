def maxArea(height: List[int]) -> int:

        best = 0
        i = 0
        j = len(height) - 1

        while i < j:
            widht = j - i
            min_height = min(height[i], height[j])
            current = widht * min_height

            if current > best:
                best = current
            
            if height[i] > height[j]:
                j -= 1
            else: 
                i += 1
            

        return best


print(maxArea([1,8,6,2,5,4,8,3,7]))