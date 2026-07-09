class Solution:
    # Date Solved: 9 July 2026, Thursday
    # NC250
    # Refer: Namaste DSA

    # Heap Sort
    # Time: O(n log n) best/avg/worst
    # Space: O(1)
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # create a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapifyDown(nums, i, n)

        # sort the array
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapifyDown(nums, 0, i)

        return nums

    def heapifyDown(self, arr, i, n):
        largest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapifyDown(arr, largest, n)

    """
    # Merge Sort
    # Time: O(n log n) best/avg/worst
    # Space: O(n) — auxiliary arrays for merging
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

    # Quick Sort
    # Time: O(n log n) best/avg, O(n^2) worst (already-sorted input with last-element pivot causes worst-case unbalanced splits)
    # Space: O(log n) avg recursion stack, O(n) worst case
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def findPivotIndex(self, arr, startIndex, endIndex):
        pivot = arr[endIndex]
        pos = startIndex - 1

        for i in range(startIndex, endIndex):
            if arr[i] < pivot:
                pos += 1
                arr[i], arr[pos] = arr[pos], arr[i]

        arr[pos + 1], arr[endIndex] = arr[endIndex], arr[pos + 1]
        return pos + 1

    def quickSort(self, arr, startIndex, endIndex):
        if startIndex < endIndex:
            pivotIndex = self.findPivotIndex(arr, startIndex, endIndex)
            self.quickSort(arr, startIndex, pivotIndex - 1)
            self.quickSort(arr, pivotIndex + 1, endIndex)
            return arr

    # Counting Sort (stable)
    # Time: O(n + k), k = value range (max_val - min_val)
    # Space: O(n + k)
    # Note: Original code only works for non-negative integers; k should be bounded/reasonable relative to n, or space blows up.
    # To allows negatives (-5*10^4 to 5*10^4), values are offset by min_val to stay within bounds.
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.counting_sort_stable(nums)

    def counting_sort_stable(self, arr):
        if not arr:
            return arr

        min_val = min(arr)
        max_val = max(arr)
        range_size = max_val - min_val + 1

        count = [0] * range_size
        for x in arr:
            count[x - min_val] += 1

        prefix = [0] * range_size
        prefix[0] = count[0]
        for i in range(1, range_size):
            prefix[i] = prefix[i - 1] + count[i]

        sorted_arr = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            idx = curr - min_val
            sorted_arr[prefix[idx] - 1] = curr
            prefix[idx] -= 1

        return sorted_arr

    # Radix Sort (uses digit-wise stable counting sort)
    # Time: O(nk), k = number of digits in max shifted value
    # Space: O(n + k)
    # Note: Original code assumes non-negative integers.
    # To allow negatives, all values are shifted up by abs(min_val) before sorting, then shifted back after.
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.radixSort(nums)

    def countingSortStable(self, arr, e):
        count = [0] * 10

        for x in arr:
            digit = (x // e) % 10
            count[digit] += 1

        for i in range(1, len(count)):
            count[i] = count[i] + count[i - 1]

        sortedArr = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            curr = (arr[i] // e) % 10
            x = count[curr]
            sortedArr[x - 1] = arr[i]
            count[curr] -= 1

        for i in range(len(arr)):
            arr[i] = sortedArr[i]

    def radixSort(self, arr):
        if not arr:
            return arr

        offset = -min(arr) if min(arr) < 0 else 0
        shifted = [x + offset for x in arr]

        max_val = max(shifted)
        e = 1
        while max_val // e > 0:
            self.countingSortStable(shifted, e)
            e *= 10

        return [x - offset for x in shifted]
    
    # Bucket Sort
    # Time: O(n + k) avg (k = number of buckets), O(n^2) worst (all elements land in one bucket)
    # Space: O(n + k)
    # Note: assumes input is floats uniformly distributed in [0, 1). index = int(x * n) requires x in [0, 1) to stay in bounds.
    # Bucket general integers (including negatives) by scaling each value's position within [min_val, max_val] into a bucket index.
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucketSort(nums)

    def bucketSort(self, arr):
        if not arr:
            return arr

        n = len(arr)
        min_val, max_val = min(arr), max(arr)

        if min_val == max_val:
            return arr

        bucket_count = n
        bucket_size = (max_val - min_val) / bucket_count
        buckets = [[] for _ in range(bucket_count + 1)]

        for x in arr:
            index = int((x - min_val) / bucket_size)
            index = min(index, bucket_count)  # clamp for max_val edge case
            buckets[index].append(x)

        for bucket in buckets:
            bucket.sort()

        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result
    """
