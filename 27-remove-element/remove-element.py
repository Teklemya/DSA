class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0

        for i in range(len(nums)):
            #check if the reader pointer is the not same as val if so move it to writer and move writer
            if nums[i] != val:
                nums[writer] = nums[i]
                writer += 1
        return writer

        '''
            Given an array of ints i am requireed to go ahead and remove the elems with the val of val 
            but i can't use two arrays becuase then that will not be in place replacemnet

            so i need to use two pointers that way i can use a pointer to check if the pointer

            [1,2,3,2,4] remove 2
             l       r

        '''