class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #P - handle the edge case first
        if not intervals:
            return 0

        #sort by start 
        startTime = sorted(interval[0] for interval in intervals)
        print(startTime)
        #sort by end time
        endTime = sorted(interval[1] for interval in intervals)
        print(endTime)

        minRoom, room = 0, 0
        s, e = 0, 0

        while s < len(startTime):
            #now take the min between start time and end time at that point
            if startTime[s] < endTime[e]:
                room += 1
                s += 1
            else:
                room -= 1
                e += 1
            minRoom = max(minRoom, room)
        return minRoom

        #now do a two pointer apporach 
        #where we take the min between start and end and move that pointer
        #if we choose start -> need a room += 1
        #if we choose end -> we just got a room freed room -= 1
        #if we have a tie then we pick the end and move pointer
        #keep track of max rooms we had a moment

    
        



    '''
    Given a array of intervals, wehre itervals i is [start,end] return the minmum number of rooms
    input = [[0,30],[5,10],[15,20]]?
    sort by end is [[5,10], [15,20], [0,30]]

    case 2:
        [[2,4], [7,10]]

    can the end time be 0? No so it is 1 or above
    if interval is empty? return 0 for rooms? 
    
    How many overlapping meetings at a time?

    at any point in time we keep track of rooms by seeming how many meeting ends 


    | ------------------------------------------------------------------ |  
0                                                                       30
            5 |-----------| 10 
                                    15 -------------- 20

initally meeting 1 starts so room = 1 and the at 5 mins mark meeting 2 starts now we have to add to rooms + 1
then at min 10 meeting ends meaning room -= 1 then another starts at 15 which will add 1 to rooms = 1 + 1 = 2

we sort the start my itself and the end on its own
start = [0, 5, 15]
                Sp
end =   [10, 20, 30]
            Ep
the use two pointers and we take the min between the two either startP or endP 

iniatlly between 0 and 10 we take 0 which is the min and add to the room becuase meeting is started
then move Sp to 5 and 5 is still less than 10 so add on rooms and move Sp to 15
now sp > ep so room - 1 meaning meeting has ended now we move ep room = 2 - 1 = 1
and then we take 15 than 20 and add to rooms = 1 + 1 = 2 and make sure to keep track of minRooms 
once we finish start we are done
what if we have a tie? like 10 and 10? we will choose the ep 



if Sp < Ep:
    rooms += 1
    sp += 1
else:
    rooms -= 1
    ep -= 1

minRoom = max(minRoom, rooms)

keep track of rooms 
'''