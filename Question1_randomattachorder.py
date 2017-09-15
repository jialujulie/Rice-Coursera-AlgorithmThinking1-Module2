"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import time
import math
import Project2_BFS
import matplotlib.pyplot as plt



# CodeSkulptor import
# import simpleplot
# import codeskulptor
# codeskulptor.set_timeout(60)

# Desktop imports
import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)


def targeted_order(ugraph):
    # type: (object) -> object
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:               # from n, n-1,n-2,  O(n^2)
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def fast_targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    degreesets = []
    for k in range(len(new_graph)):   # initialize degreesets
        degreesets.append(set())

    for node_i in range(len(new_graph)): # fill up degreesets
        degree_i = len(new_graph[node_i])
        degreesets[degree_i].add(node_i)

    order_list = []

    for k in range(len(ugraph)-1,-1,-1):  #

        while degreesets[k]:
            node_u = random.choice(list(degreesets[k]))
            degreesets[k].remove(node_u)
            neighbors = new_graph[node_u]
            for neighbor_v in neighbors:
                degree_v = len(new_graph[neighbor_v])
                degreesets[degree_v].remove(neighbor_v)
                degreesets[degree_v-1].add(neighbor_v)

            order_list.append(node_u)

            new_graph.pop(node_u)

            for neighbor in neighbors:
                 new_graph[neighbor].remove(node_u)

    return order_list


# fast_targeted order for normal network instead of graphs created with sequential nodes
def fast_targeted_order_network(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    degreesets = []
    for k in range(len(ugraph)):   # initialize degreesets
        degreesets.append(set())

    for node_i in ugraph.keys(): # fill up degreesets
        degree_i = len(ugraph[node_i])
        degreesets[degree_i].add(node_i)

    order_list = []

    for k in range(len(ugraph)-1,-1,-1):  #

        while degreesets[k]:
            node_u = random.choice(list(degreesets[k]))
            degreesets[k].remove(node_u)
            neighbors = new_graph[node_u]
            for neighbor_v in neighbors:
                degree_v = len(new_graph[neighbor_v])
                degreesets[degree_v].remove(neighbor_v)
                degreesets[degree_v-1].add(neighbor_v)

            order_list.append(node_u)

            new_graph.pop(node_u)

            for neighbor in neighbors:
                 new_graph[neighbor].remove(node_u)

    return order_list
##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def make_graph_udER(num_nodes,p):
    """docstring"""
    dictionary = dict()
    if num_nodes <= 0:
        return dictionary
    else:
        for node in range(num_nodes):
            dictionary[node]= set([])
        for node_i in range(num_nodes-1):
            for node_j in range(node_i+1,num_nodes):
                randomnum = random.random()
                #print randomnum
                if randomnum < p:
                    dictionary[node_i].add(node_j)
                    dictionary[node_j].add(node_i)

    return dictionary

# codes for complete graph for creating UPA graph
def make_complete_graph_ud(num_nodes):
    """docstring"""
    dictionary = dict()
    if num_nodes <= 0:
        return dictionary
    else:
        for node in range(num_nodes):
            dictionary[node] = set([])
        for node_i in range(num_nodes - 1):
            for node_j in range(node_i + 1, num_nodes):
                dictionary[node_i].add(node_j)
                dictionary[node_j].add(node_i)

    return dictionary


"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""


class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm

    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that each node number
        appears in correct ratio

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        # update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


# create UPA
def UPA(n,m):
    graph = make_complete_graph_ud(m)

    i = m
    UPATrial1 = UPATrial(m)
    while i < n:
        graph[i] = UPATrial1.run_trial(m)
        for node_j in graph[i]:
            graph[node_j].add(i)

        i += 1

    return graph


# p is determined to be 0.004, m is determined to be 3
def random_order(ugraph):
    node_list = ugraph.keys()
    #print node_list
    random.shuffle(node_list)
    return node_list



# create data points for network
network = load_graph(NETWORK_URL)
num_nodes = len(network)
x_axis = list(range(num_nodes+1))
#attackorder = random_order(network) #question1
attackorder = fast_targeted_order_network(network)  #question 4
print attackorder[:10]
y_network = Project2_BFS.compute_resilience(network,attackorder)

# create data points for ER
graph_ER = make_graph_udER(num_nodes,0.004)
print graph_ER
#attackorder_ER = random_order(graph_ER) #Question 1
#attackorder_ER = targeted_order(graph_ER) #Q4
fast_attackorder_ER = fast_targeted_order(graph_ER) #Q4

#print attackorder_ER[:10], fast_attackorder_ER[:10]
print graph_ER.has_key(0)
y_ER = Project2_BFS.compute_resilience(graph_ER,fast_attackorder_ER)

# create data points for UPA
graph_UPA = UPA(num_nodes,3)
#attackorder_UPA = random_order(graph_UPA)  # Q1
attackorder_UPA = fast_targeted_order(graph_UPA) # Q4

y_UPA = Project2_BFS.compute_resilience(graph_UPA,attackorder_UPA)

# Plotting
plt.plot(x_axis,y_network,'-r',label = 'Network')
plt.plot(x_axis,y_ER,'-b', label = 'ER, p = 0.004')
plt.plot(x_axis,y_UPA,'-g', label = 'UPA, m = 3')
plt.legend(loc = 'upper right')

plt.title('Comparision of graph resilience for targeted attack - three graphs')
plt.xlabel('Number of Nodes attacked')
plt.ylabel('Size of largest connect component')
#plt.scatter(indegree_distribution.keys(),normalize_dist)

plt.show()
# test codes:

#print make_complete_graph_udER(4,0.5)
#print make_complete_graph_ud(4)
#print UPA(3,2)

#print random_order(Project2_BFS.EX_GRAPH00)
