
from pygments.style import Style
from pygments.token import *

class R2PinkStyle(Style):
    name = 'r2pink'
    background_color = "#72d"
    styles = {
        Comment: '#72d',
        Generic.Emph: '#f5d',
        Name.Function: '#f5d',
        Name.Constant: '#f5d',
        Name.Label: '#f5d',
        Generic.Emph: '#f5d',
        Generic.Prompt: '#f5d',
        Name.Label: '#72d',
        Keyword: '#f5d',
        Keyword: '#f5d',
        Keyword: '#f5d',
        Name.Function: '#000',
        Name.Variable: '#f5d',
        Number: '#72d',
        Name.Variable: '#72d',
        Keyword.Type: 'blue',
        Name.Variable: '#72d',
    }
