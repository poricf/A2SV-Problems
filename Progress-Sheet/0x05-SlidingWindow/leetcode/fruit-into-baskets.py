class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        left,right = 0,0
        max_size = 0
        while(right < len(fruits)):
            window[fruits[right]] += 1

            while len(window) > 2:
                window[fruits[left]] -= 1
                
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left+=1
            
            max_size = max(right - left + 1, max_size)
            right+=1
        return (max_size)

