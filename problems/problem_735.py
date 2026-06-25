def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for asteroid in asteroids:
        alive = True

        while stack and stack[-1] > 0 and asteroid < 0:
            if stack[-1] < abs(asteroid):
                stack.pop()
            elif stack[-1] == abs(asteroid):
                stack.pop()
                alive = False
                break
            else:
                alive = False
                break

        if alive:
            stack.append(asteroid)

    return stack

print(asteroidCollision([1,-1,-2,-2]))

#Input: asteroids = [5,10,-5]
#Output: [5,10]