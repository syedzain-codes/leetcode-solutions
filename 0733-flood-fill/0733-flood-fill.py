class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        visited=set()
        def dfs(r,c,x):
            if r<0 or c<0 or r>len(image)-1 or c>len(image[0])-1:
                return 0
            if image[r][c]!=x or (r,c) in visited:
                return 0
            visited.add((r,c))
            image[r][c]=color
            up=dfs(r-1,c,x)
            down=dfs(r+1,c,x)
            left=dfs(r,c-1,x)
            right=dfs(r,c+1,x)
        dfs(sr,sc,image[sr][sc])
        return image
         

            
        