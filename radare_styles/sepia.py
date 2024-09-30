
from pygments.style import Style
from pygments.token import *

class R2SepiaStyle(Style):
    name = 'r2sepia'
    background_color = "#db7"
    styles = {
        Name.Function: '#ffffff',
        Keyword: '#fec',
        Keyword: '#fec',
        Keyword: '#fec',
        Comment: '#fd9',
        Generic.Emph: '#ca6',
        Name.Function: '#bb7',
        Name.Label: '#788',
        Number: '#960',
        Name.Label: '#960',
        Generic.Prompt: '#960',
        Name.Variable: '#ca6',
        Generic.Emph: '#ab7',
        Name.Constant: '#ffd',
        Name.Variable: '#fd9',
        Keyword.Type: '#850',
        Name.Variable: '#fd9',
    }
