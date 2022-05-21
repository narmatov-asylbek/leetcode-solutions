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
