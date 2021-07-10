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

def barplot(x, y, show_values=False, spines=True, color="#59ffc5", lw=25, font_dict=dict(),
            y_offset=0, ax=None):
    
    """
    NEONA
    —————

     _______________________________________________________    
    |This function plots a neon barplot. A column structure.|
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    
    About
    -----
    This function is the neon sibling of `plt.bar`. Here it will plot
    each category of your value with the respective height. 

    Try to utilize the `show_values` feature of this function for easy
    overview of the data.


    Parameters
    ----------
    x: Any 1D iterable — A base on which the bars will be plotted.
       It will be your x-axis.

    y: Any 1D iterable — The `height` of all individual bars. It 
        must be numerical.

    show_values: True / False — To toggle the numerical visibility
        of the values of `y`.

    spines: True / False — To toggle visibility of axes spines. As
        neona looks better with dark black and withot any borders!

    color: hex / str — value for color (only single color
         - multiple colors will be added soon)

    lw: int / float — it is `linewidth` to control the intensity 
        and thickness of the edge.

    font_dict: dict() — Any acceptable arguement for fonts in 
        matplotlib can be passed here. (Font colors are not
        supported now.)

    y_offset: int / flot  — Will set an offset for the `values`.
        If show_values is True.
       
    ax: plt.axes object.

    Example
    -------
    >>> ser = pd.Series(np.random.randint(0, 100, 5), index=list('abcde'))
    
    a    41
    b    37
    c    18
    d    49
    e    58
    dtype: int32

    >>> neona.barplot(ser.index, ser)

    Also see
    --------
    neona.lollipoplot()


    Future updates
    --------------
    • I am trying to provide more facilities. And currently working on vertical and
    horizontal layout for bar plot. Which can be accessed directly from here. 

    • Other thing is to add more color flexibilities for the fonts and the individual
    bars. But looking at the colors - there are a few / very few colors that can suite
    well with neon light. But still is under development.

    --- END ---

    """
    
    fig = plt.gcf()
    ax = ax or plt.gca()
    plot_configure(ax, spines_yn=spines)
    a, b = get_lw(lw)
    
    for width, alpha in zip(a, b):
        plt.bar(x, y, edgecolor=color, facecolor= (0, 0, 0, 0), linewidth=width, 
                 alpha=alpha)
    plt.bar(x, y, edgecolor=color, facecolor= (0, 0, 0, 0));
    
    if show_values == True:
        font_dict['color'] = color
        for x, y in zip(x, y):
            plt.text(x, y - y_offset, str(int(y)), **font_dict)    
        
    return ax

# -------------------------------------- ANOTHER -------------------------------------------


def lollipoplot(x, y, show_values=True, point_marker='o', point_size=2, 
                color="#59ffc5", spines=True, font_dict=dict(), ax=None, lw=15):

    """
    NEONA
    —————

     ___________________________________________________________    
    |This function plots a neon lollipop plot. A line structure.|
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    
    About
    -----
    This function will make you "wow". It is similar to the routine
    barplot, but the main difference is — this provides the functionality
    to choose the `point_marker` type and their respective sizes.

    This will plot a single vertical line for each category of your data
    and till the height provided in `y`.

    Another advantage is that — you can pass multiple colors for each individual
    lollipops and your plot will shine.
    

    Parameters
    ----------
    x: Any 1D iterable — A base on which the bars will be plotted.
       It will be your x-axis.

    y: Any 1D iterable — The `height` of all individual lollipop. It 
        must be numerical.

    show_values: True / False — To toggle the numerical visibility
        of the values of `y`.

    point_marker: Any acceptable format of markers in `plt.scatter`.
        Such as — 'o', 'x', 's'... Default is 'o'. This will change
        the look of the lollipop head.

    point_size: int / float — This will change the head size of the
        lollipop. 

    spines: True / False — To toggle visibility of axes spines. As
        neona looks better with dark black and withot any borders!

    color: hex / str / 1D iterable — value to provide color(s) to
        the lollipops. Single (color='r') or multiple (color=['r', 'purple'])
        will work. Works even when the colors are less than the total bars.

    lw: int / float — it is `linewidth` to control the intensity 
        and thickness of the edge of each lollipop.

    font_dict: dict() — Any acceptable arguement for fonts in 
        matplotlib can be passed here. (Font colors are not
        supported now.)
       
    ax: plt.axes object.
    
    
    Example
    -------
    >>> ser = pd.Series(np.random.randint(0, 100, 5), index=list('abcde'))
    
    a    41
    b    37
    c    18
    d    49
    e    58
    dtype: int32

        # With single color
    >>> neona.lollipoplot(ser.index, ser, color='r')

        # With multiple colors (even if their length is not same as data)
    >>> neona.lollipoplot(ser.index, ser, color=['r', 'cyan'])

        # With multiple colors built in neona
    >>> neona.lollipoplot(ser.index, ser, color=neona.neos1)

    Also see
    --------
    neona.barplot()


    Future updates
    --------------
    • I am trying to provide more facilities. And currently working on vertical and
    horizontal layout for lollipop plot. Which can be accessed directly from here. 

    --- END ---
    """
    
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

