__author__ = 'appell'

var = '''
 (Intermediate): Find the shortest path

Given an ASCII grid through standard console input, you must find the shortest path from the start to the exit (without walking through any walls). You may only move up, down, left, and right; never diagonally.

Author: liloboy
Formal Inputs & Outputs
Input Description

The first line of input is an integer, which specifies the size of the grid in both dimensions. For example, a 5 would indicate a 5 x 5 grid. The grid then follows on the next line. A grid is simply a series of ASCII characters, in the given size. You start at the 'S' character (for Start) and have to walk to the 'E' character (for Exit), without walking through any walls (indicated by the 'W' character). Dots / periods indicate open, walk-able space.
Output Description

The output should simply print "False" if the end could not possibly be reached or "True", followed by an integer. This integer indicates the shortest path to the exit.
Sample Inputs & Outputs
Sample Input

5
S....
WWWW.
.....
.WWWW
....E

Check out this link for many more examples! http://pastebin.com/QFmPzgaU
Sample Output

True, 16

Challenge Input

8
S...W...
.WW.W.W.
.W..W.W.
......W.
WWWWWWW.
E...W...
WW..WWW.
........

Challenge Input Solution

True, 29
Note

As a bonus, list all possible shortest paths, if there are multiple same-length paths.

'''

import heapq

maze_size = 8
total_squares = maze_size*maze_size
maze_layout = "S...W....WW.W.W..W..W.W.......W.WWWWWWW.E...W...WW..WWW........."

# Get start and end maze indexes
start = maze_layout.index("S")
end = maze_layout.index("E")

# List of visited nodes
visited = []
#Tuple of path cost and the path steps
paths = [(0, [start])]

# Set up starting path
current_path = paths[0]
# Set up first node
current_node = current_path[1][0]

# Loop through node options until we find the shortest path to end
while current_node != end:
    visited.append(current_node)
	# Get all adjacent nodes
    nsew = current_node - maze_size, current_node + maze_size, current_node + 1, current_node - 1
	# Filter the adjacent nodes based on the following:
    for valid_option in (option for option in nsew
		# option is within square bounds
        if option < total_squares \
		   # option is not a wall ('W')
           and maze_layout[option] != "W" \
		   # option is not negative i.e. outside the box
           and option > 0 \
		   # option has not already been visited
           and option not in visited \
		   # The following two conditions are required because I am treating a 1d array as a 2d datastructure
		   # If the current node is on the left edge of the maze and the option is on the right edge, filter it out
           and not((current_node % maze_size) == 0 and option == (current_node - 1)) \
		   # If the current node is on the right edge and the option is the left edge, filter it out
           and not((current_node + 1) % maze_size == 0 and option == (current_node + 1))):
		# push the new node option on to the end of the current path with a priority equal to (x2 - x1) + (y2 - y1)
        heapq.heappush(paths, (abs((valid_option % maze_size) - (end % maze_size)) + abs((valid_option / maze_size) - (end / maze_size)), current_path[1] + [valid_option]))

    current_path = heapq.heappop(paths)
    current_node = current_path[1][-1]

print ("Answer: ", current_path)

