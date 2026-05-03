def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        num_possible = 0
        
        if (len(flowerbed) == 1) and (flowerbed[0] == 0):
             return True
             
        for i,element in enumerate(flowerbed):

            
            if element == 1:
                continue
            
            elif (i == 0 and flowerbed[i + 1] != 1) or (i == len(flowerbed) - 1 and flowerbed[i - 1] != 1):
                num_possible += 1
                flowerbed[i] = 1
            
            elif (i == 0 or i == (len(flowerbed) - 1)):
                continue
                    
            elif (flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1):
                num_possible += 1
                flowerbed[i] = 1
            
        return False if n > num_possible else True