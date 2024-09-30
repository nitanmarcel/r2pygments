
from pygments.style import Style
from pygments.token import *

class R2BehelitStyle(Style):
    name = 'r2behelit'
    background_color = "#68f"
    highlight_color = "#1f1f1f"
    styles = {
        Text: '#4e4e4e',
        Name.Label: '#5f87ff',
        Generic.Emph: '#af87d7',
        Generic.Prompt: '#5f87ff',
        Comment: '#ff005f',
        Comment.Special: '#000000',
        Name.Constant: '#5f87ff',
        Name.Function: '#000000',
        Keyword: '#000000',
        Number: '#af87ff',
        Name.Variable: '#ff005f',
        Generic: '#5f87ff',
        Generic.Inserted: '#00ff5f',
        Generic.Deleted: '#ff005f',
        Generic.Strong: '#5f87ff',
        Generic.Traceback: '#ffff5f',
        Keyword.Type: 'blue',
    }
