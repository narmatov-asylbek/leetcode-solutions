Problem #15

### Problem description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


### Test examples:
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

### Solution
We can solve this problem using hash maps. But let's discuss another approach.

Suppose, we are given sorted list. How can we solve this? We can easily solve this using two pointers method.
But, how do we eliminate duplicates? Every time we find an answer, we need to skip left and right pointers, if they are duplicates.

We need three pointers: position, left, right.

We scan list using position pointer, the left pointer is position + 1, and the right pointer - the most right(the biggest) index of the list

If sum of elements left, right, and positions is less than zero, then we need to increase left. If greater, then we need to move right to left.
Else we need to add this elements to answer list.

### Code solution
```python
from typing import List

# Space complexity: O(n)
# Time complexity: O(n^2)
def three_sum(nums: List[int]):
    nums.sort()

    answers = []

    for position in range(len(nums)):
        left, right = position + 1, len(nums) - 1
        if position > 0 and nums[position] == nums[position - 1]:
            continue

        while left < right:
            current_answer = nums[left] + nums[right] + nums[position]
            if current_answer == 0:
                answers.append([nums[left], nums[right], nums[position]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_answer < 0:
                left += 1
            else:
                right -= 1
    
    return answers

```

### Analysis

We use additional space for answers, so the space complexity will be O(N).
For time complexity: We sorted list in-place, which I believe is O(n log n). Also in every iteration, we need to scan list from position + 1 to right, so it's O(n^2). O(n^2) > O(n log n). So, The time complexity will be O(n^2)