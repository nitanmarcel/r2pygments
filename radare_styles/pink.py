
from pygments.style import Style
from pygments.token import *

class R2PinkStyle(Style):
    name = 'r2pink'
    background_color = "#72d"
    highlight_color = "#fdf"
    styles = {
        Comment: '#72d',
        Generic.Emph: '#f5d',
        Name.Function: '#000',
        Name.Constant: '#f5d',
        Name.Label: '#72d',
        Generic.Prompt: '#f5d',
        Text: '#d5a',
        Keyword: '#a7f',
        Comment.Special: '#f5d',
        Name.Variable: '#72d',
        Number: '#72d',
        Generic.Inserted: '#f5d',
        Generic.Deleted: '#715',
        Generic: '#f5d',
        Generic.Strong: '#f5d',
        Generic.Traceback: '#a7f',
        Keyword.Type: 'blue',
    }
