class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float(inf)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))    
        return res  



        '''
        Given an int array, i will keep trakc of the value and index for target and then calcuate to take 
        the minimum abs(i-start) and return that so first i will build a dict if num == target i will add it in dict
        for val in dict i will claclute the min of value - start and take the min of that and return
        '''