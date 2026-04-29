class Solution:
    def makeGood(self, s: str) -> str:
        '''
        I use a stack to keep building the good string. For each character, I compare it with the top of the stack. If they are the same letter but different case, 
        that forms a bad adjacent pair, so I pop the stack. Otherwise, I push the current character. At the end, joining the stack gives the final good string.
        '''
        stack = []
        for char in s:
            #since we are only checking for one lower and then Cap or vice versa and we don't care about two lowers side by side stack[-1] != char is key 
            if stack and stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)

        #Once i have cleaned up the given string into a good string by removing the chars that have an adj of upper or lower i will rejoin the string
        goodString = "".join(stack)
        return goodString
        '''
        U - Given a s of lower and upper case english letter
            a good string doesn't have an adjaucent two chars that are the same but one in small and one i caps
            remove these two chars that are bad adn keep doing that until the s is good
            return the good string even i empty

        M - Stack
        P - Base case if not s:
                return "
            I will start iterating the string for each char in s:
            I will check if stack and stack[peek] == lower(char) || upper(char):
                stack.pop()
            else:
                stack.append(char)
            while stack:
                goodString = "".join(stack.pop)
            return goodString
        '''
        