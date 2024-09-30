
from pygments.style import Style
from pygments.token import *

class R2OgrayStyle(Style):
    name = 'r2ogray'
    background_color = "#f72"
    highlight_color = "#111"
    styles = {
        Name.Function: '#f72',
        Keyword: '#f72',
        Comment: '#f72',
        Comment.Special: '#000',
        Name.Variable: '#f72',
        Name.Constant: '#f72',
        Generic.Emph: '#f72',
        Name.Label: '#555',
        Number: '#f72',
        Text: '#999',
        Generic.Prompt: '#f72',
        Generic.Inserted: '#f72',
        Generic.Deleted: '#777',
        Generic: '#fff',
        Generic.Strong: '#f72',
        Generic.Traceback: '#f00',
        Keyword.Type: '#777',
    }
