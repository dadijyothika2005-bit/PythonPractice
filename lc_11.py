def maxArea(heights):
        if len(heights)<=1:
            return 0
        l,r=0,1
        maximum=0
        area=0
        while l<r and r<len(heights):
            if heights[r]>heights[l] and l<r:
                  area=(r-l)*heights[l]
                  l=r
                  r+=1
            else:
                 area=(r-l)*heights[r]
                 r+=1
            maximum=max(maximum,area)
        return maximum
heights=[1,2,7,4,500,500,7,8,3]
print(maxArea(heights))