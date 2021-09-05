# neona
*Makes your viz glow*

### About<br>—
`neona` is just for your need to to glow up the charts that you love in python. Made purely in python using `Matplotlib` as the base library—it just adds glow!


### Motivation<br>—
About 3 months ago, I had to make a presentation where I chose the dark theme wanted to give a feel of "Dark Mode" in a drak room, yea-builtin styles of matplotlib and seaborn would have worked but still the theme and colors were not matching. It tried to give my own palette but still there was something still missing. A light. A light in dark. That was a beautiful **glow** in darkness.

I searched on internet about the glowing charts in python but they were so limited and saw that people are not interested in that much. Actully I stopped my search there because I wanted to create my own. I think the design trend is not on the *glow* side, people are moving for the *glass theme* or the *material theme* and just newly launched *neuomorphic* designs. But for darkmode? I found this would be an amazing choice for darkglow! (Ah "DarkGlow" kind of nice name, huh?)

Then I tried a couple of combinations, got some color palette and chose the syntax for my library. I wanted to make a compact library without much moving parts and simple but a syntax that allow many flexibilities and also should be appandable with your existing plt (sorry Matplotlib) skills. And then my very first glowing, lightning in dark — a line chart was ready. It was simple, without marks but it was looking awsome. And then it was the birth of `neona` ∞

### Features<br>—
- **6** most often used plots (adding more soon)
- Toggleable `show_values`
- Change `markers`
- Show values and control precision
- Works with almost all iterable objects (DataFrame, array, Series etc.)
- Attatch your `plt` calls easily
- Give any length of colors—it will cycle on them
- Specially chosen built-in glow suited color palettes (currently one)
- Adjustable glowness
- Auto legend
- "*Human Readable*" Docstring
- Open Source 😉

Actully there are more...!


### Basic Syntax
```python
# Import
import neona

# Plot Call
neona.lineplot(...)
```


### Glowzuals<br>—
(ie. vizuals)

# 1. LinePlot


