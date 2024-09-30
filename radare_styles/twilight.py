
from pygments.style import Style
from pygments.token import *

class R2TwilightStyle(Style):
    name = 'r2twilight'
    background_color = "#ffd"
    highlight_color = "#004"
    styles = {
        Text: '#aaa',
        Name.Function: '#c64',
        Keyword: '#bb7',
        Comment: '#c64',
        Comment.Special: '#9b7',
        Generic.Emph: '#ab7',
        Name.Label: '#788',
        Number: '#aaa',
        Generic.Prompt: '#788',
        Name.Variable: '#c64',
        Name.Constant: '#ffd',
        Generic.Inserted: '#9b7',
        Generic.Deleted: '#b97',
        Generic: '#9b7',
        Generic.Strong: 'blue',
        Generic.Traceback: 'blue',
        Keyword.Type: '#aa6',
    }
