class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = float(inf)

        for price in prices:
            minBuy = min(minBuy, price)
            profit = price - minBuy
            maxProfit = max(maxProfit, profit)
        return maxProfit

        '''
        U - So i can buy at any day and sell at any day in the future 
            return the max profit i can achive

            if can not active any profit what do i return? 0?

            prices = [7,3,1] = 0
                    [8,9,1,2] = 1

        M - Single traversal

        P - i can KEEP track of a maxProfit, my i - minBuy
            minBuy = float(inf) and comapre with i and take the min

        '''


























        # maxProfit = 0
        # minPrice = float(inf)
        
        # # iterate through the prices array
        # for price in prices:
        #     #first check if price is less than minPrice 
        #     if price < minPrice:
        #         #if so update minPrice
        #         minPrice = price
        #     #then now check if price - minPrice is > maxProfit:
        #     if price - minPrice > maxProfit:
        #         maxProfit = max(maxProfit, price - minPrice)
        # return maxProfit
        


        # '''
        # U - Given prices: stcok price on that day, i can buy and sell in the future. the goal is to 
        #     calucate the max profit i can make if there is no profit just return 0
        # M - Single iteration / pass then check if price is minium and then calaute the profit if price > 
        #     minPrice then i will calaucte the profit and update it and finally i will have max profit
        # P - maxProfit = 0
        #     minPrice = float(inf)
            
        #     iterate through the prices array
        #         first check if price is less than minPrice 
        #             if so update minPrice
        #         then now check if price - minPrice is > maxProfit:
        #             maxProfit = max(maxProfit, price - minPrice)
        #     finally return maxProfit
        # '''



















        # minPrice = float(inf)
        # maxProfit = 0

        # for price in prices: # 7 , # 1, 5, 3, 6
        #     if price < minPrice: 
        #         minPrice = price # 7, 1, 
        #     elif price - minPrice > maxProfit: 
        #         maxProfit = price - minPrice # 4, 5
        # return maxProfit # 5


        # for price in prices: # 7, 1, 5, 3, 6
        #     minPrice = min(minPrice, price) #7 , 1, 1, 1, 1
        #     profit = price - minPrice # 7 - 7 = 0 1 - 1 = 0 , 4, 2, 5
        #     maxProfit = max(maxProfit, profit) #(0,0) = 0 = 0, 4, 4, 5
        # return maxProfit









        # buy, sell, lastDay = 0, 1, len(prices) - 1
        # maxProfit = 0
        # while sell <= lastDay:
        #     if prices[buy] > prices[sell]:
        #         sell += 1
        #     elif prices[buy] < prices[sell]:
        #         sellPrice = prices[sell] - prices[buy]
        #         maxProfit = max(maxProfit, sellPrice)
        #         sell += 1
        #     buy += 1
        # return maxProfit


        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[i] > prices[j]:
        #             j += 1
        #         else:
        #             profit = prices[j] - prices[i]
        #             maxProfit = max(maxProfit, profit)
        # return maxProfit





        # buy, sell, lastDay = 0, 1, len(prices) - 1
        # maxProfit = 0
        # while sell <= lastDay:
        #     if prices[buy] > prices[sell]:
        #         sell += 1
        #     elif prices[buy] < prices[sell]:
        #         sellPrice = prices[sell] - prices[buy]
        #         maxProfit = max(maxProfit, sellPrice)
        #         sell += 1
        #     buy += 1
        # return maxProfit
        '''
        U - given prices array inculding prices of stock
            check what the best day to buy and sell is then return
            maxmimum profit if no profit return 0
            Edge cases: could it be [] if so 0
        M - if i have three pointers, 
            One that will be buy date, and another that will check future sell dates and compare based of a conditon 
            and udpates max profit until it reaches last date
            [7,1,5,3,6,4]
             *         -
                       $        
            if buy and sell satrt at index 0, 1
            lastDay is len(price) - 1
            maxprofit = 0
            while sell <= lastDay:
                if prices[buy] > prices[sell]:
                    sell += 1
                elif prices[buy] < prices[sell]:
                    sellPrice = prices[sell] - prices[buy]
                    maxProfit = max(maxProfit, sellPrice)
                    sell += 1
                buy += 1
            return maxProfit
        '''    














        # prices = [7,1,5,3,6,4]
        # left = 0
        # right = len(prices) - 1
        # maxProfit = 0      
        # while left <= right:
        #     if prices[left] > prices[right]:
        #         right -= 1
        #     else:
        #         profit = prices[right] - prices[left] #1, #5
        #         maxProfit = max(maxProfit, profit)
        #         right -= 1
        # left += 1
        # return maxProfit
        
        
        
        





        
        
        
        
        
        
        
        
        
        # result = 0
        # price = prices[i]
        # for i in range(len(prices) -1, -1, -1):
        #     result = price 




        '''
        So given array of price each index is the price of stock on that day [0,1,2...]
        We want to return the max return we can get by buying low and selling high, if we can not do that just return 0
        You can only sell in the future / can't iterate back the array
        
        
        '''

        