class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        '''
        output = [17,13,11,2,3,5,7]
        sorted_desck = [2, 3, 5, 7, 11, 13, 17]
        ---------------------------------------------
        queue = [0,1,2,3,4,5,6]
        resulr = [0,0,0,0,0,0,0]
        result[qpop()0]  = 2
        qpop(1) and append it last  [2,3,4,5,6,1]
        result[2] = 3
        q - [4,5,6,1,3]
        result[4] = 5
        q - [6,1,3,5]
        res[6] = 7
        q - [3,5,1]
        res[3] = 11
        q - [1,5]
        res[1] = 13
        q - 5
        res[5] = 17
       res = { 2,13,3,11,5,17,7]}


        '''
        n = len(deck)
        deck.sort()
        print(deck)
        
        q = deque()
        for i in range(n):
            q.append(i)
        
        result = [0] * n
        for i in range(n):
            result[q.popleft()] = deck[i]
            if q: q.append(q.popleft())
        
        return result