
from pygments.style import Style
from pygments.token import *

class R2GentooStyle(Style):
    name = 'r2gentoo'
    background_color = "cyan"
    highlight_color = "#101010"
    styles = {
        Comment: 'cyan',
        Comment.Special: 'cyan',
        Name.Function: 'green',
        Name.Constant: 'green',
        Name.Label: 'yellow',
        Generic.Emph: 'cyan',
        Generic.Prompt: 'green',
        Text: '#c0c0c0',
        Keyword: 'cyan',
        Name.Variable: 'white',
        Number: 'yellow',
        Keyword.Type: 'yellow',
        Generic: '#3030f0',
        Generic.Inserted: '#30f030',
        Generic.Deleted: '#f03030',
        Generic.Strong: '#f03030',
        Generic.Traceback: '#f00000',
    }
