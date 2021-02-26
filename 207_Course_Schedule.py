from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            inDegree[pre[0]] += 1
            
        # enqueue all nodes with indegree equals zero
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        result = []
        while(len(queue) > 0):
            node = queue.pop(0)
            result.append(node)
            
            for n in graph[node]:
                inDegree[n] -= 1
                
                if inDegree[n] == 0:
                    queue.append(n)
            
        if len(result) != numCourses:
            return False
        else:
            return True
        