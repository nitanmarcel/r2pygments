
from pygments.style import Style
from pygments.token import *

class R2OnedarkStyle(Style):
    name = 'r2onedark'
    background_color = "#ec7"
    highlight_color = "#5c6370"
    styles = {
        Name.Variable: '#e5c07b',
        Keyword.Type: 'white',
        Generic.Prompt: '#d19a66',
        Name.Function: '#e06c75',
        Name.Label: '#366',
        Keyword: '#e06c75',
        Comment: '#56b6c2',
        Comment.Special: '#ff0',
        Number: '#be5046',
        Generic.Emph: '#98c379',
        Name.Constant: '#56b6c2',
        Generic: '#61afef',
        Generic.Inserted: '#98c379',
        Generic.Deleted: '#e06c75',
        Generic.Strong: '#61afef',
        Generic.Traceback: '#d19a66',
    }
