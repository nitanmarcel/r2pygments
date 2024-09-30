
from pygments.style import Style
from pygments.token import *

class R2AyuStyle(Style):
    name = 'r2ayu'
    background_color = "#888"
    styles = {
        Comment: '#cd4',
        Name.Constant: '#5de',
        Generic.Emph: '#cd4',
        Name.Function: '#5de',
        Generic.Emph: '#c2d94c',
        Keyword: '#c2d94c',
        Name.Label: '#5de',
        Number: '#f85',
        Name.Label: '#d74',
        Generic.Prompt: '#5de',
        Name.Function: '#f73',
        Name.Variable: 'yellow',
        Keyword: '#c2d94c',
        Keyword: '#c2d94c',
        Name.Variable: '#95e6cb',
        Keyword.Type: '#ffd580',
        Name.Variable: '#95e6cb',
    }
