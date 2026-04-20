class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        vertical = 0
        maxArea = 0

        while l < r:
            if height[l] <= height[r]:
                vertical = height[l]
                area = vertical * (r - l)
                maxArea = max(maxArea, area)
                l += 1
            else:
                vertical = height[r]
                area = vertical * (r - l)
                maxArea = max(maxArea, area)
                r -= 1
        return maxArea

        '''
        U - Given heights of the vertical lines, i need to keep track of the two vertical lines that can contain the most amount of 
            water
        M - use two pointers to keep track of the mimumum from the two pointers then multiple by the right - left to get area
            keep track of the max
        P - left = 0
            right = len(height) - 1
            maximumArea = float('-inf')
            vertical = 0

            while left < right:
                check which one is smaller
                if height[left] <= height[right]:
                    vertical = height[left]
                    area = vertical * (right - left)
                    maximumArea = max(maximumArea, area)
                else:
                    vertical = height[right]
                    area = vertical * (right - left)
                    maximumArea = max(maximumArea, area)
            return maximumArea
        E - Space is O(1)
            Time
        '''