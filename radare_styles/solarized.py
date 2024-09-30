
from pygments.style import Style
from pygments.token import *

class R2SolarizedStyle(Style):
    name = 'r2solarized'
    background_color = "#bb5"
    styles = {
        Name.Function: '#890',
        Keyword: '#890',
        Keyword: '#890',
        Keyword: '#e37',
        Comment: '#28d',
        Generic.Emph: '#3a9',
        Name.Function: '#d33',
        Name.Label: '#77c',
        Number: '#eee',
        Name.Label: '#9aa',
        Generic.Prompt: '#c41',
        Name.Variable: '#de8',
        Generic.Emph: '#e37',
        Name.Constant: '#c41',
        Name.Variable: '#28d',
        Keyword.Type: '#cc8',
        Name.Variable: '#28d',
    }
