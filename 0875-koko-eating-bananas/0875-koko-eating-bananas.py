from math import ceil
class Solution:
    '''
    Give piles which is a pile of bananas i and h is amount of hours allowed
    decide the mimumum speed you need to eat at to finish all bananas on time
    banana eating speed = pile / hour
    hour = pile / speed 

    h >= len(piles) always becuase i can only eat a one pile an hr
    my top speed can be set to the max pile becuase if i findh that an hour i can finish the rest

    so lets say k = max(pile) now inorder to find the mimumim k i need to check from 1 -> k
    and return the minmum number that will satisify the case 


    M - Brute force is check all k from 1 - k for speed in range(1, k): ..
        or i can use a binary search apporach to cut k in half everytime to get to the right solution

    P - set left -> 1 and right to the max(pile)
        res could be float(inf) but in this case the highest it can be is max(piles)
        then do a binary search on k 
        while left <= right:
            k = left + right // 2
            then check for each pile the total hour it would take to eat for that k
            totalhour = 0
            for pile in piles:
                totalhour += math.celi(pile / k)
            # now i have total hour it took me to eat at that speed i can check if i am i the time limit
            if totalHour <= h:
                # i have found one work i will update my result but that might not be the lowest
                res = min(res, k)
                #since i updated my res by mid i don't need to recheck it but i need to check the lower
                right = mid - 1
            else:
                it is on the upper range so
                left = mid + 1
        finally return the result
        return res

    '''
   
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min left can be is 1 becuase if we use 0 we are not eating anything
        left, right = 1, max(piles)
        # since we knows the max of the piles will give us a working result we can set it to that and update as we find min
        res = right

        while left <= right:
            k = (left + right) // 2
            #let us set total hour
            totalHours = 0
            for pile in piles:
                totalHours += ceil(float(pile) / k)
            #we have found one working k
            if totalHours <= h:
                res = min(res, k)
                #because we have checked that mid already
                right = k - 1
            else:
                left = k + 1
        return res

        ############################# Brute Force #################################
        #time  = O(max(piles) * n)
        # upperRange = max(piles)
        # res = upperRange
        # for k in range(1, upperRange + 1):
        #     totalHour = 0
        #     for pile in piles:
        #         totalHour += math.ceil(pile / k)
        #     if totalHour <= h:
        #         res = min(res, k)
        # return res 
    '''
    U — Understand
        Given piles of bananas and h hours
        Koko eats at speed k bananas/hour
        Each hour → chooses ONE pile
        Goal:
            Find the minimum k such that all bananas are eaten within h hours

    M — Match
        This is Binary Search on Answer
        Why?
        If k is too small → too slow 
        If k is big enough / max value in piles → works 

        Find first valid k which is max value in piles
    
    P — Plan
        Search range:
            left = 1
            right = max(piles)
        For each k:
            totalHours = sum(ceil(pile / k))
        If:
        totalHours <= h
            k works → try smaller

        Else → k too slow → increase
    
    '''