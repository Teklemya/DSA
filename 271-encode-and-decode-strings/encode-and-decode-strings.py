class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        """ 
        How do we know where one string ends and another starts? if we use an ascii char as a delimiter the issue is 
        ["leet", "co#de"] assume we use # as the delimeter we will end up with leet#co#de -> leet, co, de which is wrong

        so what if we knew how many of the charcters go into the first string and next... by looking at encoded str
        we can put the length of the str infornt so 4leet 4code but the issue is we need to know that the 4 is length and not part of the str
        so we can add a delimiter in between 4#leet4#code that way the moment we see a number followed by # we will convert to an int and 
        add the char after the pound sign into the first string

        """
        #solution 1
        #we can use a non ascii char since the input is only ascii chars
        # encoded_string = "é".join(strs)
        # return encoded_string

        #solution 2
        #let us encode the strs by adding the len of the str infront of the str followed by # and str
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        #print(encodedStr)
        return encodedStr


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        #solution 1
        #we spilit using non ascii char
        # decoded_string = s.split("é")
        # return decoded_string

        #solution 2 
        #we need to read the first number followed by # as the len and first str will be whatever the len is after that # and appened to list
        #
        res = []
        i = 0 
        #as long as we are in range we will decode char by char 
        while i < len(s):
            #we will need a pointer to know where the delimeter is in case of 12 is len so we won't assume len is s[0]
            j = i
            while s[j] != "#":
                j += 1
            #now we have reached the delimiter, len of word is from i to j + 1, we want to grab the str after deleimiter size of that len
            length = int(s[i:j])
            #the string we want to add to result is from # + 1 and ends before the next int / length
            startString = j + 1
            endString = startString + length
            res.append(s[startString:endString])
            #finally update the i pointer to the next int if it exists
            i = endString
        return res



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))