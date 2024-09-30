
from pygments.style import Style
from pygments.token import *

class R2ZenburnStyle(Style):
    name = 'r2zenburn'
    background_color = "#8dd"
    highlight_color = "#004"
    styles = {
        Text: '#aaa',
        Name.Function: '#d50',
        Keyword: '#d22',
        Comment: '#7a7',
        Comment.Special: '#d52',
        Generic.Emph: '#ffc',
        Name.Label: '#aaa',
        Number: '#c88',
        Generic.Prompt: '#d50',
        Name.Variable: '#7a7',
        Name.Constant: '#d50',
        Generic: '#aaa',
        Generic.Inserted: '#aaa',
        Generic.Deleted: '#d52',
        Generic.Strong: 'blue',
        Generic.Traceback: 'red',
        Keyword.Type: '#eec',
    }
