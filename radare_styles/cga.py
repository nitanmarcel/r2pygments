
from pygments.style import Style
from pygments.token import *

class R2CgaStyle(Style):
    name = 'r2cga'
    background_color = "#f0f"
    styles = {
        Comment: '#0ff',
        Name.Function: '#f0f',
        Name.Constant: '#f0f',
        Name.Label: '#f0f',
        Generic.Emph: '#f0f',
        Generic.Prompt: '#0ff',
        Name.Label: '#0ff',
        Keyword: '#f0f',
        Keyword: '#f0f',
        Name.Function: '#f0f',
        Name.Variable: '#f0f',
        Number: '#0ff',
        Generic.Emph: '#0ff',
        Keyword: '#f0f',
        Name.Variable: '#f0f',
        Keyword.Type: '#f0f',
        Name.Variable: '#f0f',
    }
