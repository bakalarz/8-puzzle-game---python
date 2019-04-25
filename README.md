# Astar-python
The program simulates the 8 puzzle game (A* algorithm using heuristic)


The 8-puzzle game is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. The board
consists of 9 blocks with numbers from one to eight and one "free" space. That space is used to rearrange the
blocks, so they end up in order. The goal is to use the least possible amount of moves. The blocks can be moved
vertically or horizontally into the empty space.

Tools used:

A* uses heuristics to guide its search.
f(n) = g(n) + h(n)
g(n) = cost from the starting node to reach n.
h(n) = heuristic, estimate of the cost of the cheapest path from n to the goal node.
At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on
the cost of the path and an estimate of the cost required to extend the path all the way to the goal. A* algorithm
generates an optimal solution if h(n) is an admissible heuristic, what means that it never overestimates the cost
to reach the destination node, and the search space is a tree.

The Manhattan distance is a sum of the vertical and horizontal distance, while Euklidean distance is the shortest
in the plane.

In the program PQueue takes the heuristic and board, and returns the smallest heuristic and the board distance.
The result is stored in the array called "visited", which prevents it from being compared again.
