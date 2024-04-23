# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)

        for u,v in richer:
            graph[u].append(v)

        ancestor = [[] for _ in range(len(quiet))]
       
        for node in range(len(quiet)):
            queue = deque([node])
            visited = {node}
            while queue:
                now = queue.popleft()
                for nb in  graph[now]:
                    if nb not in visited:
                        visited.add(nb)
                        heappush(ancestor[nb],(quiet[node],node))
                        queue.append(nb)
                
        answer = [0 for i in range(len(quiet))]

        for i in range(len(ancestor)):
            if ancestor[i] and ancestor[i][0][0] < quiet[i]:
                val,node = ancestor[i][0]

                answer[i] = node
            else:
                answer[i] = i
        return answer           



        