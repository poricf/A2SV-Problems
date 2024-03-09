class Solution:
    def bestClosingTime(self, customers: str) -> int:

        d = {i : 1e9 for i in range(len(customers)+1)}
        yp = [0 for i in range(len(customers))]
        np = [0 for i in range(len(customers))]

        for i in range(len(customers)) :
            if customers[i] == "Y" :
                yp[i] += yp[i-1] + 1 
            else :
                yp[i] = yp[i-1]
            if customers[i] == "N" :
                np[i] += np[i-1] + 1 
            else:
                np[i] = np[i-1]
            
        yp = [0] + yp
        np = [0] + np

        d[yp[-1]] = 0

        for i in range(1,len(customers)+1) :
            val = yp[-1] - yp[i]
            val += np[i]

            d[val] = min(d[val] , i )

        dic = {}
        for k,v in d.items():
            if v !=1e9:
                dic[k] = v 

        dic = dict(sorted(dic.items() , key = lambda x : x[0]))

        for k,v in dic.items():
            return v