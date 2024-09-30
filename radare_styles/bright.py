
from pygments.style import Style
from pygments.token import *

class R2BrightStyle(Style):
    name = 'r2bright'
    background_color = "#303030"
    highlight_color = "#000080"
    styles = {
        Name.Function: '#ff0000',
        Keyword: '#00ff00',
        Comment: '#ff0000',
        Comment.Special: '#ffffff',
        Name.Variable: '#ffffff',
        Name.Constant: '#00ffff',
        Generic.Emph: '#00ff00',
        Name.Label: '#00ff00',
        Number: '#ffff00',
        Text: '#ffffff',
        Generic.Prompt: '#ffff00',
        Keyword.Type: '#ffff00',
        Generic: '#0000ff',
        Generic.Inserted: '#00ff00',
        Generic.Deleted: '#ff0000',
        Generic.Traceback: '#ffff00',
        Generic.Strong: '#0000ff',
    }
