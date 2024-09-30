
from pygments.style import Style
from pygments.token import *

class R2SmyckStyle(Style):
    name = 'r2smyck'
    background_color = "#bb5"
    highlight_color = "#004"
    styles = {
        Text: '#888',
        Name.Function: '#9df',
        Keyword: '#d66',
        Comment: '#9df',
        Comment.Special: '#9f4',
        Number: '#bb5',
        Generic.Emph: '#fd6',
        Name.Label: '#bb5',
        Generic.Prompt: '#bb5',
        Name.Variable: '#9df',
        Name.Constant: '#9df',
        Generic: '#9c4',
        Generic.Inserted: '#9c4',
        Generic.Deleted: '#d66',
        Generic.Strong: '#fff',
        Keyword.Type: '#fd6',
    }
