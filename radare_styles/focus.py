
from pygments.style import Style
from pygments.token import *

class R2FocusStyle(Style):
    name = 'r2focus'
    background_color = "#ff0"
    highlight_color = "#222"
    styles = {
        Name.Function: '#ff0',
        Name.Label: '#fff',
        Keyword: '#000',
        Generic.Prompt: 'byellow',
        Comment: '#0cf',
        Comment.Special: '#ff0',
        Text: '#666',
        Number: '#ff0',
        Name.Variable: 'cyan',
        Generic.Emph: '#ff3',
        Generic: 'blue',
        Generic.Inserted: 'green',
        Generic.Deleted: 'red',
        Generic.Strong: 'blue',
        Generic.Traceback: 'red',
        Keyword.Type: '#f3f',
    }
