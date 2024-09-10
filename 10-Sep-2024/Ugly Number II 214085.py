# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        chung = [2, 3, 5]
        st = set()
        for _ in range(n-1):
            now = heappop(heap)
            for prime in chung:
                x = now * prime
                if x not in st:
                    heappush(heap, x)
                    st.add(x)
        
        return heap[0]

