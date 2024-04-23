# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(ingredients)):
            indegree[recipes[i]] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])

        for node in supplies:
            queue = deque([node])
            while queue:
                node = queue.popleft() 
                for neg in graph[node]:
                    indegree[neg] -= 1
                    if neg in graph and indegree[neg] == 0:
                        queue.append(neg)  
        
            
        answer = []
        for food,req in indegree.items():
            if req < 1:
                answer.append(food) 
        return answer


