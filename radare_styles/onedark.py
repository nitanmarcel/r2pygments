
from pygments.style import Style
from pygments.token import *

class R2OnedarkStyle(Style):
    name = 'r2onedark'
    background_color = "#ec7"
    styles = {
        Name.Variable: '#61afef',
        Keyword.Type: 'white',
        Name.Variable: '#61afef',
        Generic.Prompt: '#d19a66',
        Name.Function: '#56b6c2',
        Name.Label: '#56b6c2',
        Name.Function: '#e06c75',
        Keyword: '#c678dd',
        Keyword: '#c678dd',
        Keyword: '#c678dd',
        Name.Label: '#366',
        Comment: '#56b6c2',
        Number: '#be5046',
        Name.Variable: '#e5c07b',
        Generic.Emph: '#98c379',
        Name.Constant: '#56b6c2',
        Generic.Emph: '#98c379',
    }
