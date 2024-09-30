
from pygments.style import Style
from pygments.token import *

class R2DarkStyle(Style):
    name = 'r2dark'
    background_color = "#366"
    highlight_color = "#004"
    styles = {
        Generic.Emph: '#bbb',
        Comment: '#99a',
        Comment.Special: '#368',
        Name.Function: '#99a',
        Keyword: '#368',
        Name.Constant: '#99a',
        Name.Label: '#366',
        Number: '#99a',
        Text: '#bbb',
        Generic.Prompt: '#366',
        Name.Variable: '#99a',
        Generic: '#06c',
        Generic.Inserted: '#06c',
        Generic.Deleted: '#035',
        Generic.Strong: '#99a',
        Generic.Traceback: '#bbb',
        Keyword.Type: '#636',
    }
