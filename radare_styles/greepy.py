
from pygments.style import Style
from pygments.token import *

class R2GreepyStyle(Style):
    name = 'r2greepy'
    background_color = "#f0f"
    highlight_color = "#111"
    styles = {
        Name.Function: '#f0f',
        Keyword: '#f0f',
        Comment: '#0f0',
        Comment.Special: '#0f0',
        Name.Variable: '#f0f',
        Name.Constant: '#f0f',
        Generic.Emph: '#f0f',
        Name.Label: '#0f0',
        Number: '#0f0',
        Text: '#999',
        Generic.Prompt: '#f0f',
        Generic.Inserted: '#f0f',
        Generic.Deleted: '#fff',
        Generic: '#fff',
        Generic.Strong: '#f0f',
        Generic.Traceback: '#f00',
        Keyword.Type: '#fff',
    }
