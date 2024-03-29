'''
Models for Physics based dynamical systems 
Written by Raunak Dey
'''


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from dataclasses import dataclass
import logging
import seaborn as sns

# Setting logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)


@dataclass
class PhysicsModel:
    name: str = None #name of model
    adjacency_matrix: 'np.ndarray' = None
    num_nodes: int = 10 #setting a default value to 5.
    initial_values: 'np.ndarray' = None
    noise_level: float = 0.0
    time : 'np.ndarray' = None

    #def __init__(self):
    #    pass  # You can initialize anything here if needed


    def __post_init__(self):
        if self.name not in ['kuramoto1', 'kuramoto2', 'michaelis_menten', 'roessler']:
            raise NameError("Invalid Input model. Sorry model not found. Please check spelling of input keywords.")
        if self.name is None:
            raise NameError("Need to specify the model ")
        if self.adjacency_matrix is None:
            self.adjacency_matrix = np.ones((self.num_nodes, self.num_nodes))
        if self.initial_values is None:
            self.initial_values = np.random.rand(self.num_nodes)
        if self.time is None:
            raise ValueError("Time of simulation is needed")
        if self.adjacency_matrix.shape[0] != self.adjacency_matrix.shape[1]:
            raise ValueError("Adjacency matrix should be a square matrix for an unipartite graph")
        if self.initial_values.shape[0] != self.adjacency_matrix.shape[0]:
            raise ValueError("Dimensions of number of nodes and adjacency matrix do not match.")

    
    # already taken care of the default values and not naming stuff in the post-init method
    # that is how I like to write 
    # if you don't like this, feel free to suggest soemthing else
    def dynamical_model(self, y, t, A, omega):
        dynamical_functions = {
            'kuramoto1': self.kuramoto1,
            'kuramoto2': self.kuramoto2,
            'michaelis_menten': self.michaelis_menten,
            'roessler': self.roessler
        }
        if self.name not in dynamical_functions:
            raise ValueError("Invalid model name")
        return dynamical_functions[self.name](y, t, A, omega)
    


    @staticmethod
    def kuramoto1(y,t,A,omega):
        dydt = np.zeros((y.shape[0],))
        k = omega.shape[0]
        for i in range(k):
            sum = 0.0
            for j in range(k):
                sum += A[i,j] * np.sin(y[j] - y[i])
            dydt[i] = omega[i] + sum
        return(dydt)
    
    @staticmethod
    def kuramoto2(y,t,A,omega):
        dydt = np.zeros((y.shape[0],))
        k = omega.shape[0]
        for i in range(k):
            sum = 0.0
            for j in range(k):
                sum += A[i,j] * (np.sin(y[j]-y[i]-1.05)) + 0.33*np.sin(2*(y[i]-y[j]))
            dydt[i] = omega[i] + sum
        return(dydt)

    @staticmethod
    def michaelis_menten(y,t,A):
        dydt = np.zeros((y.shape[0],))
        k = A.shape[0]
        for i in range(k):
            sum=0.0
            for j in range(k):
                sum += (A[i,j] * (y[j]/(1+y[j])))
            dydt[i] = -y[i] + sum
        return(dydt)

    @staticmethod   
    def roessler(y,t,A):
        dydt = np.zeros(y.shape[0])
        N = A.shape[0]
        for i in range(N):
            sum = 0.0
            for j in range(N):
                sum += A[i,j]*np.sin(y[(3*j)+0])
            dydt[(3*i)+0] = -y[(3*i)+1] - y[(3*i)+2] + sum
            dydt[(3*i)+1] = y[(3*i)+0] + 0.1*y[(3*i)+1]
            dydt[(3*i)+2] = 0.1 + (y[(3*i)+2]*(y[(3*i)+0]-18))

        return(dydt)



def read_data_file(file_path):
    # Assuming the data file contains numerical data separated by whitespace
    data_array = np.loadtxt(file_path)
    return data_array




if __name__ == "__main__":
    N = 25
    init = 1. + np.random.uniform(0.,30.,size=(N,))
    tspan = np.arange(0,100,1)
    #adjacency_matrix = np.random.randint(2, size=(N,N))
    physics_model = PhysicsModel(name='kuramoto2', time=tspan, num_nodes=N)  # Assigning tspan to time
    #omega_value = 1 + 10 * np.random.rand(N,)  # np.random needs to be np.random.rand

    # Example usage:
    omega_value = read_data_file('./../res/data/frequencies.dat')
    adjacency_matrix =  read_data_file('./../res/data/connection.dat')

    logging.debug('omega_value{}'.format(omega_value.shape))
    logging.debug('omega_value{}'.format(adjacency_matrix))

    y = odeint(physics_model.dynamical_model, init, tspan, args=(physics_model.adjacency_matrix,omega_value))

    ## plotting -- separate function exists
    num_nodes = y.shape[1]
    for i in range(num_nodes):
        plt.plot(tspan, y[:, i], label=f'Node {i+1}')
    plt.xlabel('Time (arbitrary units)')
    plt.ylabel('Time series (arbitrary units)')
    plt.legend()
    plt.show()

    #boolean matrix -- separate function exists 
    cmap = sns.color_palette("binary", as_cmap=True)
    plt.imshow(adjacency_matrix, cmap=cmap)
    plt.colorbar()
    plt.text(-1, -1, '0: White (False)\n1: Black (True)', fontsize=10)
    plt.show()