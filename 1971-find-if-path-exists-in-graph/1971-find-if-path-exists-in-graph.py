class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = {}
        visited=set()

        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if node==destination:
                return True
            for i in graph[node]:
                if dfs(i):
                    return True
            return False
        return dfs(source)
            
                