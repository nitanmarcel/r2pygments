
from pygments.style import Style
from pygments.token import *

class R2LimaStyle(Style):
    name = 'r2lima'
    background_color = "#ef0"
    highlight_color = "#140"
    styles = {
        Comment: '#af2',
        Comment.Special: '#af2',
        Name.Function: '#fff',
        Name.Constant: '#af2',
        Name.Label: '#ef0',
        Generic.Emph: '#af2',
        Generic.Prompt: '#090',
        Text: '#090',
        Keyword: '#0a0',
        Name.Variable: 'yellow',
        Number: '#ef0',
        Generic: '#af2',
        Generic.Inserted: '#ef2',
        Generic.Deleted: '#5d5',
        Generic.Strong: '#af2',
        Generic.Traceback: '#090',
        Keyword.Type: 'green',
    }
