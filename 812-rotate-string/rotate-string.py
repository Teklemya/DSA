class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        seen = set()
        currS = s 
        print(currS)
        while currS not in seen:
            #add the inital s to the set to shot while loop when we see that string
            seen.add(currS)
            if currS == goal:
                return True
            else:
                #then now i need to move the frist letter to the end
                currS = currS[1:] + currS[0]
                print(currS)
        return False
        '''
        Given two strings after rotating the s string by moving the first letter to the end constatly if i hit the goal
        then great i return true else false?
        
        I am thinking of haivng a case where i check 
        i will set the currS = s initally
        while currS not in seen:
            if currS == goal:
                return True
            seen.add(currS)
            else:
                then now i need to move the frist letter to the end
                fristLetter = currS[0]
                currS = currS.join("firstLetter")
                currS = currS.replace(firstLetter, "")
        return False
        '''