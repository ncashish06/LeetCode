class Solution:
    # Date Solved: 15 July 2026, Wednesday
    # NC250
    # Refer: codestorywithMIK for both approaches. 1hr video. NeetCode's approach is same as Approach 2.
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        # Approach 1: Brute Force - Do as said
        # Time: O(mlogm + m*n), n = number of rooms, m = number of meetings
        # Space: O(n)

        meetings.sort(key=lambda x: x[0])

        rooms_used_count = [0] * n  # how many times each room is used
        last_available_at = [0] * n  # when each room next frees up

        for start, end in meetings:
            found = False
            early_end_room_time = float("inf")
            early_end_room = 0

            # find first available room (lowest index, free by 'start')
            for room in range(n):
                if last_available_at[room] <= start:
                    found = True
                    last_available_at[room] = end
                    rooms_used_count[room] += 1
                    break
                # track room that frees up earliest, in case none are free
                if last_available_at[room] < early_end_room_time:
                    early_end_room = room
                    early_end_room_time = last_available_at[room]

            if not found:
                # delay meeting: keep same duration, push onto earliest-freeing room
                duration = end - start
                last_available_at[early_end_room] += duration
                rooms_used_count[early_end_room] += 1

        # find room with max bookings (lowest index wins tie, since we use strict >)
        result_room, max_use = -1, 0
        for room in range(n):
            if rooms_used_count[room] > max_use:
                max_use = rooms_used_count[room]
                result_room = room

        return result_room
        """
        # Approach 2: Use priority Queue to find the first available meeting room
        # Time: O(mlogm + m*log(n)), n = number of rooms, m = number of meetings
        # Space: O(n)
        meetings.sort(key=lambda x: x[0])

        rooms_used_count = [0] * n

        used_rooms = []  # min-heap of (end_time, room) -- rooms currently occupied
        available_rooms = list(range(n))  # min-heap of free room numbers
        heapq.heapify(available_rooms)

        for start, end in meetings:
            # free up any rooms whose meetings have ended by 'start'
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                # lowest-numbered free room takes this meeting
                room = heapq.heappop(available_rooms)
                heapq.heappush(used_rooms, (end, room))
                rooms_used_count[room] += 1
            else:
                # no free room: delay on the room that frees up earliest
                end_time, room = heapq.heappop(used_rooms)
                duration = end - start
                heapq.heappush(used_rooms, (end_time + duration, room))
                rooms_used_count[room] += 1

        result_room, max_use = -1, 0
        for room in range(n):
            if rooms_used_count[room] > max_use:
                max_use = rooms_used_count[room]
                result_room = room

        return result_room