def lineplot(x, y= None, show_marks= True, point_marker= 'o', point_size= 2, show_values= True,
            color= "#59ffc5", lw=15, spines= True, font_dict= dict(), ax=None, 
            legend=False, legend_label=None):
    
    """
    NEONA
    —————

     ____________________________________
    |This function plots a neon Line plot|
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    
    About
    -----
    This function is when the neona really shines. (Actully shines)
    It is the sibling of `plt.plot`. Well, with plt.plot many kinds
    of plots like - connected, not connected, scatter etc. are possible
    but I have made this `neona.lineplot` with just the line structure
    (connected dots) in mind.

    So when you have the data which shows some progress or something else
    in which the value changes, you must use this.

    Good things
    -----------
    This function can accept `DataFrame` object directly and will apply the
    individual colors automatically to each column, each fonts and each points.

    Others like list, series and array can be passed to individually passed to as well.
    

    Parameters
    ----------
    x: DataFrame / List / Array / Series.
        If just DataFrame is passed then there is no need to pass `y`.
        This will automatically take index as x-axis and values of each
        column will be plotted with different colors as y-axis.
        (if multiple colors passed)

        If List / Array / Series passed and `y` is not passed. Then
        their index will be taken as x-axis and values as y-axis.

        If `x` and `y` are both passed. Then they both must be List /
        Array / Series. In that case - x's values will be on x-axis and
        y's values on the y-axis.

        You can't pass DF with Array / Series / List.


    y: [optional] Any 1D iterable — The `height` of all individual lollipop. It 
        must be numerical.

    show_marks: True / False — This will toggle the point intersection marks'
        visibility.
    
    point_marker: Any acceptable format of markers in `plt.plot`.
        Such as — 'o', 'x', 's'... Default is 'o'. This will change
        the look of the points' intersection head. (only if show_marks= True)
    
    point_size: int / float — This will change the head size of the
        points' intersection. (only if show_marks= True)

    show_values: True / False — To toggle the numerical visibility
        of the values of `y`.

    color: hex / str / 1D iterable — value to provide color(s) to the
        lines. Single (color='r') or multiple (color=['r', 'purple'])
        will work. Multiple colors will only makes sense if you are passing
        DataFrame as `x`. Only first color in that list will be used.

    lw: int / float — it is `linewidth` to control the intensity 
        and thickness of the edge of each lollipop.
        
    spines: True / False — To toggle visibility of axes spines. As
        neona looks better with dark black and withot any borders!

    font_dict: dict() — Any acceptable arguement for fonts in 
        matplotlib can be passed here. (Font colors are not
        supported now.)
    
    legend: True / False — Will show or hide legends. If the DataFrame is passed
        then the `legend_label` parameter will be not effective. It will automatically
        give the column names of that DataFrame in `x` to the legend. 

    legend_label: str — This will be used if the legend = True and the `x` is not DataFrame.
        The values passed in here will act asif you are passing `label` parameter in plt.plot(label="Value")
        and then calling plt.legend()

    ax: plt.axes object.
    
    
    Example
    -------
    >>> df = pd.DataFrame(np.random.randint(0, 100, (5,3)))
    
        0   1   2
    0  54  90  98
    1  30  23   6
    2  42  83  49
    3   6  21  73
    4   3  16   7

        # Passing DF
    >>> neona.lineplot(df, color=neona.neos1)

        # Passing Series ↓ (also series, right?)
    >>> neona.lineplot(df[0])

        # Passing both x and y
    >>> neona.lineplot(df[0], df[1])

    --- END ---
    """

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