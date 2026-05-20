class Solution:
    # Date Solved: 19 May 2026, Tuesday
    # Refer: codestorywithMIK
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Approach 1: (Optimal Approach)
        # Time : O(n), Space : O(n)
        n = len(A)
        result = []
        mp = defaultdict(int)
        count = 0

        for i in range(n):
            mp[A[i]] += 1
            if mp[A[i]] == 2:
                count += 1

            mp[B[i]] += 1
            if mp[B[i]] == 2:
                count += 1

            result.append(count)

        return result

        """
        # Approach 2: Found in comments
        # Time : O(n), Space : O(n)
        # Intuition: At index i, we insert (i+1) elements from A and (i+1) elements from B. Total insertions attempted = 2*(i+1).
        # A set only stores UNIQUE elements, so if a number appears in both A and B, it gets inserted twice but stored once("absorbed")
        # Each common element shrinks the set by 1 compared to total insertions: set.size() = 2*(i+1) - common_count
        # Therfore, common_count  = 2*(i+1) - set.size()
        
        s = set()
        result = []

        for i in range(len(A)):
            s.add(A[i])
            s.add(B[i])

            result.append(2 * (i + 1) - len(s))

        return result

        # Approach 3:
        # Time : O(n^2), Space : O(n)
        n = len(A)
        result = []
        is_present_a = [False] * (n + 1)
        is_present_b = [False] * (n + 1)

        for i in range(n):
            is_present_a[A[i]] = True
            is_present_b[B[i]] = True

            count = 0
            for num in range(1, n + 1):
                if is_present_a[num] and is_present_b[num]:
                    count += 1

            result.append(count)

        return result

        # Approach 4: Brute Force
        # Time : O(n^3), Space : O(1)
        n = len(A)
        result = []

        for i in range(n):
            count = 0

            for x in range(i + 1):  # iterate A up to i
                for y in range(i + 1):  # iterate B up to i
                    if B[y] == A[x]:
                        count += 1
                        break

            result.append(count)

        return result
        """
