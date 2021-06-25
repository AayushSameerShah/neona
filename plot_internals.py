import matplotlib.pyplot as plt
import numpy as np

def get_lw():
    a= np.arange(15, -1, -4); gap = len(a)
    b= np.arange(0, 1, (1/gap)-.1)
    return a, b

def plot_configure(spines_yn= True, figsize= None):
    fig, ax = plt.subplots(figsize= figsize)
    for spine in ['left', 'right', 'top', 'bottom']:
        ax.spines[spine].set_visible(spines_yn)
    return fig, ax

def get_point(fig, point_size):
    fig_width_x_height = fig.get_figwidth() * fig.get_figheight()
    
    point_size *= 1_000
    patch_size = (point_size * fig_width_x_height) // 150
    decrease = (500 * patch_size) // 10_000
    point = (50 * patch_size) // 10_000

    size = np.arange(patch_size, 0, -decrease); gap = len(size)
    alpha = np.linspace(.05, .5, gap) ** 3
    return size, alpha, point