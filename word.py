class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) 
        n = len(board[0])
        def dfs(node,visited,i,ans="") :
            visited[node[0]][node[1]] = 1
            row = node[0] 
            col = node[1] 
            ans += board[row][col] 
            print(ans )
            if(ans == word) :
                return True 
            right,left,up,down = False,False,False,False
            if(col + 1 < n) :
                if(i+1 <= len(word)) :
                    if(board[row][col+1] == word[i] and visited[row][col+1]== 0) :
                        right = dfs((row,col+1),visited,i+1,ans)

            if(col - 1 >= 0) :
                if(i+1 <= len(word)) :
                    if(board[row][col-1] == word[i] and visited[row][col-1]== 0) :
                        left = dfs((row,col-1),visited,i+1,ans)


            if(row + 1 < m) :
                if(i+1 <= len(word)) :
                    if(board[row+1][col] == word[i] and visited[row+1][col]== 0) :
                        down = dfs((row+1,col),visited,i+1,ans)


            if(row -1 >= 0) :
                if(i+1 <= len(word)) :
                    if(board[row-1][col] == word[i] and visited[row-1][col]== 0) :
                        up = dfs((row-1,col),visited,i+1,ans)

            return left or right or up or  down 
        if(len(word) == 0) :
            return True 
        
        for i in range(m) :
            for j in range(n) :
                if(board[i][j] == word[0]) :
                    visited = [[0]*n for i in range(m)] 
                    ans = dfs((i,j),visited,1)
                    if(ans == True  ) :
                        return True 

        return False 

