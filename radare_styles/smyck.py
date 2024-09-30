
from pygments.style import Style
from pygments.token import *

class R2SmyckStyle(Style):
    name = 'r2smyck'
    background_color = "#bb5"
    styles = {
        Name.Function: '#9f4',
        Keyword: '#9c4',
        Keyword: '#9c4',
        Keyword: '#9c4',
        Comment: '#9df',
        Number: '#bb5',
        Generic.Emph: '#888',
        Name.Function: '#9df',
        Name.Label: '#9df',
        Name.Label: '#bb5',
        Generic.Prompt: '#bb5',
        Name.Variable: '#fff',
        Generic.Emph: '#fd6',
        Name.Constant: '#9df',
        Name.Variable: '#9df',
        Keyword.Type: '#fd6',
        Name.Variable: '#9df',
    }
