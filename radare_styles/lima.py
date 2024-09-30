
from pygments.style import Style
from pygments.token import *

class R2LimaStyle(Style):
    name = 'r2lima'
    background_color = "#ef0"
    styles = {
        Comment: '#af2',
        Name.Function: '#af2',
        Name.Constant: '#af2',
        Name.Label: '#af2',
        Generic.Emph: '#af2',
        Generic.Prompt: '#090',
        Name.Label: '#ef0',
        Keyword: '#af2',
        Keyword: '#af2',
        Keyword: '#af2',
        Name.Function: '#fff',
        Name.Variable: '#af2',
        Number: '#ef0',
        Generic.Emph: '#af2',
        Name.Variable: 'yellow',
        Keyword.Type: 'green',
        Name.Variable: 'yellow',
    }
