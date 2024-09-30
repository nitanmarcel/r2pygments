
from pygments.style import Style
from pygments.token import *

class R2GbStyle(Style):
    name = 'r2gb'
    background_color = "#86c06c"
    styles = {
        Comment: '#86c06c',
        Name.Function: '#e0f8cf',
        Name.Constant: '#e0f8cf',
        Name.Label: '#86c06c',
        Generic.Emph: '#86c06c',
        Generic.Prompt: '#e0f8cf',
        Name.Label: '#306850',
        Keyword: '#e0f8cf',
        Keyword: '#e0f8cf',
        Keyword: '#e0f8cf',
        Name.Function: '#e0f8cf',
        Name.Variable: '#e0f8cf',
        Number: '#e0f8cf',
        Generic.Emph: '#e0f8cf',
        Name.Variable: '#86c06c',
        Keyword.Type: '#86c06c',
        Name.Variable: '#86c06c',
    }
