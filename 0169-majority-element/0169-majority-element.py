class Solution:
    # Date Solved: 19 May 2026, Tuesday
    # NeetCode 250
    def majorityElement(self, nums: List[int]) -> int:
        """
        # Approach 1: HashMap
        # Time: O(n), Space: O(n)
        majority = len(nums) / 2
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            if count[num] > majority:
                return num

        # Approach 2: Sorting
        # Time: O(nlogn), Space: O(1)
        nums.sort()
        return nums[len(nums) // 2]
        """
        # Approach 3: Boyer-Moore Voting Algorithm (It assumes that there is definitely a majority element (frequency greater than n/2 times) in the array)
        # Time: O(n), Space: O(1)
        # Approach: res = current candidate for majority
        # count = "lead" the candidate has over all other elements seen so far
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num  # initially assume first element is the majority element
            if num == res:
                count += 1
            else:
                count -= 1
        return res
