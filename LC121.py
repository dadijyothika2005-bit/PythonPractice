def maxProfit(prices):
   if len(prices)<2:
         return 0
   else:
    start=0
    end=1
    diff=0
    maxres=0
    while(end<len(prices)):
      
      if prices[start]<=prices[end]:
         diff=prices[end]-prices[start]
         end+=1
      else:
         start=end
         end+=1
      maxres=max(maxres,diff)
    return maxres
prices=[7,6,4,3,1]
print(maxProfit(prices))
