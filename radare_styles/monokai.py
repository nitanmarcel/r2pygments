
from pygments.style import Style
from pygments.token import *

class R2MonokaiStyle(Style):
    name = 'r2monokai'
    background_color = "#f1c40f"
    styles = {
        Name.Function: '#f1c40f',
        Keyword: '#A6df2E',
        Keyword: '#A6df2E',
        Keyword: '#A6df2E',
        Comment: '#66d9ef',
        Number: '#a398e5',
        Generic.Emph: '#A6df2E',
        Name.Function: '#66d9ef',
        Name.Label: '#66d9ef',
        Name.Label: '#f92672',
        Generic.Prompt: '#ef8d1a',
        Name.Variable: '#fff',
        Generic.Emph: '#ef8d1a',
        Name.Constant: '#ef8d1a',
        Name.Variable: 'cyan',
        Keyword.Type: '#a398e5',
        Name.Variable: 'cyan',
    }
