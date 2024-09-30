
from pygments.style import Style
from pygments.token import *

class R2GbStyle(Style):
    name = 'r2gb'
    background_color = "#86c06c"
    highlight_color = "#306850"
    styles = {
        Comment: '#86c06c',
        Comment.Special: '#86c06c',
        Name.Function: '#e0f8cf',
        Name.Constant: '#e0f8cf',
        Name.Label: '#306850',
        Generic.Emph: '#e0f8cf',
        Generic.Prompt: '#e0f8cf',
        Text: '#306850',
        Keyword: '#86c06c',
        Name.Variable: '#86c06c',
        Number: '#e0f8cf',
        Generic: '#86c06c',
        Generic.Inserted: '#86c06c',
        Generic.Deleted: '#e0f8cf',
        Generic.Strong: '#e0f8cf',
        Generic.Traceback: '#86c06c',
        Keyword.Type: '#86c06c',
    }
