
from pygments.style import Style
from pygments.token import *

class R2GruvboxStyle(Style):
    name = 'r2gruvbox'
    background_color = "#7c6f64"
    highlight_color = "#3c3836"
    styles = {
        Comment: '#928374',
        Name.Variable: '#83a598',
        Name.Constant: '#8ec07c',
        Generic.Emph: '#b8bb26',
        Name.Function: '#fb4934',
        Generic.Traceback: '#b8bb26',
        Generic: '#83a598',
        Generic.Strong: '#ebdbb2',
        Generic.Deleted: '#fb4934',
        Generic.Inserted: '#b8bb26',
        Keyword: '#b8bb26',
        Name.Label: '#d65d0e',
        Number: '#d3869b',
        Text: '#7c6f64',
        Generic.Prompt: '#8ec07c',
        Comment.Special: '#fe8019',
        Keyword.Type: '#fabd2f',
    }
