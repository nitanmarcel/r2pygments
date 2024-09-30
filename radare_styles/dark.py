
from pygments.style import Style
from pygments.token import *

class R2DarkStyle(Style):
    name = 'r2dark'
    background_color = "#366"
    styles = {
        Generic.Emph: '#366',
        Comment: '#99a',
        Name.Function: '#44f',
        Keyword: '#368',
        Name.Constant: '#99a',
        Generic.Emph: '#bbb',
        Keyword: '#368',
        Name.Function: '#99a',
        Name.Label: '#99a',
        Number: '#99a',
        Name.Label: '#366',
        Generic.Prompt: '#366',
        Name.Variable: '#368',
        Keyword: '#368',
        Name.Variable: '#99a',
        Keyword.Type: '#636',
        Name.Variable: '#99a',
    }
