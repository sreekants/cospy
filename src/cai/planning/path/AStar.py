#!/usr/bin/env python
# Filename: AStar.py
# Description: Implementation of the A* Path Planning Algorithm

# TODO: Revise the implementation refering to https://www.redblobgames.com/pathfinding/a-star/introduction.html

import heapq, sys


# You should only need to use the following functions to implement A*:
# Graph(path_to_map) # path_to_map can, for instance, be 'maps/map1.png'
# graph.get_list_of_nodes()
# graph.get_neighbors(node)
# graph.get_start_node()
# graph.get_goal_node()

# For visualizing the algorithm use the following functions:
# graph.add_visited_node(node) # Use this when you are visiting a new node to update the visualization
# graph.add_shortest_path(path) # Use this to visualize the shortest path after you have found it.

def g(graph, start, end):
    """ #TODO: g
    Arguments
    	graph -- #TODO
    	start -- #TODO
    	end -- #TODO
    """
    return max( abs(start[0]-end[0]), abs(start[1]-end[1]) )

def h(graph, start, end):
    """ #TODO: h
    Arguments
    	graph -- #TODO
    	start -- #TODO
    	end -- #TODO
    """
    # Manhattan distance to the end goal.
    dest = tuple(graph.get_goal_node())
    return max( abs(dest[0]-end[0]), abs(dest[1]-end[1]) )

def f(graph, start, end):
    """ #TODO: f
    Arguments
    	graph -- #TODO
    	start -- #TODO
    	end -- #TODO
    """
    return g(graph, start,end)+h(graph, start,end)

def a_star(graph, heuristic_function=None):
    """ #TODO: a_star
    Arguments
    	graph -- #TODO
    	heuristic_function -- #TODO
    """
    # Here you need to implement A*. The implementation should return the path from start to goal, in the form of a
    # sequential list of nodes in the path.

    start = tuple(graph.get_start_node())
    dest = tuple(graph.get_goal_node())

    vertices = graph.get_list_of_nodes()

    # initialize distance maps
    dist = {v: (float('infinity'),None) for v in vertices}
    dist[start] = (0, None)

    # Track a priority queue to pick the shortest next step
    pq = [(0, start)]

    current = start
    graph.add_visited_node(start)

    while len(pq):
        currdist, current = heapq.heappop(pq)

        if currdist > dist[current][0]:
            continue

        for next in graph.get_neighbors(current):
            graph.add_visited_node(next)

            newdist = currdist + f(graph, current, next)
            if newdist < dist[next][0]:
                dist[next] = (newdist,current)
                if next == dest:
                    pq.clear()
                    break

                heapq.heappush( pq, (newdist, next) )


    # Build the path
    path = []
    current = dest
    while current != start:
        partdist, prev = dist[current]
        current = prev
        path.append(current)

    path.append(start)

    return path


if __name__ == "__main__":
    from cai.planning.utilities.ImageGridGraph import Graph
    graph = Graph(sys.argv[1])
    path = a_star(graph, heuristic_function=None)

    graph.add_shortest_path(path)

