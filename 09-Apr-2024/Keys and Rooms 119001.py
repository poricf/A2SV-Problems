# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = set()
        visited.add(0)
        q = deque()
        q.append(0)
        while q:
            print(q)
            for i in range(len(q)):
                room = q.popleft()

                for key in rooms[room]:
                    if key not in visited:
                        q.append(key)
                        visited.add(key)

        
        return len(visited) == len(rooms)
            
