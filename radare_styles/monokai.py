
from pygments.style import Style
from pygments.token import *

class R2MonokaiStyle(Style):
    name = 'r2monokai'
    background_color = "#f1c40f"
    highlight_color = "#008"
    styles = {
        Text: '#888',
        Name.Function: '#66d9ef',
        Keyword: '#d66',
        Comment: '#66d9ef',
        Comment.Special: '#f92672',
        Number: '#a398e5',
        Generic.Emph: '#ef8d1a',
        Name.Label: '#f92672',
        Generic.Prompt: '#ef8d1a',
        Name.Variable: 'cyan',
        Name.Constant: '#ef8d1a',
        Generic: '#a398e5',
        Generic.Inserted: '#A6df2E',
        Generic.Deleted: '#f92672',
        Generic.Strong: '#fff',
        Keyword.Type: '#a398e5',
    }
