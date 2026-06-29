class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
    
            for j in rooms[node]:
                dfs(j)
        dfs(0)
        if len(visited)==len(rooms):
            return True
        else:
            return False


        