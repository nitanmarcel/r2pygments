# Radare2 Pygments styles
Radare2 themes as pygments styles 


## Generate styles

### from source files
```bash
python3 -m radare_styles.generator {in[file/dir]} {out[file/dir]}
``` 

### at runtime from source string as class
```python3
>>> theme = """
... ecd
... ec ai.exec rgb:6d6
... ec ai.read rgb:66d
... ec ai.write rgb:d66
... """

>>> from radare_styles.generator import generate_pygments_style
>>> cls = generate_pygments_style(theme, "themename")
<class 'pygments.style.R2ThemenameStyle'>
```

### at runtime from source string as dict
```python3
>>> theme = """
... ecd
... ec ai.exec rgb:6d6
... ec ai.read rgb:66d
... ec ai.write rgb:d66
... """

>>> from radare_styles.generator import generate_pygments_style_dict
>>> _dict = generate_pygments_style_dict(theme, "themename")
{'background_color': '#000', 'name': 'r2name', ...}
```

### at runtime from prebuild styles
```python3
>>> from radare_styles import get_style
>>> get_style("ayu")
<class 'radare_styles.ayu.R2AyuStyle'>
```