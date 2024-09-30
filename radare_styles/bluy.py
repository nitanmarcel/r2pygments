
from pygments.style import Style
from pygments.token import *

class R2BluyStyle(Style):
    name = 'r2bluy'
    background_color = "#000"
    highlight_color = "#000000"
    styles = {
        Comment: '#fc1',
        Name.Function: 'magenta',
        Name.Constant: '#fc1',
        Name.Label: '#666',
        Generic.Emph: '#e71',
        Generic.Prompt: '#09f',
        Text: '#09f',
        Keyword: '#09f',
        Name.Variable: '#09f',
        Number: '#fc1',
        Generic.Strong: '#aaf',
        Keyword.Type: '#99a',
    }
