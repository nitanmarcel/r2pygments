
from pygments.style import Style
from pygments.token import *

class R2MatrixStyle(Style):
    name = 'r2matrix'
    background_color = "#0b0"
    styles = {
        Name.Function: '#0b0',
        Keyword: '#2f2',
        Keyword: '#2f2',
        Keyword: '#2f2',
        Comment: '#060',
        Generic.Emph: 'bgreen',
        Name.Function: '#0b0',
        Name.Label: '#0f0',
        Number: '#3f3',
        Name.Label: '#383',
        Generic.Prompt: '#080',
        Name.Variable: '#1a1',
        Generic.Emph: '#0b0',
        Name.Constant: '#0f0',
        Name.Variable: '#060',
        Keyword.Type: '#383',
        Name.Variable: '#060',
    }
