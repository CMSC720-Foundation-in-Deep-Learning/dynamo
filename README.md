# dynamo
Dyna-Mo is a "dynamical model" simulation framework to simualate Physics based time-series on Networks.
Given an input model, initial conditions and input graph, Dyna-mo simulates the trajectory of the dynamical system. We are also including two key statistical features.
* Understanding the statistics of the underlying graph.
* Simple statistics based forecasting (Physics-agnostic) 

### Advanced features (to be build)
* input model using symbolic math (will be built on sympy)
* Time-series analysis -- statistics (tbd)
* Advanced analysis -- Times Net/Prophet/TSlib etc

### Installation

To get started clone the dynamo repository. After two months this will be pushed to PyPi as a standalone package.

```
git clone git@github.com:CMSC720-Foundation-in-Deep-Learning/dynamo.git
```

### Minimal example

Simulating dynamical model for given input pamaters and model
```python
init = 1. + np.random.uniform(0.,30.,size=(10,))
tspan = np.arange(0,100,1)
adjacency_matrix = np.random.randint(2, size=(10,10))
physics_model = PhysicsModel(name='kuramoto2', time=tspan)  # Assigning tspan to time
omega_value = 1 + 10 * np.random.rand(10,)  # np.random needs to be np.random.rand
y = odeint(physics_model.dynamical_model, init, tspan, args=(physics_model.adjacency_matrix,omega_value))
```


Plotting the time series and the underlying network.
``` python
plot_timeseries(y, t)
plot_boolean_graph(A):

```
![kuramoto2](https://github.com/CMSC720-Foundation-in-Deep-Learning/dynamo/assets/39820997/daccf988-f108-4447-8684-c1053b42e9ee)
![demo_adjacency_matrix](https://github.com/CMSC720-Foundation-in-Deep-Learning/dynamo/assets/39820997/63c74988-230e-4c02-8488-898068b4cd45)

### Contributions
Started by Raunak Dey. Open to contribution from April'24 onwards.