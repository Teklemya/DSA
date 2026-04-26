class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        #for each i i will need to find the two compleiment pairs j and k
        for i in range(len(nums)):
            #skip dupliactes if cur i and prev are the same, after processing the first
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            #while the two pointer don't overlap 
            while j < k:
                currSum = nums[j] + nums[k]
                #if we find curr as a solution we add it to result
                if currSum == target:
                    #i will append this pair to the res
                    res.append([nums[i], nums[j], nums[k]])
                    #now we move both j and k so that we don't end up with duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    #move j and k and if it is still a duplaicte move it
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif currSum < target:
                    j += 1
                else:
                    k -= 1 
        return res




        '''

        Given an int array nums i need to retunr the triplets i, j, k when i add them up it will return a 0
        I am thinking of sorting and using two pointers, for each i i will find the two pairs that will be the two
        pairs

        so like is nums[i] + nums[j] + nums[k] == 0

        then that means nums[i] = -nums[j] + - nums[k]
        nums[i] = - (nums[j] + nums[k])
        -nums[i] = nums[j] + nums[k]

        nums = [-1,0,1,2,-1,-4]

        sortedNums = [-3,-1,-1,0,1,2] = -1 + 0 + 2 == 0
                       i  j         k 
        
        for each i, i need to find the two pairs that will add up to - i which is my target

        j is going to be at  i + 1 and k  is len(nums) - 1

        while j < k
        currSum = nums[j] + nums[k]
        then i will check if currSum == target
        if they are equal then am move both j and k
        if currSum < target then that means i need to move j 
        else move k

        '''
































        '''
        U - We need to find three numbers in the array to add up to zero, 
        The solution can only be valid if distinct solutions exisit (no duplicates)
        if i have one distinct i then i can do two pointers

        traget = 0
        left and right = 1, 
        solutions
        for i in range(len(nums)):
           if nums[i] +  
        '''