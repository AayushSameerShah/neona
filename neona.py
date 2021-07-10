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
plt.style.use('dark_background')


def barplot(x, y, spines= True, point_size= 2, color= "#59ffc5",
            point_marker= 'o', font_dict= dict(),
            show_values= True, ax=None, lw=15):
    
    fig = plt.gcf()
    ax = ax or plt.gca()
    plot_configure(ax, spines_yn=spines)
    sizes, alphas, point = get_point(fig, point_size)
    a, b = get_lw(lw)
    
    colors = cycle_colors(color)
    for xi, yi in zip(x, y):
        colr = next(colors)
        for width, alpha in zip(a, b):
            ax.plot([xi, xi], [0, yi], lw= width, alpha= alpha, color= colr)
        ax.plot([xi, xi], [0, yi], lw= 1, alpha= 1, color= colr)
        
        for size, alpha in zip(sizes, alphas):
            ax.scatter(xi, yi, s= size, alpha= alpha, color= colr, marker= point_marker)
        ax.scatter(xi, yi, s= point, alpha= 1, color= colr, marker= point_marker)
        
    if show_values:
        colors = cycle_colors(color)
        for xi, yi in zip(x, y):
            colr = next(colors)
            font_dict['color'] = colr
            ax.text(xi, yi, str(yi), **font_dict)
            
    return ax

# ----------------------------------------------- ANOTHER ------------------------------------------------------

def lineplot(x, y= None, spines= True, figsize= None, point_size= 2,
             color= "#59ffc5", point_marker= 'o', font_dict= dict(),
             show_values= True, show_marks= True, ax=None, lw=15, legend=False, legend_label=None):
    
    fig = plt.gcf()
    ax = ax or plt.gca()
    plot_configure(ax, spines_yn=spines)
    sizes, alphas, point = get_point(fig, point_size= point_size)
    a, b = get_lw(lw)
    
    
    
    # WHOLE DF / Series
    if isinstance(x, (pd.Series, pd.DataFrame)) and y is None:
        
        # DF given
        if isinstance(x, pd.DataFrame):
            colors = cycle_colors(color)
            columns = [*x.columns]
            
            for col in columns:
                colr = next(colors)
                font_dict['color'] = colr
                
                for width, alpha in zip(a, b):
                    plt.plot(x[col], lw= width, alpha= alpha, color= colr)
                plt.plot(x[col], lw= 1, alpha= 1, color= colr, label=col)
                
                if show_values: 
                    for ind, val in zip(x[col].index, x[col].values):
                        plt.text(ind, val, str(val), **font_dict)    
                        
                if show_marks:
                    for ind, val in zip(x[col].index, x[col].values):
                        for size, alpha in zip(sizes, alphas):
                            plt.scatter(ind, val, s= size, alpha= alpha, color= colr, marker= point_marker)
                        plt.scatter(ind, val, s= 10, alpha= 1, color= colr, marker= point_marker)
                    
        # SERIES given / List
        else:
            colr = color if isinstance(color, str) else color[0]
            font_dict['color'] = colr
            for width, alpha in zip(a, b):
                plt.plot(x, lw= width, alpha= alpha, color= colr)
            plt.plot(x, lw= 1, alpha= 1, color= colr, label=legend_label)
            
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
                        plt.scatter(ind, val, s=size, alpha=alpha, color=colr, marker=point_marker)
                    plt.scatter(ind, val, s=10, alpha=1, color=colr, marker=point_marker)
    
    # Both X and Y given              
    else:
        colr = color if isinstance(color, str) else color[0]
        font_dict['color'] = colr
        
        for width, alpha in zip(a, b):
            plt.plot(x, y, lw= width, alpha= alpha, color= colr)
        plt.plot(x, y, lw= 1, alpha= 1, color= colr, label=legend_label)
        
        if show_values:
            for valx, valy in zip(x, y):
                plt.text(valx, valy, str(valy), **font_dict)   
            
        if show_marks:
            for ind, val in zip(x, y):
                for size, alpha in zip(sizes, alphas):
                    plt.scatter(ind, val, s= size, alpha= alpha, color= colr, marker= point_marker)
                plt.scatter(ind, val, s= 10, alpha= 1, color= colr, marker= point_marker)
    
    if legend: plt.legend()
    return ax

