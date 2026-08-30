class Solution:
    # Date Solved: 29 August 2026, Saturday, POTD
    # Refer: codestorywithMIK
    # In NC All
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        # Approach-1: Brute force
        # Time: O(n^3), Space: O(1)
        n = len(nums)

        for i in range(n):
            while True:
                smallValue = nums[i]
                idx = -1

                for j in range(i + 1, n):
                    if abs(nums[i] - nums[j]) <= limit:
                        if nums[j] < smallValue:
                            smallValue = nums[j]
                            idx = j

                if idx != -1:
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    break

        return nums
        """
        # Approach-2: Using sorting and grouping using unordered_map
        # NeetCode's solution is same as this.
        # Time: O(n*logn), Space: O(n)
        n = len(nums)

        vec = sorted(nums)

        groupNum = 0
        numToGroup = {}
        groupToList = defaultdict(deque)

        numToGroup[vec[0]] = groupNum
        groupToList[groupNum].append(vec[0])

        for i in range(1, n):
            if abs(vec[i] - vec[i - 1]) > limit:
                groupNum += 1

            numToGroup[vec[i]] = groupNum
            groupToList[groupNum].append(vec[i])

        result = [0] * n
        for i in range(n):
            num = nums[i]
            group = numToGroup[num]
            result[i] = groupToList[group].popleft()

        return result
