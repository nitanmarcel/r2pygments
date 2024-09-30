
from pygments.style import Style
from pygments.token import *

class R2RastaStyle(Style):
    name = 'r2rasta'
    background_color = "yellow"
    highlight_color = "#008"
    styles = {
        Comment: 'green',
        Comment.Special: 'yellow',
        Name.Function: 'red',
        Name.Constant: 'yellow',
        Name.Label: 'yellow',
        Generic.Emph: 'yellow',
        Generic.Prompt: 'green',
        Text: 'green',
        Keyword: 'yellow',
        Name.Variable: 'green',
        Number: 'red',
        Generic: 'green',
        Generic.Inserted: 'green',
        Generic.Deleted: 'red',
        Generic.Strong: 'green',
        Generic.Traceback: 'yellow',
        Keyword.Type: 'red',
    }
