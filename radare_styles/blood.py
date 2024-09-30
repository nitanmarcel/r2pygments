
from pygments.style import Style
from pygments.token import *

class R2BloodStyle(Style):
    name = 'r2blood'
    background_color = "#f00"
    styles = {
        Name.Function: '#faa',
        Keyword: '#faa',
        Keyword: '#faa',
        Keyword: '#faa',
        Comment: '#700',
        Name.Variable: '#f00',
        Name.Constant: '#f00',
        Generic.Emph: '#f00',
        Name.Function: '#f00',
        Generic.Emph: '#f00',
        Name.Label: '#f00',
        Number: '#f00',
        Name.Label: '#500',
        Generic.Prompt: '#f00',
        Name.Variable: '#f00',
        Keyword.Type: '#700',
        Name.Variable: '#f00',
    }
