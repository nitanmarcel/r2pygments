
from pygments.style import Style
from pygments.token import *

class R2GruvboxStyle(Style):
    name = 'r2gruvbox'
    background_color = "#7c6f64"
    styles = {
        Comment: '#928374',
        Name.Constant: '#8ec07c',
        Generic.Emph: '#928374',
        Name.Function: '#8ec07c',
        Generic.Emph: '#b8bb26',
        Keyword: '#b8bb26',
        Name.Label: '#8ec07c',
        Number: '#d3869b',
        Name.Label: '#d65d0e',
        Generic.Prompt: '#8ec07c',
        Name.Function: '#fb4934',
        Name.Variable: '#fabd2f',
        Keyword: '#b8bb26',
        Keyword: '#b8bb26',
        Name.Variable: '#83a598',
        Keyword.Type: '#fabd2f',
        Name.Variable: '#83a598',
    }
