import matplotlib.pyplot as plt
import seaborn as sns

def plot_timeseries(y, t):
    '''
    Plot all the time series in the columns of the numpy array y against t (in the x axis).
    y label is 'Time series  (arbitrary units)'.
    x label is 'Time (arbitrary units)'.
    Legends should be Node 1, Node 2, and so on.python
    '''
    num_nodes = y.shape[1]
    for i in range(num_nodes):
        plt.plot(t, y[:, i], label=f'Node {i+1}')
    plt.xlabel('Time (arbitrary units)')
    plt.ylabel('Time series (arbitrary units)')
    plt.legend()
    plt.show()

def plot_boolean_graph(A):
    '''
    Plot for input adjacency matrix A (2d numpy array).
    Outputs a figure with plot of the boolean matrix A,
    white for 0 and black for 1.
    Include a caption on what is white and what is black.
    '''
    cmap = sns.color_palette("binary", as_cmap=True)
    plt.imshow(A, cmap=cmap)
    plt.colorbar()
    plt.text(-1, -1, '0: White (False)\n1: Black (True)', fontsize=10)
    plt.show()

def plot_trilean_graph(A):
    '''
    Plot for input adjacency matrix A (2d numpy array).
    Outputs a figure with plot of the boolean matrix A,
    white for 0, blue for 1, and red for -1.
    '''
    cmap = sns.color_palette(["#FF5733", "white", "#334FFF"], as_cmap=True)
    plt.imshow(A, cmap=cmap)
    plt.colorbar()
    plt.text(-1, -1, '-1: Red\n0: White\n1: Blue', fontsize=10)
    plt.show()
