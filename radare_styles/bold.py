
from pygments.style import Style
from pygments.token import *

class R2BoldStyle(Style):
    name = 'r2bold'
    background_color = "yellow"
    styles = {
        Name.Variable: 'green',
        Name.Constant: 'yellow',
        Generic.Emph: 'yellow',
        Name.Function: 'black',
        Generic.Emph: 'yellow',
        Name.Label: 'white',
        Comment: 'yellow',
        Name.Function: 'black',
        Number: '#fff',
        Keyword: 'yellow',
        Keyword: 'yellow',
        Keyword: 'yellow',
        Name.Label: 'white',
        Generic.Prompt: 'black',
        Name.Variable: 'yellow',
        Keyword.Type: 'blue',
        Name.Variable: 'yellow',
    }
