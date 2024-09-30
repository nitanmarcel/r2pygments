
from pygments.style import Style
from pygments.token import *

class R2BasicStyle(Style):
    name = 'r2basic'
    background_color = "white"
    styles = {
        Name.Function: 'cyan',
        Name.Label: 'cyan',
        Name.Constant: 'green',
        Name.Label: 'white',
        Comment: 'red',
        Generic.Emph: 'green',
        Keyword: 'green',
        Generic.Emph: 'yellow',
        Generic.Prompt: 'cyan',
        Name.Variable: 'yellow',
        Number: 'cyan',
        Name.Function: 'green',
        Keyword: 'green',
        Keyword: 'green',
        Name.Variable: 'white',
        Keyword.Type: 'blue',
        Name.Variable: 'white',
    }
