# 🌸 Pink Jupyter Theme 🌸

<div>
  Data science just became <span style="color: #FF69B4;"> ✨ pink ✨</span>. I promise you won't regret installing this!
</div>

## <span style="color: #FF69B4;">🎀 Installation 🎀</span>


### <span style="color: #FF69B4;">🚀 Quick Install</span>

1. **Clone this repository:**
```bash
git clone https://github.com/alexandertsai/pink-jupyter-theme.git
cd pink-jupyter
```

2. **Choose your setup:**

#### <span style="color: #FF69B4;">Option A: Universal (Recommended)</span>
```bash
pip install nbclassic
# Input 1 or 2

python install_theme.py

jupyter nbclassic
```

#### <span style="color: #FF69B4;">Option B: Can't Install nbclassic</span>
```bash

python install_theme.py
# Input 3

jupyter lab
# OR
jupyter notebook
```

The <span style="color: #FF1493;">pink</span> theme will be applied automatically!

## <span style="color: #FF69B4;">Pink Matplotlib Plots (Highly Recommended)</span>

To make your matplotlib plots match the pink theme automatically, use the included style file:

```python
import matplotlib.pyplot as plt
plt.style.use('/path/to/pink.mplstyle') # use the absolute path
```

## <span style="color: #FF69B4;">Collapsible Features</span>

### <span style="color: #FF69B4;">For `custom.css` and `custom_less.css` users:</span>

Install these extensions for enhanced collapsible functionality:

```bash
# For collapsible headings
pip install nbclassic-collapsible-headings

# For code folding within cells  
pip install nbextension-cellfolding
```

### <span style="color: #FF69B4;">For `custom_no_nbclassic.css` users:</span>

**No extensions needed!** This version uses native collapsible features:

- **JupyterLab**: Click the blue bar to the left of cells to collapse them
- **Classic Notebook**: Built-in collapsible features (if available)
- **All interfaces**: Beautiful pink-themed collapse indicators

All versions include beautiful <span style="color: #FF69B4;">pink</span>-themed collapsible controls! ✨

## <span style="color: #FF69B4;">Usage</span>

Once installed, the theme is applied automatically to all Jupyter notebooks. Try the demo notebook <span style="color: #C71585;">`demo.ipynb`</span> to see all the theme features!



## <span style="color: #FF69B4;">Customization</span>

You can customize the theme by editing the <span style="color: #C71585;">`custom.css`</span> file. Some easy modifications:

- <span style="color: #FF1493;">Change pink shades</span> by updating the color hex codes
- <span style="color: #FF1493;">Adjust font sizes</span> in the `.CodeMirror` class  
- <span style="color: #FF1493;">Modify cell padding</span> in the `div.cell` class

## <span style="color: #FF69B4;">Theme Colors</span>

The <span style="color: #FF1493;">pink</span>  theme uses these slay colors:

- <span style="color:#FFF0F5; background-color:#333;">**Background**: Lavender Blush (#FFF0F5)</span>
- <span style="color:#FFB6C1">**Light Pink**: #FFB6C1</span>
- <span style="color:#FF69B4">**Hot Pink**: #FF69B4</span>
- <span style="color:#FF1493">**Deep Pink**: #FF1493</span>
- <span style="color:#C71585">**Medium Violet Red**: #C71585</span>
- <span style="color:#4B0082">**Text**: Indigo (#4B0082)</span>

The included <span style="color: #C71585;">pink.mplstyle</span> uses these colors for plots:</span>

1. <span style="color:#FF69B4">**Hot Pink**: #FF69B4</span> (primary plot color)
2. <span style="color:#C71585">**Medium Violet Red**: #C71585</span> (secondary plot color)
3. <span style="color:#FF1493">**Deep Pink**: #FF1493</span>
4. <span style="color:#FFB6C1">**Light Pink**: #FFB6C1</span>
5. <span style="color:#DB7093">**Pale Violet Red**: #DB7093</span>
6. <span style="color:#8B1538">**Burgundy**: #8B1538</span>
7. <span style="color:#FF6347">**Tomato**: #FF6347</span>
8. <span style="color:#BC8F8F">**Rosy Brown**: #BC8F8F</span>

## <span style="color: #FF69B4;">Uninstallation</span>

Please don't! But if you must...

```bash
python install_theme.py uninstall
```



## <span style="color: #FF69B4;">💞 Contributing 💞</span>

Feel free to submit issues or pull requests if you have suggestions for improvements!

## <span style="color: #FF69B4;">License</span>

This theme is released under the MIT License. Feel free to use and modify as needed.

---
<br>
<div align="center">
  <span style="color: #FF69B4; font-size: 18px;">Made with 💕 for the Jupyter community (and Allison)</span>
</div>