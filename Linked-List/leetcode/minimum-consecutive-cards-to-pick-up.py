class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards))==len(cards):
            return -1
        dic={}   
        mxm = 1000000
        for i in range (len(cards)):
            if cards[i] not in dic:
                dic[cards[i]]=i
            else:
                if mxm > (i-(dic[cards[i]])):
                    mxm = (i-dic[cards[i]])
                dic[cards[i]]=i
        return mxm + 1
