
from pygments.style import Style
from pygments.token import *

class R2GentooStyle(Style):
    name = 'r2gentoo'
    background_color = "cyan"
    styles = {
        Comment: 'cyan',
        Name.Function: 'green',
        Name.Constant: 'green',
        Name.Label: 'yellow',
        Generic.Emph: 'cyan',
        Generic.Emph: 'cyan',
        Generic.Prompt: 'green',
        Name.Label: 'yellow',
        Name.Function: 'green',
        Keyword: '#009000',
        Keyword: '#009000',
        Keyword: '#009000',
        Name.Variable: '#f0f0f0',
        Number: 'yellow',
        Name.Variable: 'white',
        Keyword.Type: 'yellow',
        Name.Variable: 'white',
    }
