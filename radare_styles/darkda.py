
from pygments.style import Style
from pygments.token import *

class R2DarkdaStyle(Style):
    name = 'r2darkda'
    background_color = "#099"
    highlight_color = "#00007f"
    styles = {
        Text: '#ff7f00',
        Name.Function: '#00ffff',
        Keyword: '#df077e',
        Comment: '#82607e',
        Comment.Special: '#f3c5ff',
        Number: '#d25032',
        Generic.Emph: '#009d9d',
        Name.Label: '#ababab',
        Generic.Prompt: '#fc0',
        Name.Variable: '#99a',
        Name.Constant: '#00b1ab',
        Generic: '#0043cb',
        Generic.Inserted: '#009100',
        Generic.Deleted: '#bc0000',
        Generic.Strong: '#fff',
        Keyword.Type: '#df077e',
    }
