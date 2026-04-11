from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        #build the preMap to map each course to its prereq
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        #initalize dfs on that course
        def dfs(crs):
            #if this crs is in visiting w
            if crs in visiting:
                return False
            #check if the value of this course is empty / no other pre-req
            if preMap[crs] == []:
                return True
            #else add into the visiting set
            visiting.add(crs)
            #if crs has pre-reqs then call dfs on that crs pre-req 
            for preq in preMap[crs]:
                #when i run dfs if i get False at any of the preqs
                if not dfs(preq):
                    return False
            #if all prereqs can be done it is no longer in the dfs path so i can remove it from the visiting set
            visiting.remove(crs)
            #if all are true that means i can compelete this course -> update value to []
            preMap[crs] = []
            return True
        #now incase we have sth like [0,1] [2,3] a graph that is not connected i need to run dfs on all course in numCourses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



        


        '''
        U — Understand
            You are given:
            numCourses (total number of courses)
            prerequisites → [course, prereq]
            Meaning:
            To take course, you must first take prereq
            Goal:
            Return True if you can finish all courses
            Return False if it’s impossible

            Key idea:

            If there is a cycle, you cannot finish

        M — Match (Pattern Recognition)

            Ask:

            Is this a graph? → Yes
            Type? → Directed graph
            What am I checking? → Cycle detection

            Pattern:

            DFS + cycle detection using a recursion stack

        P — Plan
            Build adjacency list:
            course → list of prerequisites
            Use DFS for each course
            Track states:
            visiting → nodes in current DFS path
            DFS logic:
            If node in visiting → cycle → return False
            If no prereqs → return True
            Add node to visiting
            DFS all neighbors
            Remove from visiting
            Mark as done (preMap[crs] = [])
            Return True
            Run DFS on all courses:
            If any fails → return False
            Otherwise → return True

        I — Implement (Mental Checklist)
        
            defaultdict(list) for graph
            visiting = set()
            Recursive DFS function
            Loop through all courses
            Careful with:
            removing from visiting at correct time
            not returning early in loop

        R — Review

            Ask yourself:

            Did I detect cycles correctly?
            Did I process all courses?
            Did I avoid returning too early?
            Did I remove from visiting AFTER exploring neighbors?

        E — Evaluate
            Time: O(V + E)
            Space: O(V + E)

            V = courses, E = prerequisites

            One-line summary (remember this)

            “I use DFS with a visiting set to detect cycles in a directed graph. 
            If a node appears again in the current path, there is a cycle.”

            Quick mental trigger for interviews

            When you see:

            prerequisites
            dependencies
            ordering

            Think immediately:

            Graph + cycle detection

        '''