class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i will use a hashmap to keep track of the index and the val of the elems
        #if i see that the compleiment is in the dict then i will retunr the valu or that complement and the index
        #else i will just add into dict

        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]
            seen[nums[i]] = i
            


































        # i use a hashamp to keep track if the elem and the index
        # seen = {}

        # for i, num in enumerate(nums):
        #     #check for the complement properly
        #     complement = target - num
        #     #check if the compelement in seen
        #     if complement in seen:
        #         return [seen[complement], i]
        #     seen[num] = i
            
        # time - O(N)
        # space - O(N)
















        # seen = {} # {}, {2:0}

        # for i, num in enumerate(nums):
        #     complement = target - num # 9 - 2 = 7, 9 - 7 = 2
        #     if complement in seen:
        #         return [seen[complement], i] # [0,1]
        #     else:
        #         seen[num] = i # we add


        ''' U - We are given an array that contains nums
                We are sure that two numbers in the array will add up to give us the target
                Once we find those elements we need to return the index of the two elements
            M: Dict, two pointer is sorted, brute force (double for loop)

            P:    Create a dict = {element value: index}
                Then iterate through array, as we go first substract the number from target then check if the diff
                exists in dict if it does then great we can then return the index of the element and the one in dict

                So when we set up the dict = {} # 9-2 = 7 First it is empty so no match 
                                      for diff so we can then append to dict
                                      dict = {2:0} #Second now 9 - 7 = 2 and 2 is in the dict so we return the value of 
                                      that key which our result is [value of that element in dict, and index of that elem]
            R: Test has passed
            E: Time: O(N)
               Space: O(N)
            '''
