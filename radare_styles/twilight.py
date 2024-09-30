
from pygments.style import Style
from pygments.token import *

class R2TwilightStyle(Style):
    name = 'r2twilight'
    background_color = "#ffd"
    styles = {
        Name.Function: '#ffd',
        Keyword: '#ffd',
        Keyword: '#ffd',
        Keyword: '#ffd',
        Comment: '#c64',
        Generic.Emph: '#446',
        Name.Function: '#c64',
        Name.Label: '#788',
        Number: '#aaa',
        Name.Label: '#788',
        Generic.Prompt: '#788',
        Name.Variable: '#ca6',
        Generic.Emph: '#ab7',
        Name.Constant: '#ffd',
        Name.Variable: '#c64',
        Keyword.Type: '#aa6',
        Name.Variable: '#c64',
    }
