# 0001 Two Sum

## Idea
Use a hash map to store visited numbers and their indices.

For each element `nums[i]`, check whether  
`target - nums[i]` already exists in the map.

If it exists, return the indices.

## Algorithm
1. Create an unordered_map
2. Iterate through the array
3. Compute complement
4. Check if complement exists
5. If yes → return indices
6. Otherwise insert current number

## Complexity

Time Complexity: O(n)  
Space Complexity: O(n)