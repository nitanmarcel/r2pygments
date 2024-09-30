
from pygments.style import Style
from pygments.token import *

class R2White2Style(Style):
    name = 'r2white2'
    background_color = "#2f6f9f"
    styles = {
        Name.Function: '#A63A00',
        Keyword: '#376B4C',
        Comment: '#001296',
        Name.Constant: '#912D3A',
        Generic.Emph: '#376B4C',
        Name.Function: '#8D0004',
        Generic.Emph: '#2F6F9F',
        Keyword: '#376B4C',
        Name.Label: '#66d9ef',
        Number: '#761B48',
        Name.Label: '#2F6F9F',
        Generic.Prompt: '#2F6F9F',
        Name.Variable: '#400080',
        Keyword: '#376B4C',
        Name.Variable: '#400080',
        Keyword.Type: '#305F65',
        Name.Variable: '#400080',
    }
