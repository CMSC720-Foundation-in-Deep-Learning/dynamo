
'''
Examples for Physics based dynamical systems 
Written by Raunak Dey
'''



import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from dataclasses import dataclass
import logging
import sys

sys.path.append('./../dynamo')

# sample/example.py

#from dynamo.model import PhysicsModel
#from dynamo.utils_plot import *

#from model import PhysicsModel
# I do not know why this is not working.

from ..dynamo.model import PhysicsModel



if __name__ == "__main__":
    init = 1. + np.random.uniform(0.,30.,size=(10,))
    tspan = np.arange(0,100,1)
    adjacency_matrix = np.random.randint(2, size=(10,10))
    physics_model = PhysicsModel(name='kuramoto2', time=tspan)  # Assigning tspan to time
    omega_value = 1 + 10 * np.random.rand(10,)  # np.random needs to be np.random.rand

    y = odeint(physics_model.dynamical_model, init, tspan, args=(physics_model.adjacency_matrix,omega_value))

    plt.plot(y)
    plt.show()

