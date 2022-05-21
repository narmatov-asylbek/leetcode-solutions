from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    counter = 0
    curr_sum = 0
    hash_map = {}

    hash_map[0] = 1

    for pos in range(len(nums)):
        curr_sum += nums[pos]

        if (curr_sum - k) in hash_map:
            counter += hash_map[curr_sum - k]
        if curr_sum in hash_map:
            hash_map[curr_sum] += 1
        else:
            hash_map[curr_sum] = 1
    
    return counter

