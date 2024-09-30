
from pygments.style import Style
from pygments.token import *

class R2GreepyStyle(Style):
    name = 'r2greepy'
    background_color = "#f0f"
    styles = {
        Name.Function: '#f0f',
        Keyword: '#f0f',
        Comment: '#0f0',
        Name.Variable: '#fff',
        Name.Constant: '#f0f',
        Generic.Emph: '#f0f',
        Name.Function: '#f0f',
        Generic.Emph: '#f0f',
        Keyword: '#f0f',
        Name.Label: '#f0f',
        Number: '#0f0',
        Name.Label: '#0f0',
        Generic.Prompt: '#f0f',
        Keyword: '#f0f',
        Name.Variable: '#f0f',
        Keyword.Type: '#fff',
        Name.Variable: '#f0f',
    }
