class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Given a roman numeral represtend in I, V, X, L, C, D, M with a value i will be given an input of roman numerals like III
        i will need to return the numeral value, i need to keep in mind for example if i see an I before a V 
        or an X before then that is substrctaion or if i see X before L and C that is substruction and same with C

        now if can iterate through the string i am given and before computing i will check s[i] and s[i + 1] if i is I, X, C and s[i + 1] is 

        '''
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        #now that i have the map i can iterate through the string
        for i in range(len(s)):
           #check bound and if the s[i] is lower in value that the next if so then substract else add
            if i < len(s) - 1 and romanMap[s[i]] < romanMap[s[i + 1]]:
                result -= romanMap[s[i]]
            else:
                result += romanMap[s[i]]
        return result

            