
from pygments.style import Style
from pygments.token import *

class R2TangoStyle(Style):
    name = 'r2tango'
    background_color = "#bb5"
    styles = {
        Name.Function: '#7d1',
        Keyword: '#370',
        Keyword: '#370',
        Keyword: '#370',
        Comment: '#370',
        Generic.Emph: '#248',
        Name.Function: '#ca0',
        Name.Label: '#c50',
        Number: '#ca0',
        Name.Label: '#bbb',
        Generic.Prompt: '#950',
        Name.Variable: '#c50',
        Generic.Emph: '#ddd',
        Name.Constant: '#950',
        Name.Variable: '#370',
        Keyword.Type: '#a41',
        Name.Variable: '#370',
    }
