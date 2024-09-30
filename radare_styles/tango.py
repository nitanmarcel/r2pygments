
from pygments.style import Style
from pygments.token import *

class R2TangoStyle(Style):
    name = 'r2tango'
    background_color = "#bb5"
    highlight_color = "#004"
    styles = {
        Name.Function: '#ca0',
        Keyword: '#950',
        Comment: '#370',
        Comment.Special: '#7d1',
        Generic.Emph: '#ddd',
        Name.Label: '#bbb',
        Number: '#ca0',
        Text: '#950',
        Generic.Prompt: '#950',
        Name.Variable: '#370',
        Name.Constant: '#950',
        Generic.Inserted: '#370',
        Generic.Deleted: '#a00',
        Generic: '#950',
        Generic.Strong: '#7d1',
        Generic.Traceback: '#f00',
        Keyword.Type: '#a41',
    }
