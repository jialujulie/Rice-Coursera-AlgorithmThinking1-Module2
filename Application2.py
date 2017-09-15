def make_complete_graph(num_nodes):
    """docstring"""
    dictionary = dict()
    if num_nodes <= 0:
        return dictionary
    else:
        for node in range(num_nodes):
            dictionary[node] = set(other_node for other_node in range(num_nodes))
            dictionary[node].remove(node)

    return dictionary