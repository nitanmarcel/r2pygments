
from pygments.style import Style
from pygments.token import *

class R2CgaStyle(Style):
    name = 'r2cga'
    background_color = "#f0f"
    highlight_color = "#008"
    styles = {
        Comment: '#0ff',
        Comment.Special: '#f0f',
        Name.Function: '#f0f',
        Name.Constant: '#f0f',
        Keyword: '#f0f',
        Name.Label: '#0ff',
        Generic.Emph: '#0ff',
        Generic.Prompt: '#0ff',
        Text: '#fff',
        Name.Variable: '#f0f',
        Number: '#0ff',
        Generic: '#f0f',
        Generic.Inserted: '#f0f',
        Generic.Deleted: '#0ff',
        Generic.Strong: '#0ff',
        Generic.Traceback: '#f0f',
        Keyword.Type: '#f0f',
    }
