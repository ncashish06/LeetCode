class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        results = []
        next_expected = lower
        
        for num in nums:
            if num > next_expected:
                # Gap found: The missing range is [next_expected, num - 1]
                results.append([next_expected, num - 1])
            
            next_expected = num + 1
            
        # ap between the last number and 'upper'?
        if next_expected <= upper:
            results.append([next_expected, upper])
            
        return results
