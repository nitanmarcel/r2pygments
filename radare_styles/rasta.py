
from pygments.style import Style
from pygments.token import *

class R2RastaStyle(Style):
    name = 'r2rasta'
    background_color = "yellow"
    styles = {
        Comment: 'green',
        Name.Function: 'yellow',
        Name.Constant: 'yellow',
        Name.Label: 'yellow',
        Generic.Emph: 'green',
        Generic.Prompt: 'green',
        Name.Label: 'yellow',
        Keyword: 'red',
        Keyword: 'red',
        Keyword: 'red',
        Name.Function: 'red',
        Name.Variable: 'green',
        Number: 'red',
        Generic.Emph: 'yellow',
        Name.Variable: 'green',
        Keyword.Type: 'red',
        Name.Variable: 'green',
    }
