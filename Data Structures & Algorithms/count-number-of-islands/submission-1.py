class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def checkneighbors(curr, curc):
            r=[1, 0, 0 , -1]
            c=[0, 1 ,-1, 0]
            res=[]
            for i in range(len(r)):
                row=curr+r[i]
                col=curc+c[i]
                if 0<=row<rows and 0<=col<cols:
                    res.append([row,col])
            return res

        def dfs(curr, curc):
            if grid[curr][curc]=="0" or visited[curr][curc] == 1:
                return
            visited[curr][curc] = 1
            neighbors=checkneighbors(curr, curc)

            for neighbor in neighbors:
                dfs(neighbor[0], neighbor[1])
        
        visited=[]
        for i in range(rows):
            temp=[]
            for _ in range(cols):
                temp.append(0)
            visited.append(temp)
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and visited[i][j] ==0:
                    dfs(i,j)
                    count+=1

        return count