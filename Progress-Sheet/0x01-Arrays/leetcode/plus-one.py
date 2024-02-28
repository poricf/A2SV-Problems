class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s =""
        for i in digits:
            s+=str(i)
        num = int(s)+1
        l = list(str(num))
        l2 =[]
        for i in l:
            l2.append(int(i))
        return (l2)