
from pygments.style import Style
from pygments.token import *

class R2SolarizedStyle(Style):
    name = 'r2solarized'
    background_color = "#bb5"
    highlight_color = "#004"
    styles = {
        Name.Function: '#d33',
        Keyword: '#f00',
        Comment: '#28d',
        Comment.Special: '#890',
        Generic.Emph: '#e37',
        Name.Label: '#9aa',
        Number: '#eee',
        Text: '#577',
        Generic.Prompt: '#c41',
        Name.Variable: '#28d',
        Name.Constant: '#c41',
        Generic: '#899',
        Generic.Inserted: '#890',
        Generic.Deleted: '#c41',
        Generic.Strong: '#f00',
        Generic.Traceback: 'red',
        Keyword.Type: '#cc8',
    }
