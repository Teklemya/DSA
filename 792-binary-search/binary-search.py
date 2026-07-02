class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            #Get the middle
            mid = (left + right) // 2
            #Check if the number in middle index is equal to target
            if nums[mid] == target:
                return mid
            #Check if the target is more than mid then move the right down
            if nums[mid] > target:
                right = mid - 1
            #Move the left above mid becuase mid is already accounted for
            else:
                left = mid + 1
        return -1


        '''
        U - Given a sorted array I am asked to find if target is in the given array and if not return 
            -1
        M - I can treverse through the array directly from the first element to the last to the end and see if i 
            have found it and then return the index of that elem

            However using a binary search apporach would be better becuase that way i can divide and conquer
            
        P - Since it is sorted i can cut it in half and if the middle is > target then it is on the left side
            else on the right then middle will be c

            So i will start left = 0 and right = len(nums) - 1 

            while the left < right:
                now i caa calculate the mid which is left + right // 2
                if mid == target:
                    return mid
                elif mid > target: 
                    right = mid - 1
                else:
                    left = mid + 1

            Finally return -1 if we are done
        '''