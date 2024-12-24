import random

def bruteForce(n):
    totalScore = 0
    for i in range(n):
        scoreBias = 6
        r = random.randint(1,100)
        
        left = 1
        right = 100
        
        # Binary search
        while left <= right:
            mid = (left + right) // 2
            if mid == r:
                break
            elif mid < r:
                left = mid + 1
            else:
                right = mid - 1
            scoreBias -= 1
            
        totalScore += scoreBias
        
    return totalScore


print (bruteForce(1000)/1000)