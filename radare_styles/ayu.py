
from pygments.style import Style
from pygments.token import *

class R2AyuStyle(Style):
    name = 'r2ayu'
    background_color = "#888"
    highlight_color = "#42505e"
    styles = {
        Comment: '#cd4',
        Name.Variable: '#95e6cb',
        Name.Constant: '#5de',
        Generic.Emph: '#c2d94c',
        Name.Function: '#f73',
        Generic.Traceback: '#2eb',
        Generic: '#55b4d4',
        Generic.Strong: '#fff',
        Generic.Deleted: '#f07178',
        Generic.Inserted: '#bae67e',
        Keyword: '#c2d94c',
        Name.Label: '#d74',
        Number: '#f85',
        Text: '#888',
        Generic.Prompt: '#5de',
        Comment.Special: '#fa6e32',
        Keyword.Type: '#ffd580',
    }
