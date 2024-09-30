
from pygments.style import Style
from pygments.token import *

class R2ConsonanceStyle(Style):
    name = 'r2consonance'
    background_color = "#4cf"
    styles = {
        Name.Function: '#f2a',
        Keyword: '#4cf',
        Keyword: '#4cf',
        Keyword: '#4cf',
        Comment: '#fcc',
        Generic.Emph: '#789',
        Name.Function: '#ee0',
        Name.Label: '#ee0',
        Number: '#fff',
        Name.Label: '#888',
        Generic.Prompt: '#4cf',
        Name.Variable: '#789',
        Generic.Emph: '#ee0',
        Name.Constant: '#4cf',
        Name.Variable: '#fcc',
        Keyword.Type: '#f2a',
        Name.Variable: '#fcc',
    }
