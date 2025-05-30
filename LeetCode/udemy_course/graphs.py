from collections import deque

class Solution:
    def traversal_bfs(self, graph):
        if not graph:
            return []
        
        result = []
        queue = deque([0])
        seen = set([0])

        while queue:
            node = queue.popleft()
            result.append(node)
            
            for edge in graph[node]:
                if edge not in seen:
                    queue.append(edge)
                    seen.add(edge)
        
        return result
    
    def traversal_dfs(self, graph):
        if not graph:
            return []
        
        def dfs(node, seen, result):
            if node in seen:
                return
            
            result.append(node)
            seen.add(node)

            for edge in graph[node]:
                dfs(edge, seen, result)

        result = []
        seen = set()
        dfs(0, seen, result)
        return result
    
    def num_of_minutes(self, n, headID, manager, informTime):
        if n == 1:
            return 0
        
        graph = {id:[] for id in range(n)}
        for employee_id in range(len(manager)):
            manager_id = manager[employee_id] #2

            if manager_id != -1:
                graph[manager_id].append(employee_id)

        def dfs(node):
            if not graph[node]:
                return 0

            max_minutes = 0
            for edge in graph[node]:
                max_minutes = max(max_minutes, dfs(edge))
            
            return max_minutes + informTime[node]
        
        return dfs(headID)   

solution = Solution()
graph_1 = {
    0: [1, 3],
    1: [0],
    2: [3, 8],
    3: [0, 4, 5, 2],
    4: [3, 6],
    5: [3],
    6: [4, 7],
    7: [6],
    8: [2]
}
print(solution.traversal_bfs(graph_1))
print(solution.traversal_dfs(graph_1))

print(solution.num_of_minutes(8, 4, [2,2,4,6,-1,4,4,5], [0,0,4,0,7,3,6,0]))
print(solution.num_of_minutes(11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]))