
from pygments.style import Style
from pygments.token import *

class R2FocusStyle(Style):
    name = 'r2focus'
    background_color = "#ff0"
    styles = {
        Name.Function: '#0cf',
        Name.Label: '#0cf',
        Name.Function: '#ff0',
        Keyword: '#ff0',
        Keyword: '#ff0',
        Keyword: '#ff3',
        Name.Label: '#fff',
        Generic.Prompt: 'byellow',
        Comment: '#0cf',
        Number: '#ff0',
        Name.Variable: '#6f0',
        Generic.Emph: '#ff3',
        Name.Variable: 'cyan',
        Keyword.Type: '#f3f',
        Name.Variable: 'cyan',
    }
