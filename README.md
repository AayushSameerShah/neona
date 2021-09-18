# neona
*Makes your viz glow*

![mainPoster](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/Poster%20Final.png)
![commit][commit-badge]
![license][license-badge]

### 📖 About<br>—
`neona` is just for your need to to glow up the charts that you love in python. Made purely in python using `Matplotlib` as the base library—it just adds glow!


### 🙌 Motivation<br>—
About 3 months ago, I had to make a presentation where I chose the dark theme wanted to give a feel of "Dark Mode" in a drak room, yea-builtin styles of matplotlib and seaborn would have worked but still the theme and colors were not matching. It tried to give my own palette but still there was something still missing. A light. A light in dark. That was a beautiful **glow** in darkness.

I searched on internet about the glowing charts in python but they were so limited and saw that people are not interested in that much. Actully I stopped my search there because I wanted to create my own. I think the design trend is not on the *glow* side, people are moving for the *glass theme* or the *material theme* and just newly launched *neuomorphic* designs. But for darkmode? I found this would be an amazing choice for darkglow! (Ah "DarkGlow" kind of nice name, huh?)

Then I tried a couple of combinations, got some color palette and chose the syntax for my library. I wanted to make a compact library without much moving parts and simple but a syntax that allow many flexibilities and also should be appandable with your existing plt (sorry Matplotlib) skills. And then my very first glowing, lightning in dark — a line chart was ready. It was simple, without marks but it was looking awsome. And then it was the birth of `neona` ∞

### 🧰 Features<br>—
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


### ⚛️ Basic Syntax
```python
# Import
import neona

# Plot Call
neona.lineplot(...)
```


### 📈 Glowzuals<br>—
(ie. vizuals)

# 1. Line Plot
![lineplot_steps](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/line_1.png)
![lineplot_male_female](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/line_2.png)

# 2. LollipoPlot
![lollipoplot](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/lollipop_1.png)
<img src="https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/lollipop_1mini.png" height=30% width=50%><img src="https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/lollipop_1minii.png" height=30% width=50%>

# 3. KDE Plot
![kde](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/kde_1.png)

# 4. Bar Plot
![bar](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/bar_1.png)

# 5. Scatter Plot
![scatter_1](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/scatter_1.png)
![scatter_2](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/scatter_2.png)
![scatter_3](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/scatter_3.png)

# 6. Hist Plot
![hist](https://github.com/AayushSameerShah/neona/blob/AddPrecision/Posters%20and%20Thumbnails/hist_1.png)


And there is a lot in it when you try it out yourself.
## 😄 Requirements<br>—
 - numpy
 - pandas
 - matplotlib
 - scipy

(Any version of those will work)

**A Small advice:** This library is focused more on the aesthetics not on the performance. It creates many layers of shades to create the desired glow effect. The advice is to use `neona` in your final presentation or when you want to show your findings. It may take a while to generate whole plot from scratch. So, using `neona` during your analysis is not advised.

## 🤝 Please, pardon my dust.
This is my very first trial to make such work and make it usable to everyone. There can be many things which you may find broken with `neona`. If you are a contributor, then please support this project to make it better and more accessible.

*Tell me if your presentation doesn't glow! Good Luck 😉*

___

**Thanks!**<br>
*∞ Aayush Shah*

[commit-badge]: https://img.shields.io/github/commit-activity/m/AayushSameerShah/neona
[license-badge]: https://img.shields.io/github/license/AayushSameerShah/neona
