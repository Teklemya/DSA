from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            #when you sort word it will be a list so we have to use a join "" to join back to an empty string
            sortedWord = "".join(sorted(word))
            #since we have defaultdict that aalready set up a key so we can just append if it exisits it will add it to the list
            anagram[sortedWord].append(word)
            #this is list of list 
        return list(anagram.values())

        # result = []
        # for value in anagram.values():
        #     result.append(value)
        # return result
        '''
        Complexity

        Let:
        n = number of words
        k = average word length

        Then:
        Sorting each word: O(k log k)
        For all words: O(n · k log k)
        Space: O(nk)
        '''


        '''
        Given an arr of strs group the anagrams : the words that can be rearranged to create the another word
        I am thinking of sorting the str and checking if it is in a str or not
        if it is then i will that to anagram[sorted].append(str)
        else anagram[sorted] = [str]

        for key and value in the anagrams
            result.append(value)
        return result           
        '''


























        # anagrams = defaultdict(list)
        # for s in strs:
        #     #since strings are immuatable i have to treat the char like a sorted list and join them back and reassign into new str
        #     sortedS = "".join(sorted(s))
        #     # if the sorted value is in the dict then just append the str into the list
        #     if sortedS in anagrams:
        #         anagrams[sortedS].append(s) 
        #     # if this is first time seeing the sortedS / key then assign the key with a list of string 
        #     else:
        #         anagrams[sortedS] = [s]
        # print(anagrams)
        # return list(anagrams.values())
        '''
        U - Given a list of strings i need to find those that are anagrams and then return them grouped
            If i get [tea, cat, hat, eat] is should return [[tea, eat], [cat], [hat]]
            so if there is no anagram just return that string in a list
            Edge case if i am given an empty lust then what do i return? empty list? yes
        M - I am thinking of using a dict to keep track of the keys which are going to be the sorted values of that string
            espcifically a defaultdict becuase i can initalize a list without having a key
        P - Once i initalize the defaultdict
            I can iterate through the list of strings and for each string i will sort and check if that key in the dict

            i will append the key (sorted) and value the s but value is going to be a list
            so i will have sth like 
            [tea, cat, hat, eat]
            [act, aet, aet, aht] 
            the dict will look like {aet:[tea, eat], act:[cat], aht:[hat]}
            return the value in dict as a list(anagram.values())

        '''

























        '''
        U - Given an array of strings, group the anagrams togther and then return them in any order List[list[]]
            Edge case: what happens if list is [] return []
        M - HashTable
            ["tea", "eat","tan", "bat"]
            charCount = {char: count} {t : 1, e: 1,  a: 1 }, {e: 1, a:1, t: 1}, {t:1, a:1, n:1}
            strDetail = {"tea" : charCount = { t : 1, a: 1, e: 1}, "eat": {e: 1, a:1, t: 1}, "tan" : {t:1, a:1, n:1}}
            anagram = {}
            anagrams = []
        p - iniatalize anagram = []
            for str in strs: 
                # itertae through char in str and build charCount dict
                for char in str
                    charCount[char] = charCount.get(char, 0) + 1
                # if str charCount matches with an other str value then those are anagrams
                if strDeatils and charCount in strDetails.values():
                    anagram[]
                    strDetail[str] = charCount

                    
                    
                    
                    if strDetail[str] == strDetails.values()
                        anagram.append(str)
                    else:
                        anagram.append(str)
                   
            return anagrams
        '''