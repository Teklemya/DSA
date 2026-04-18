# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

'''
so given a nested list with either int or list of ints or other lits i am asked to flaten it
what does inpuut look like?  [[1,1],2,[1,1]]
expected output? [1,1,2,1,1] by calling next repeatedly i can build the output 
funcion of next this returns the next int in the nestedList
funtin of hasNext this returns True or False if the 

why use a stack? i can easily pop out when i need to return when next is called and also i can easily peek in and check if the top is a int or not


I am thinking of using a stack to keep reporcessing if the top is not an int i will go into that list and expand it
so hasNext will return True if the top is an int else it will go in while the stack exisits

But with stack i need to put things in reverse order becase stack has the char of LIFO so i want to process the first elem

P - initalize a stack
    and populate the stack with the nestedList in reverse order

    Once we have the stack we can go into hasNext and while stack if the top of the stack is an int by cechking isInteger then i can just return True
    else: i will have to go deeper into that list by calling getList
    which means i will add it into the stack in reverse order again

    else if stack is empty hasNext will return False

    in the next i will return the top of the stack bydoing getInteger assumming we are calling it becuae hasNext is returnning true

'''

class NestedIterator:
    #How do I access its data? when you see an object in paramater
    #Since this is a custom object, I assume I have helper methods like isInteger() and getList() to access its contents?

    def __init__(self, nestedList: [NestedInteger]):
        #iniatlize the stack
        self.stack = []
        #populate the stack with the given nestedList
        for i in range(len(nestedList) -1, -1, -1):
            self.stack.append(nestedList[i])
    
    def next(self) -> int:
        # #now when we call next assuming hasnext will return true then we can just pop the top of the stack since it is an int
        # if self.hasNext():
        #     #then now that i will be able to get the nestedInterger object by poping i can pop and call getInteger on that object
        #     nestedInt = self.stack.pop()
            return self.stack.pop().getInteger()
        
    
    def hasNext(self) -> bool:
        #now that i have a stack
        while self.stack:
            #get the top and check if it is int
            top = self.stack[-1]
            #call the helper function to check for integer
            if top.isInteger():
                return True
            #if it is a list
            else:
                #in this case it is a list i will have to expand it and add its elem into the stack
                nestedList = self.stack.pop()
                #once i get the nestedList Object i will get the list calling the getList api
                nestedList = nestedList.getList()
                #add it back in reverse to process the first one first
                for i in range(len(nestedList) -1, -1, -1):
                    self.stack.append(nestedList[i])
        #if not stack
        return False

            
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())