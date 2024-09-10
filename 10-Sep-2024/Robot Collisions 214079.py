# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        temp = []
        for i, j in enumerate(positions):
            temp.append((j, i))
        temp.sort()
        st = []
        for i in temp:
            if not st:
                st.append(i)
                continue
            if directions[i[1]] == 'R':
                st.append(i)
            else:
                hold = i
                while hold and st and directions[hold[1]] == 'L' and directions[st[-1][1]] == 'R':
                    a, b = st[-1][1], hold[1]
                    if healths[a] > healths[b]:
                        healths[a] -= 1
                        hold = None
                    elif healths[a] < healths[b]:
                        st.pop()
                        healths[b] -= 1
                    else:
                        st.pop()
                        hold = None
                if hold:st.append(i)
        d = {}
        for i in st:
            d[i[0]] = i[1]
        ans = []
        for i in positions:
            if i in d:
                ans.append(healths[d[i]])
        return ans
                      
        