# ------------------------------------- ANOTHER ----------------------------------------------------------------

from scipy.stats import gaussian_kde

def kdeplot(x, covariance_factor=.5, fill_alpha=.15, fill=True, spines=True,
             color="#59ffc5", lw=15, ax=None, legend=False, legend_label=None):
    
    ax = ax or plt.gca()
    plot_configure(ax, spines_yn=spines)
    a, b = get_lw(lw=lw)
    
    def plot_it(x, color=color, legend_label=None):
        density = gaussian_kde(x)
        x_min = min(x)
        x_max = max(x)
        xs = np.linspace(x_min - int(x_max * .5), x_max + int(x_max * .5), 2000)
        density.covariance_factor = lambda : covariance_factor
        density._compute_covariance()
        
        for width, alpha in zip(a, b):
            plt.plot(xs, density(xs), color=color, alpha= alpha, lw= width)
        plt.plot(xs, density(xs), color=color, label=legend_label)
        
        if fill:
            plt.fill_between(xs, density(xs), color=color, alpha=fill_alpha)

    
    
    # Checking if X is from list, array, series or tuple (in short not df)
    if not isinstance(x, (pd.DataFrame)):
        colr = color if isinstance(color, str) else color[0]
        plot_it(x, legend_label=legend_label)
        
    # Means DF is passed
    else:
        columns = [*x.columns]
        color = cycle_colors(color)
        for colorId, col in enumerate(columns):
            colr = next(color)
            plot_it(x[col], colr, legend_label=col)
            
    if legend: plt.legend()
    return ax

# ------------------------------------ ANOTHER ------------------------------------------

def scatterplot(x, y, spines=True, point_size=2,
                color="#59ffc5", point_marker='o', font_dict=dict(),
                show_values=None, ax=None, labels=None, legend=False, legend_label=None):
    
    fig = plt.gcf()
    ax = ax or plt.gca()
    font_dict['color'] = color
    plot_configure(ax, spines_yn=spines)
    size, alpha, point = get_point(fig, point_size=point_size)
    
    for size, alpha in zip(size, alpha):
        plt.scatter(x, y, s=size, alpha=alpha, color=color, marker=point_marker)
    plt.scatter(x, y, s=point, color=color, marker=point_marker, label=legend_label)
    
    if show_values == True:
        if not labels:
            for x, y in zip(x, y):
                plt.text(x, y, str(y), **font_dict)
        else:
            values = list(iter(labels))
            if len(values) == len(x):
                for x, y, value in zip(x, y, values):
                    plt.text(x, y, str(value), **font_dict)
            else: raise NotImplementedError("The length is not matching")
                
    
    if legend: plt.legend()        
    return ax

# ------------------------------------- ANOTHER ---------------------------------------

def histplot(x, spines=True, color="#59ffc5", font_dict=dict(),
             show_values=False, ax=None, bins=None, lw=25, text_offset_xy=(0, 1)):
    
    if isinstance(x, pd.DataFrame):
        print("DataFrames are not supported now. Please provide 1D object - Series/Array/List etc.")
        return
    
    fig = plt.gcf()
    ax = ax or plt.gca()
    plot_configure(ax, spines_yn=spines)
    a, b = get_lw(lw)
    
    for width, alpha in zip(a, b):
        plt.hist(x, edgecolor=color, facecolor= (0, 0, 0, 0), linewidth=width, 
                 alpha=alpha, bins=bins)
    height, locs, _ = plt.hist(x, edgecolor=color, facecolor= (0, 0, 0, 0), bins=bins);
    
    if show_values == True:
        font_dict['color'] = color
        loc_mean = []
        for i in range(len(locs) - 1):
            mean = locs[i:i+2].mean()
            loc_mean.append(mean)
        
        xo, yo = text_offset_xy
        for x, y in zip(loc_mean, height):
            if y > 0: plt.text(x - xo, y - yo, str(int(y)), **font_dict)
        
    return ax