import numpy as np

def generate_unipartite_graph(sparsity=0.1, type='fully_connected', num_nodes=5):
    '''
    Output should be a 2d numpy array of shape (num_nodes,num_nodes), default values are set
    Fully -- connected is all ones
    full_rank -- random booleans 0s and 1s -- such that (total number of 1)/num_nodes is approximately equal to 1-sparsity
    and the square matrix is full rank
    fully nested -- upper-traingular matrix
    '''
    if type == "fully_connected":
        return np.ones((num_nodes, num_nodes))
    elif type == "full_rank":
        num_ones = int((1 - sparsity) * num_nodes ** 2)
        matrix = np.zeros((num_nodes, num_nodes))
        indices = np.random.choice(num_nodes ** 2, num_ones, replace=False)
        matrix.flat[indices] = 1
        return matrix
    elif type == "fully_nested":
        matrix = np.triu(np.ones((num_nodes, num_nodes)), k=1)
        return matrix
    else:
        raise NotImplementedError("Graph type not implemented for"+type)

def generate_bipartite_graph():
    raise NotImplementedError
