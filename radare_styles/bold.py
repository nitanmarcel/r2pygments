
from pygments.style import Style
from pygments.token import *

class R2BoldStyle(Style):
    name = 'r2bold'
    background_color = "yellow"
    highlight_color = "#008"
    styles = {
        Keyword: 'red',
        Comment.Special: 'black',
        Name.Variable: 'yellow',
        Name.Constant: 'yellow',
        Generic.Emph: 'yellow',
        Name.Function: 'black',
        Name.Label: 'white',
        Comment: 'yellow',
        Number: '#fff',
        Text: '#999',
        Generic.Prompt: 'black',
        Generic: '#ddd',
        Generic.Inserted: 'green',
        Generic.Deleted: 'red',
        Generic.Strong: '#f72',
        Generic.Traceback: '#f00',
        Keyword.Type: 'blue',
    }
