# Libs
import importlib
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
# Plot-Mods
import plot_internals
from plot_internals import *

importlib.reload(plot_internals)
colors = ["#59ffc5", "#ffed4f", "#19ffaf", "#00eaff", "#ffed4f", "#f67dff", "#ff59db", "#ff59db", "#fffba6", "cyan"]

def barplot(x, y, spines= True, figsize= None, point_size= 2, color= "#59ffc5",
            point_marker= 'o', font_dict= dict(), font_offset_xy= (0, 0),
            show_values= True):
    
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

# ----------------------------------------------- ANOTHER ------------------------------------------------------

def lineplot(x, y= None, spines= True, figsize= None, point_size= 2,
             color= "#59ffc5", point_marker= 'o', font_dict= dict(),
             font_offset_xy= (0, 0), show_values= True, show_marks= True):
    
    fig, ax = plot_configure(spines_yn= spines, figsize= figsize)
    sizes, alphas, point = get_point(fig, point_size= point_size)
    font_dict['color'] = color
    a, b = get_lw()
    
            
    # WHOLE DF / Series
    if not isinstance(y, (pd.Series, pd.DataFrame)) and y == None:
        
        # DF given
        if isinstance(x, pd.DataFrame):
            columns = [*x.columns]
            for colorId, col in enumerate(columns):
                font_dict['color'] = colors[colorId]
                
                for width, alpha in zip(a, b):
                    plt.plot(x[col], lw= width, alpha= alpha, color= colors[colorId])
                plt.plot(x[col], lw= 1, alpha= 1, color= colors[colorId])
                
                if show_values: 
                    for ind, val in zip(x[col].index, x[col].values):
                        plt.text(ind, val, str(val), **font_dict)    
                        
                if show_marks:
                    for ind, val in zip(x[col].index, x[col].values):
                        for size, alpha in zip(sizes, alphas):
                            plt.scatter(ind, val, s= size, alpha= alpha, color= colors[colorId], marker= point_marker)
                        plt.scatter(ind, val, s= 10, alpha= 1, color= colors[colorId], marker= point_marker)
                    
        # SERIES given / List
        else:
            for width, alpha in zip(a, b):
                plt.plot(x, lw= width, alpha= alpha, color= color)
            plt.plot(x, lw= 1, alpha= 1, color= color)
            
            if show_values:
                if isinstance(x, pd.Series): inds = x.index
                else: inds = list(range(len(x)))
                for ind, val in zip(inds, x):
                        plt.text(ind, val, str(val), **font_dict)    
            
            if show_marks:
                if isinstance(x, pd.Series): inds = x.index
                else: inds = list(range(len(x)))
                for ind, val in zip(inds, x):
                        for size, alpha in zip(sizes, alphas):
                            plt.scatter(ind, val, s= size, alpha= alpha, color= color, marker= point_marker)
                        plt.scatter(ind, val, s= 10, alpha= 1, color= color, marker= point_marker)
    
    # Both X and Y given              
    else:
        for width, alpha in zip(a, b):
            plt.plot(x, y, lw= width, alpha= alpha, color= color)
        plt.plot(x, y, lw= 1, alpha= 1, color= color)
        
        if show_values:
            for valx, valy in zip(x, y):
                plt.text(valx, valy, str(valy), **font_dict)   
            
        if show_marks:
            for ind, val in zip(x, y):
                for size, alpha in zip(sizes, alphas):
                    plt.scatter(ind, val, s= size, alpha= alpha, color= color, marker= point_marker)
                plt.scatter(ind, val, s= 10, alpha= 1, color= color, marker= point_marker)
    
    return ax

# ------------------------------------- ANOTHER ----------------------------------------------------------------

def kdeplot(x, covariance_factor=.5, fill_alpha=.15, fill=True, spines=True,
             color="#59ffc5", lw=15, ax=None):
    
    ax = ax or plt.gca()
    plot_configure(ax, spines_yn=spines)
    a, b = get_lw(lw=lw)
    
    def plot_it(x, color=color):
        density = gaussian_kde(x)
        x_min = min(x)
        x_max = max(x)
        xs = np.linspace(x_min - int(x_max * .5), x_max + int(x_max * .5), 2000)
        density.covariance_factor = lambda : covariance_factor
        density._compute_covariance()
        
        for width, alpha in zip(a, b):
            plt.plot(xs, density(xs), color=color, alpha= alpha, lw= width)
        plt.plot(xs, density(xs), color=color)
        
        if fill:
            ylim = plt.ylim()
            plt.fill_between(xs, density(xs), color=color, alpha=fill_alpha)
            plt.ylim(ylim)
    
    
    # Checking if X is from list, array, series or tuple (in short not df)
    if not isinstance(x, (pd.DataFrame)):
        plot_it(x)
        
    # Means DF is passed
    else:
        columns = [*x.columns]
        for colorId, col in enumerate(columns):
            plot_it(x[col], colors[colorId])
    
    return ax

# ------------------------------------ ANOTHER ------------------------------------------

def scatterplot(x, y, spines=True, point_size=2,
                 color="#59ffc5", point_marker='o', font_dict=dict(),
                 font_offset_xy=(0, 0), show_values=None, ax=None):
    
    fig = plt.gcf()
    ax = ax or plt.gca()
    font_dict['color'] = color
    plot_configure(ax, spines_yn=spines)
    size, alpha, point = get_point(fig, point_size=point_size)
    
    for size, alpha in zip(size, alpha):
        plt.scatter(x, y, s=size, alpha=alpha, color=color, marker=point_marker)
    plt.scatter(x, y, s=point, color=color, marker=point_marker)
    
    if show_values:
        if show_values == True:
            for x, y in zip(x, y):
                plt.text(x, y, str(y), **font_dict)
        else:
            values = list(iter(show_values))
            if len(values) == len(x):
                for x, y, value in zip(x, y, values):
                    plt.text(x, y, str(value), **font_dict)
            else: raise NotImplementedError("The length is not matching")
            
    return ax