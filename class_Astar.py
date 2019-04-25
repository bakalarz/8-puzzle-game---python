from queue import PriorityQueue as pq
from copy import deepcopy

"""Creates a class called Node"""
class Node(object):
    """Constractor of the class."""
    def __init__(self, board, move,parent=None):
        self.board = board
        self.move = move
        self.parent = parent
    """Special method,which makes it possible for the classes to be compared. Used for PQueue."""
    def __lt__(self,other): 
        return 0
    """Returns the position of the empty block. """
    def zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i,j
    """Returns the manhattan distance."""
    def manhattan_distance(self):
        total = 0
        for i in range(3):
            for j in range(3):
                row = int(self.board[i][j]/3)
                column = int(self.board[i][j]%3)
                total += abs(i-row)+abs(j-column)
        return total
    """The function generates and returns nodes."""
    def generate_nodes(self):
        zero_position = self.zero_position() #assigns the position of the empty block to the variable zero_position.
        board = self.board #assigns the board that has been passed as an attribute of the class Node to the variable board.
        allnodes = [] #creates an array that will store nodes.
        if not zero_position[0]-1<0: #checks if the node can be moved upwards.
            board_up = deepcopy(board) #creates a copy of the board and assigns it to the variable board_up.
            board_up[zero_position[0]][zero_position[1]] = board_up[zero_position[0]-1][zero_position[1]] #puts a value of the node above to the place, where zero was.
            board_up[zero_position[0]-1][zero_position[1]] = 0 #puts zero one node above.
            board_up_node = Node(board_up,'down',self) #creates an object of a class Node, passing two arguments and an object containing information from the parent node.
            allnodes.append(board_up_node) #the node is appended to "allnodes" array.
        if zero_position[0]+1<3:  #checks if the node can be moved downwards
            board_down = deepcopy(board)
            board_down[zero_position[0]][zero_position[1]] = board_down[zero_position[0]+1][zero_position[1]] #puts a value of the node above to the place, where zero was.
            board_down[zero_position[0]+1][zero_position[1]] = 0 #puts zero one node above
            board_down_node = Node(board_down, 'up',self)
            allnodes.append(board_down_node)
        if not zero_position[1]-1<0: #checks if the node can be moved to the right
            board_left = deepcopy(board)
            board_left[zero_position[0]][zero_position[1]] = board_left[zero_position[0]][zero_position[1]-1] #puts a value of the node above to the place, where zero was.
            board_left[zero_position[0]][zero_position[1]-1] = 0 #puts zero one node above
            board_left_node = Node(board_left,'right',self)
            allnodes.append(board_left_node)
        if zero_position[1]+1<3: #checks if the node can be moved to the left
            board_right = deepcopy(board)
            board_right[zero_position[0]][zero_position[1]] = board_right[zero_position[0]][zero_position[1]+1] #puts a value of the node above to the place, where zero was.
            board_right[zero_position[0]][zero_position[1]+1] = 0 #puts zero one node above
            board_right_node = Node(board_right,'left',self)
            allnodes.append(board_right_node)
        
        return allnodes
    """Stores all the parents "traceback" of a node. """
    def traceback(self):# returns a list of objects.
        path = []
        path.append((self.move,self.board))
        n = self.parent
        while n.parent is not None:
            path.append((n.move,n.board))
            n = n.parent
        path.append((n.move,n.board))
        path.reverse()
        return path

"""Actual A star fucntion."""      
initial_node = Node([[5,7,8],[2,3,1],[4,0,6]],'start')
def Astar(initial_node):
    PQueue = pq() #priority queue, compares and sorts.
    visited = []
    explored = 0
    PQueue.put((initial_node.manhattan_distance(),initial_node)) #inserts a tuple with heuristic and node.
    while not PQueue.empty():  
       h, n = PQueue.get() #PQueue returns a tuple, heuristic and node.
       if n.board in visited:   #this prevents repetition of the nodes.
           continue
       if h==0: #this is a condition for winning.
           print('Congratulations!')
           print('The numbered of explored nodes:%d'%explored)
           draw_path(n.traceback())
           return
       
       visited.append(n.board)
       
       explored+=1
       
       for nnode in n.generate_nodes(): 
           PQueue.put((nnode.manhattan_distance(),nnode))
"""Prints the board."""         
def draw_board(board):
    print('___________')
    for i in board:
        print('|%d|%d|%d|'%(i[0],i[1],i[2]))
        print('___________') 
"""Draws the path."""   
def draw_path(path):
    for b in path:
        print(b[0])
        draw_board(b[1])
    print('END') 


Astar(initial_node)