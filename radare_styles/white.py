
from pygments.style import Style
from pygments.token import *

class R2WhiteStyle(Style):
    name = 'r2white'
    background_color = "blue"
    styles = {
        Name.Label: '#c60',
        Generic.Emph: 'blue',
        Keyword: 'blue',
        Keyword: 'magenta',
        Keyword: 'green',
        Name.Function: 'magenta',
        Generic.Prompt: 'black',
        Name.Constant: 'blue',
        Name.Function: 'blue',
        Comment: 'magenta',
        Name.Variable: 'blue',
        Number: 'blue',
        Name.Label: 'black',
        Generic.Emph: 'blue',
        Name.Variable: 'magenta',
        Keyword.Type: 'blue',
        Name.Variable: 'magenta',
    }
