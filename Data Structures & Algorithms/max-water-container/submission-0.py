class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        right=len(heights)-1
        left=0
        while left<right:
            width=right-left
            high=min(heights[left],heights[right])
            current_area=width*high
            if current_area>area:
                area=current_area
            
            if high<heights[right]:
                left+=1
            else:
                right-=1
        return area