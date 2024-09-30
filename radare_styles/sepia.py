
from pygments.style import Style
from pygments.token import *

class R2SepiaStyle(Style):
    name = 'r2sepia'
    background_color = "#db7"
    highlight_color = "#210"
    styles = {
        Text: '#ba6',
        Name.Function: '#bb7',
        Keyword: '#bb7',
        Comment: '#fd9',
        Comment.Special: '#fff',
        Generic.Emph: '#ab7',
        Name.Label: '#960',
        Number: '#960',
        Generic.Prompt: '#960',
        Name.Variable: '#fd9',
        Name.Constant: '#ffd',
        Generic.Inserted: '#fd9',
        Generic.Deleted: '#431',
        Generic: '#431',
        Generic.Strong: '#0000ff',
        Generic.Traceback: '#0000ff',
        Keyword.Type: '#850',
    }
