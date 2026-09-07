class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                index=stack.pop()
                height=heights[index]
                
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                
                area=height*width
                maxarea=max(maxarea,area)

            stack.append(i)

        i = len(heights)
        while stack:
            index=stack.pop()
            height=heights[index]

            if stack:
                width=i-stack[-1]-1
            else:
                width=i

            area=height*width
            maxarea=max(maxarea,area)

        return maxarea
            