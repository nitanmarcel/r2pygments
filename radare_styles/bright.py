
from pygments.style import Style
from pygments.token import *

class R2BrightStyle(Style):
    name = 'r2bright'
    background_color = "#303030"
    styles = {
        Name.Function: '#00ff00',
        Keyword: '#00ff00',
        Comment: '#ff0000',
        Name.Constant: '#00ffff',
        Generic.Emph: '#00ffff',
        Name.Function: '#ff0000',
        Generic.Emph: '#00ff00',
        Keyword: '#00ff00',
        Name.Label: '#00ffff',
        Number: '#ffff00',
        Name.Label: '#00ff00',
        Generic.Prompt: '#ffff00',
        Name.Variable: '#00ffff',
        Keyword: '#00ff00',
        Name.Variable: '#ffffff',
        Keyword.Type: '#ffff00',
        Name.Variable: '#ffffff',
    }
