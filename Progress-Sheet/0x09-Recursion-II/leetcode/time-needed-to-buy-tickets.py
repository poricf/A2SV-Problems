class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque()

        for person in range(n):
            q.append(person)
        
        time = 0

        result = [0 for _ in range(n)]

        while q:
            person = q.popleft()
            tickets[person]-= 1
            time += 1
            result[person] = time

            if tickets[person] > 0:
                q.append(person)
        
        return result[k]

        #time complexity = 0(n)
        #space complexity  O(n)
