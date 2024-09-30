
from pygments.style import Style
from pygments.token import *

class R2BehelitStyle(Style):
    name = 'r2behelit'
    background_color = "#68f"
    styles = {
        Name.Label: '#4e4e4e',
        Generic.Emph: '#5f87ff',
        Generic.Prompt: '#5f87ff',
        Generic.Emph: '#af87d7',
        Comment: '#ff005f',
        Name.Constant: '#5f87ff',
        Name.Function: '#5f87ff',
        Name.Label: '#5f87ff',
        Name.Function: '#000000',
        Keyword: '#000000',
        Keyword: '#000000',
        Keyword: '#000000',
        Number: '#af87ff',
        Name.Variable: '#5fff5f',
        Name.Variable: '#ff005f',
        Keyword.Type: 'blue',
        Name.Variable: '#ff005f',
    }
