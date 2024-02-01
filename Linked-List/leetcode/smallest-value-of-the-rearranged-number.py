class Solution:
    def smallestNumber(self, num: int) -> int:
        a=[]
        if num==0:
            return 0
        if num<0:
            y=-1
            num=num*-1
        else:
            y=1
        
        while num!=0:
            a.append(num%10)
            num=num//10
        if y==1:
            a.sort()
            p=str()
            if 0 in a:
                q=a.count(0)
                for i in a:
                    if i!=0:
                        r=i
                        break
                p=p+str(r)
                for i in range(q):
                    p=p+(str(0))
                    a.remove(0)
                a.remove(r)
            a.sort()
            
            
            for i in a:
                p=p+str(i)
            return int(p)
        else:
            a.sort()
            a=a[::-1]
            p=str()
            for i in a:
                p=p+str(i)
            return -1*int(p)





        