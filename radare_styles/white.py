
from pygments.style import Style
from pygments.token import *

class R2WhiteStyle(Style):
    name = 'r2white'
    background_color = "blue"
    highlight_color = "#ff0"
    styles = {
        Name.Label: 'black',
        Generic.Emph: 'blue',
        Text: 'blue',
        Keyword: 'green',
        Name.Function: 'blue',
        Generic.Prompt: 'black',
        Name.Constant: 'blue',
        Comment: 'magenta',
        Comment.Special: 'green',
        Name.Variable: 'magenta',
        Number: 'blue',
        Generic: 'blue',
        Generic.Inserted: 'green',
        Generic.Deleted: 'red',
        Generic.Strong: '#0ff',
        Generic.Traceback: 'red',
        Keyword.Type: 'blue',
    }
