class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        visited=set()
        def dfs(r,c):
            if r>len(board)-1 or c>len(board[0])-1 or r<0 or c<0:
                return
            if board[r][c]!="O" or (r,c) in visited:
                return

         
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    if r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1:
                        dfs(r, c)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
        
        return board
        