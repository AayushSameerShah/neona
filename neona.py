import matplotlib.pyplot as plt
import importlib
import plot_internals
importlib.reload(plot_internals)
from plot_internals import *

def barplot(x, y, spines= True, figsize= None, point_size= 2, color= "#59ffc5", point_marker= 'o', font_dict= dict(), font_offset_xy= (0, 0), show_values= True):
    fig, ax = plot_configure(spines_yn= spines, figsize= figsize)
    sizes, alphas, point = get_point(fig, point_size)
    a, b = get_lw()
    
    for xi, yi in zip(x, y):
        for width, alpha in zip(a, b):
            ax.plot([xi, xi], [0, yi], lw= width, alpha= alpha, color= color)
        ax.plot([xi, xi], [0, yi], lw= 1, alpha= 1, color= color)
        
        for size, alpha in zip(sizes, alphas):
            ax.scatter(xi, yi, s= size, alpha= alpha, color= color, marker= point_marker)
        ax.scatter(xi, yi, s= point, alpha= 1, color= color, marker= point_marker)
        
    if show_values:
        x = plt.xticks()[0]
        for xi, yi in zip(x, y):
            ox, oy = font_offset_xy
            ax.text(xi + ox, yi + oy, str(yi), **font_dict)
            
    return ax