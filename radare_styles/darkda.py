
from pygments.style import Style
from pygments.token import *

class R2DarkdaStyle(Style):
    name = 'r2darkda'
    background_color = "#099"
    styles = {
        Name.Function: '#ffd200',
        Keyword: '#9dd600',
        Keyword: '#9dd600',
        Comment: '#82607e',
        Number: '#d25032',
        Generic.Emph: '#00b1ab',
        Name.Function: '#00ffff',
        Name.Label: '#66d9ef',
        Name.Label: '#ababab',
        Generic.Prompt: '#fc0',
        Name.Variable: '#009d9d',
        Generic.Emph: '#009d9d',
        Keyword: '#9dd600',
        Name.Constant: '#00b1ab',
        Name.Variable: '#99a',
        Keyword.Type: '#df077e',
        Name.Variable: '#99a',
    }
