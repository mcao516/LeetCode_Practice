from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1
             
        queue, order = [], []
        
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)
                
        while len(queue) > 0:
            node = queue.pop(0)
            order.append(node)
            
            for n in graph[node]:
                in_degree[n] -= 1
                
                if in_degree[n] == 0:
                    queue.append(n)
                    
        return len(order) == numCourses