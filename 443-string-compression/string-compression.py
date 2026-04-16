class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0   # where we write compressed output
        left = 0    # start of current group

        while left < len(chars):
            right = left

            # move right until the group ends
            while right < len(chars) and chars[right] == chars[left]:
                right += 1

            count = right - left

            # always write the character once
            chars[write] = chars[left]
            write += 1

            # if count > 1, write each digit of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            # move to the next group
            left = right

        return write

        '''
        Given a str array chars: I am asked to compress this array by writing an algo
            That groups consective repeating chars in chars:
                if groups count is 1 append the char to s
                else append char + groups count
        I can not store s on its own becuase i can not use extra space so i will have to modify chars array as i go
        I was planning to use two pointers that start at index 0 and if left and right are equal move the pointer right
        and update count by right - left + 1 else case move the left 
        inorder to update in place i might need to do some replace i can do if count > 1: then i need to append the char
        and count  
        ["a","a","b","b","c","c","c"] 
        ["a" "2" "]
        '''
        