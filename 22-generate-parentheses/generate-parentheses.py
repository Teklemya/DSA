class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openC, closeC):
        # a parenthesis valid if i end up with openC == closeC == n
            if openC == closeC == n:
                #i have valid parenthesis i can go ahead and join and append
                res.append("".join(stack))
        #i can add an open when openC < n
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closeC)
                stack.pop()
        #if closeC < openC i can add a close
            if closeC < openC:
                stack.append(")")
                backtrack(openC , closeC + 1)
                stack.pop()
        #since initally both counts are 0
        backtrack(0, 0)
        return res

    '''
    given n pairs of parenthnes which is " ( " " ) " * n generate all combinations of well formed parthneses

    so if n = 2 we have 2 open and 2 close

    output = ["(())", "()()"]

                                []
                                [(]  
                            [()]   [((]       
                        [()(]        [(()] 
                    [()()]               [(())]

    a parenthesis valid if i end up with openC == closeC == n
    i can add an open when openC < n
    if closeC < openC i can add a close

    M - using a stack to add the ( or )
        res array to keep trakc of the valid parenthesis by joining the stack 

        backtracking on the openC and closeC
            #if openC == closeC == n
                #join the stack and append

            if openC < n:
                #add an open to the stack and update the count and backtrack
                stack.append("(")
                backtrack(openC + 1, closeC)
                #everytime we are done backtracking we pop
                stack.pop()
            if closeC < openC:
                stack.append(")") 
                backtrack(openC , closeC + 1)
                stack.pop()

        pass in inital open adn close 
        backtrack(0, 0)
        return res

    '''