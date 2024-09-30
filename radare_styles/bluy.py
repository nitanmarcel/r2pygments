
from pygments.style import Style
from pygments.token import *

class R2BluyStyle(Style):
    name = 'r2bluy'
    background_color = "#000000"
    styles = {
        Comment: '#fc1',
        Name.Function: '#fc1',
        Name.Constant: '#fc1',
        Name.Label: '#fc1',
        Generic.Emph: '#3cf',
        Generic.Emph: '#e71',
        Generic.Prompt: '#09f',
        Name.Label: '#666',
        Keyword: '#e71',
        Keyword: '#e71',
        Name.Function: 'magenta',
        Name.Variable: '#3cf',
        Number: '#fc1',
        Name.Variable: '#555',
        Name.Variable: '#09f',
        Keyword.Type: '#99a',
    }
