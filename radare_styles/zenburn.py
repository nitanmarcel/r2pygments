
from pygments.style import Style
from pygments.token import *

class R2ZenburnStyle(Style):
    name = 'r2zenburn'
    background_color = "#8dd"
    styles = {
        Name.Function: '#d52',
        Keyword: '#d52',
        Keyword: '#d52',
        Keyword: '#d52',
        Comment: '#7a7',
        Generic.Emph: '#d50',
        Name.Function: '#d50',
        Name.Label: '#d50',
        Number: '#c88',
        Name.Label: '#aaa',
        Generic.Prompt: '#d50',
        Name.Variable: '#8dd',
        Generic.Emph: '#ffc',
        Name.Constant: '#d50',
        Name.Variable: '#7a7',
        Keyword.Type: '#eec',
        Name.Variable: '#7a7',
    }
