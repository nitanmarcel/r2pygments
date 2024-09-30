
from pygments.style import Style
from pygments.token import *

class R2BloodStyle(Style):
    name = 'r2blood'
    background_color = "#f00"
    highlight_color = "#111"
    styles = {
        Name.Function: '#f00',
        Keyword: '#f00',
        Comment: '#700',
        Comment.Special: '#f00',
        Name.Variable: '#f00',
        Name.Constant: '#f00',
        Generic.Emph: '#f00',
        Name.Label: '#500',
        Number: '#f00',
        Text: '#900',
        Generic.Prompt: '#f00',
        Generic.Inserted: '#f00',
        Generic.Deleted: '#700',
        Generic: '#f00',
        Generic.Strong: '#f00',
        Generic.Traceback: '#f00',
        Keyword.Type: '#700',
    }
