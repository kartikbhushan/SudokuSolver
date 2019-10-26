#welcome to the sudoku solver using backtracking
#this is the board layout of the sudoku puzzle we will be using 
#zeros represent empty spaces
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#solves for the value using valid function and backtracking
def solve(bo):
    find =find_empty(bo)
    if not find:
        return True
    else:
        row,col = find
    
    for i in range (1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i
            #recurssive solving 
            if solve(bo):
                return True
            
            bo[row][col]=0
    
    return False


#checks if the number is valid for the block 
def valid(bo,num,pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i]== num and pos[1] !=i:
            return False
    #check columns
    for i in range(len(bo)):
        if bo[i][pos[1]]== num and pos[0] !=i:
            return False
    #check Box
    box_x=pos[1] // 3
    box_y=pos[0] // 3 

    for i in range(box_y * 3 ,box_y * 3 + 3 ):
        for j in range(box_x * 3 ,box_x * 3 + 3 ):
            if bo[i][j] == num and (i,j) !=pos:
                return False
    
    return True 

#just prints the board in a good layout(OCD)
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
            #prints this line after every three rows 
        for j in range (len(bo[0])):
            if j % 3 == 0 and j !=0:
                print(" | ",end="")
                #doesnt go to the next line 

            if j == 8:
                print(bo[i][j])
            else :
                print(str(bo[i][j]) + " ",end="")

#find the empty spaces on the board ready to be filled 
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)  #return row , column

    return None


print_board(board)
solve(board)
print("_____________________________")
print_board(board)

#there you have it a sudoku solver using backtracking algo 
#have a good day 