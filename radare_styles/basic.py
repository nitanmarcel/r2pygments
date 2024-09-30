
from pygments.style import Style
from pygments.token import *

class R2BasicStyle(Style):
    name = 'r2basic'
    background_color = "white"
    highlight_color = "#004"
    styles = {
        Name.Function: 'green',
        Name.Label: 'white',
        Name.Constant: 'green',
        Comment: 'red',
        Comment.Special: 'green',
        Generic.Emph: 'yellow',
        Text: 'gray',
        Keyword: 'cyan',
        Generic.Prompt: 'cyan',
        Name.Variable: 'white',
        Number: 'cyan',
        Generic.Inserted: 'green',
        Generic.Deleted: 'red',
        Generic: 'gray',
        Generic.Strong: 'blue',
        Generic.Traceback: 'blue',
        Keyword.Type: 'blue',
    }
