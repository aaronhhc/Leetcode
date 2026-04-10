#my solution yet is the best solution for this problem, using two pointers to find the most water container
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        most_water = 0
        while(left < right):
            curr_most_water = (right - left) * min(height[left], height[right])
            most_water = max(curr_most_water, most_water)
            #check left or right move forward
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return most_water

        

