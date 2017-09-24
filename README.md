# Rice-Coursera-AlgorithmThinking1-Module2

1. Project2_BFS.py includes the following functions:
 * bfs_visited(ugraph, start_node) 
    - Takes the undirected graph ugraph and the node start_node and returns the set consisting of all nodes that are visited by a breadth-first search that starts at start_node.
 * cc_visited(ugraph) 
    - Takes the undirected graph ugraph and returns a list of sets, where each set consists of all the nodes (and nothing else) in a connected component, and there is exactly one set in the list for each connected component in ugraph and nothing else.
 * largest_cc_size(ugraph) 
    - Takes the undirected graph ugraph and returns the size (an integer) of the largest connected component in ugraph.
 * compute_resilience(ugraph, attack_order) 
    - Takes the undirected graph ugraph, a list of nodes attack_order and iterates through the nodes in attack_order. 
