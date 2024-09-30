
from pygments.style import Style
from pygments.token import *

class R2White2Style(Style):
    name = 'r2white2'
    background_color = "#2f6f9f"
    highlight_color = "#42505e"
    styles = {
        Name.Function: '#8D0004',
        Keyword: '#376B4C',
        Comment: '#001296',
        Name.Variable: '#400080',
        Name.Constant: '#912D3A',
        Generic.Emph: '#2F6F9F',
        Generic: '#007D96',
        Generic.Strong: '#fff',
        Generic.Deleted: '#990000',
        Generic.Inserted: '#376B4C',
        Name.Label: '#2F6F9F',
        Number: '#761B48',
        Text: '#4D4D4D',
        Generic.Prompt: '#2F6F9F',
        Comment.Special: '#007D96',
        Keyword.Type: '#305F65',
    }
