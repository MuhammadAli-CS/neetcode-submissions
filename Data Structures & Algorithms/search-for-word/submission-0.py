class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def dfs(i,j, word_i):
            if board[i][j]!=word[word_i]:
                return False
            if len(word)-1==word_i: return True
            char=board[i][j]
            board[i][j]="*"
            coors= [(i+1, j), (i-1, j), (i,j+1) , (i, j-1)]
            for r,c in coors:
                if 0<=r< row and 0<=c<col:
                    if dfs(r,c, word_i+1): return True
            board[i][j]=char
            return False





        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0): return True
        return False

