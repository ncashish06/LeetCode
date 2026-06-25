class Solution:
    # Date Solved: 25 June 2026, Thursday, POTD
    # Refer: codestorywithMIK
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            balance = 0
            for j in range(i, n):
                # +1 if target, -1 otherwise
                if nums[j] == target:
                    balance += 1
                else:
                    balance -= 1

                # balance > 0 means target appears more than half the time
                if balance > 0:
                    count += 1

        return count
