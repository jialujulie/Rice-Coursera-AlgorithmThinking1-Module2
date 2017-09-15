"""Algorithm thinking Module 2 - project 2"""
from collections import deque
import random


EX_GRAPH0 = {0:set([1,2]),1:set([0]), 2:set([0])}
EX_GRAPH00 = {0:set([1,4,5]), 1:set([0, 2, 4]), 2:set([1,3,5]), 3:set([2]), 4:set([0,1]), 5:set([0,2])}

EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), \
             8:set([1,2]), 9:set([0,4,5,6,7,3])}
# function to return connected components for a specific node
def bfs_visited(ugraph, start_node):
    """bfs_visited"""
    new_que = deque()
    visited = set([start_node])
    new_que.append(start_node)

    while new_que:
        j_node = new_que.popleft()
        for neighbor_h in ugraph[j_node]:
            if neighbor_h not in visited:
                visited.add(neighbor_h)
                new_que.append(neighbor_h)

    return visited
# function to return a set of connected components

def cc_visited(ugraph):
    """return a list of sets of cc"""
    remain_nodes = ugraph.keys()
    cc_list= []

    while remain_nodes:
        i_node = random.choice(remain_nodes)
        #print i_node
        w_vistednodes = bfs_visited(ugraph,i_node)
        #print w_vistednodes
        cc_list.append(w_vistednodes)

        for element in w_vistednodes:
            remain_nodes.remove(element)

    return cc_list

def largest_cc_size(ugraph):
    """return largest size among all connected components"""
    ccsets = cc_visited(ugraph)
    if ccsets:
        return max(len(eachset) for eachset in ccsets)
    else:
        return 0

def compute_resilience(ugraph,attack_order):
    """return list of sizes of each graph after deleting nodes one by one"""
    size_list = [largest_cc_size(ugraph)]
    for node in attack_order:
        for connected_node in ugraph[node]:
            ugraph[connected_node].remove(node)
        ugraph.pop(node)
        size_list.append(largest_cc_size(ugraph))

    #print ugraph
    return size_list



print bfs_visited(EX_GRAPH0,2)
print cc_visited(EX_GRAPH0)
print largest_cc_size(EX_GRAPH00)
print compute_resilience(EX_GRAPH00,[0])