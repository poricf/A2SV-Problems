class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        using two queues for R and D then who apears first will go back to the queue
        time - O(n)
        space - O(n)
        '''
        n = len(senate)
        Rqueue = deque()
        Dqueue = deque()

        for i,senator in enumerate(senate):
            if senator == 'R':
                Rqueue.append(i)
            else:
                Dqueue.append(i)
        
        while Rqueue and Dqueue:
            a = Rqueue.popleft()
            b = Dqueue.popleft()
            if  a < b :
                Rqueue.append(a+n)
            else:
                Dqueue.append(b+n)
        
        if Rqueue: output = "Radiant"
        else: output = "Dire"

        return output

        