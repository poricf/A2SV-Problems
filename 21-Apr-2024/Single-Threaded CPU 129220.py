# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        all_val = []
        for ind, task in enumerate(tasks):
            all_val.append([task[0],task[1], ind])
        all_val.sort()
        
        current_time ,answer,heap = 0, [] , []
        indSet = set()
        et,pt,ind = all_val[0]
        heappush(heap,[pt,ind,et])
        current_time = et
        
        i = 1
        while i < len(all_val):
            if heap: pt , ind , et = heappop(heap)
            
            if ind not in indSet:
                answer.append(ind)
                current_time += pt
                indSet.add(ind)
            else:
                current_time = all_val[i][0]
                
                
                

            # print(current_time)
            while i < len(all_val) and all_val[i][0] <= current_time:
                # print(all_val[i][0],current_time)
                et,pt,ind = all_val[i]
                
                heappush(heap,[pt,ind,et])
                # print("ind",ind ,"Pushed")
                # print("i = ", i)
                i += 1
        
        while heap:
            if heap: pt , ind , et = heappop(heap)
            if ind not in indSet:
                answer.append(ind)
                indSet.add(ind)
        return answer