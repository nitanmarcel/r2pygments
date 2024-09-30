
from pygments.style import Style
from pygments.token import *

class R2MatrixStyle(Style):
    name = 'r2matrix'
    background_color = "#0b0"
    highlight_color = "#020"
    styles = {
        Text: '#0a0',
        Name.Function: '#0b0',
        Keyword: '#0b0',
        Comment: '#060',
        Comment.Special: '#3f3',
        Generic.Emph: '#0b0',
        Name.Label: '#383',
        Number: '#3f3',
        Generic.Prompt: '#080',
        Name.Variable: '#060',
        Name.Constant: '#0f0',
        Generic: 'green',
        Generic.Inserted: 'green',
        Generic.Deleted: '#050',
        Generic.Strong: 'green',
        Generic.Traceback: '#060',
        Keyword.Type: '#383',
    }
