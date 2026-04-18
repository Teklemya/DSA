from collections import deque #double ended queue
class Solution:
    '''
    U — Understand
        I am given a 2D grid of "1" and "0"
        "1" = land, "0" = water
        An island is land connected up, down, left, right
        I need to return the number of islands
    M — Match
        This is a graph problem in a grid
        I can use BFS or DFS
        Pattern:
        whenever I find an unvisited "1", explore all connected land
        that whole exploration = one island
    P — Plan
        Loop through every cell in the grid
        If I find a "1" that is not visited:
        start BFS/DFS
        mark all connected land as visited
        increment island count
        Return island count
    I — Implement
        Use a visited set
        Use 4 directions:
        up, down, left, right
        In BFS:
        add start cell to queue
        mark visited when added to queue
        In DFS:
        mark visited first, then recurse on neighbors
    R — Review
        Check:
        did I handle bounds correctly?
        did I only visit "1" cells?
        did I avoid revisiting cells?
        did I count one island per BFS/DFS call?
    E — Evaluate
        Time: O(rows * cols)
        Space: O(rows * cols)
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        #if not grid just return 0, make this check before all
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def dfs(row, col):
            #set up a base case
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0" or (row, col) in visited:
                return
            
            #add to visited
            visited.add((row, col))

            #if not call dfs on all 4 directions
            dfs(row + 1, col) 
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1
        return islands














        # def bfs(row, col):
        #     #initalize a queue to process the cells
        #     queue = deque()
        #     #add the row and col
        #     queue.append((row, col))
        #     visited.add((row, col))

        #     #while queue exists
        #     while queue:
        #         #we want to check the nebighors for that row and col
        #         row, col = queue.popleft()
        #         #set up directions
        #         directions = [(0,1), (1,0), (0,-1), (-1, 0)]

        #         for dr, dc in directions:
        #             #we want to explore all nebighors 
        #             nr, nc = row + dr, col + dc
        #             #check if nebrighor is inbound, if it is a 1 and not in visited meaning we have found a 1 that is connected
        #             if (nr in range(rows) and 
        #             nc in range(cols) and
        #             grid[nr][nc] == "1" and 
        #             (nr, nc) not in visited):

        #                 queue.append((nr, nc))
        #                 visited.add((nr, nc))

        # for row in range(rows):
        #     for col in range(cols):
        #         # everytime i see a new 1 i will call bfs on it to check its nebighors and add 1 to islands
        #         if grid[row][col] == "1" and (row, col) not in visited:
        #             bfs(row, col)
        #             islands += 1
        # return islands















        # rows = len(grid)
        # cols = len(grid[0])
        # visited = set()
        # islands = 0

        # if not grid:
        #     return 0

        # def bfs(row, col):
        #     #I will need a queue to keep track of the row and col to process
        #     queue = deque()
        #     queue.append((row, col))
        #     #add into visited set after adding to queue so that it doesn't get reprocessed
        #     visited.add((row, col))

        #     #I have to check if queue is empty or not becuase if empty ntn to process
        #     while queue:
        #         #now i can pop from the left of queue to process that cells nebghiors
        #         row, col = queue.popleft()
        #         #now when we are going to process that row and col we want to add it into visited becuase that is for sure a 1
        #         visited.add((row, col))

        #         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        #         for dr, dc in directions:
        #             #set up nebighors
        #             nr, nc = row + dr, col + dc
        #             #check if not out of bound, if it is 1 and not in visited
        #             if (nr in range(rows) and
        #                 nc in range(cols) and
        #                 grid[nr][nc] == "1" and 
        #                 (nr, nc) not in visited):
        #                 #this means we have found a new one that is connected with the 1 we were processing
        #                 queue.append((nr, nc))
        #                 #When I discover a neighbor, I mark THAT neighbor visited
        #                 visited.add((nr, nc))

        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == "1" and (row, col) not in visited:
        #             bfs(row, col)
        #             islands += 1
        # return islands




        '''
        Given an m x n 2D grid 
        1 -> land and 0 -> water 
        and outside the grid is also water assumabily

        I am asked to return the number of isalnds. An island is made of land that is connected horizonatlly / vertically
        i will start when i find my first 1 then i will check its nebighors if they are a 1 and not in visited i will add that
        row, col into a queue to process their nebighors until all i can find is a 0 which means i have found my first island.

        M - I am planning on using BFS to that i can go level by level and check each nebighor 
        P - if not grid return 0
            I will use a queue to keep track of the row and col
            i will have a visited set so that i don't reporcess cells
            i will have a list of the directions i can go and check for each direction
            i will call bfs on the 1's that i find not in visited
        '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # '''
    # Scan grid
    # Find a "1" → new island
    # Flood fill (BFS) → mark all connected land
    # Repeat

    # BFS explores ALL connected "1"s automatically
    # When queue is empty → island is done

    # “Whenever I find an unvisited ‘1’, I start a BFS to explore all connected land.
    # I mark all visited nodes so I don’t count them again.
    # Each BFS represents one island.”
    # '''
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     #queue should store rows and colums
    #     #get the size of rows and cols
    #     row = len(grid) 
    #     col = len(grid[0])
    #     #viisted should be a set storing a tuple (r , c)
    #     visited = set()
    #     island = 0

    #     #if grid is empty we return a 0
    #     if not grid:
    #         return 0

    #     def bfs(r,c):
    #         #i need to set up a qeueue
    #         queue = deque()
    #         #add to visited
    #         visited.add((r,c))
    #         #add into the queue
    #         queue.append((r,c))
    #         #while the queue is not empty we will pop and check the adjuacent to expand the island
    #         while queue:
    #             r, c = queue.popleft() #if i do just pop that would pop from right which is dfs removing the recently added LIFO
    #             #add the positons as tuples inorder to expand
    #             directions = [(0,1), (1,0), (-1,0), (0,-1)]
    #             #now we need to check if the adjacent / nebighor is inbound and not in visited and if it is 1
    #             for dr, dc in directions:
    #                 nr, nc = r + dr, c + dc
    #                 if (nr in range(row) and 
    #                     nc in range(col) and 
    #                     grid[nr][nc] == "1" and 
    #                     (nr,nc) not in visited): #use a bracket to hold the whole if statement
    #                     #then we will append this to the queue and again try to expand
    #                     queue.append((nr,nc))
    #                     #mark as visited
    #                     visited.add((nr,nc))

    #     #Let us treverse through the grid
    #     for r in range(row):
    #         for c in range(col):
    #             # if we find a 1 then we will call bfs on it and if 0 we don't care
    #             if grid[r][c] == "1" and (r,c) not in visited: #Don't forget to make 1 a string and not an int
    #                 #we call bfs on it
    #                 bfs(r,c)
    #                 island += 1
    #     return island


    #     '''
    #     Given a 2D grid i am asked to find number of islands
    #     land is 1 and water is 0-> an island is when ls are connected horizontally or verstically 
    #     (0,1), (1,0), (-1,0), (0,-1) are the moves we can make to check the nebighors on top, right, left and bottom
    #     wehn we get to the edge we can assume that is water 

    #     M - I am thinking of using BFS becuase i can vist all the possible nebrighors before diving deeper 
    #     and using recursion to come all the way back

    #     P - I will create a visted and a queue, visted to keep track of the 1s i already saw so that i don't count that again.
    #         then we i explore all the ways i can go and all i find is 0 then that means i have found my first island then i can go
    #         look until i find the next 1 and do the same
    #         I will only add an island when all possiblity is done at one level
    #     '''
        