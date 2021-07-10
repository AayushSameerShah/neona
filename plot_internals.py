import matplotlib.pyplot as plt
import numpy as np

def get_lw(lw=15):
    a = np.arange(lw, 0, -4); gap = len(a)
    b = np.linspace(0, .3, gap)
    return a, b

def plot_configure(ax, spines_yn= True):
    for spine in ['left', 'right', 'top', 'bottom']:
        ax.spines[spine].set_visible(spines_yn)

def get_point(fig, point_size):
    fig_width_x_height = fig.get_figwidth() * fig.get_figheight()
    
    point_size *= 1_000
    patch_size = (point_size * fig_width_x_height) // 150
    decrease = (500 * patch_size) // 10_000
    point = (50 * patch_size) // 10_000

    size = np.arange(patch_size, 0, -decrease); gap = len(size)
    alpha = np.linspace(.05, .5, gap) ** 3
    return size, alpha, point

def cycle_colors(color):
    return cycle([color]) if isinstance(color, str) else cycle(color)