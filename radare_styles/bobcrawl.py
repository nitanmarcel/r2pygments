
from pygments.style import Style
from pygments.token import *

class R2BobcrawlStyle(Style):
    name = 'r2bobcrawl'
    background_color = "#099"
    highlight_color = "#00003f"
    styles = {
        Name.Function: '#fad200',
        Comment: '#32302f',
        Comment.Special: '#ffc5f3',
        Keyword: '#d75f00',
        Name.Constant: '#d75f00',
        Name.Label: '#afafaf',
        Generic.Emph: '#ff5f87',
        Generic.Prompt: '#d75f00',
        Text: '#5f8787',
        Name.Variable: '#64604f',
        Number: '#d25032',
        Generic: '#005fff',
        Generic.Strong: '#c68e00',
        Generic.Inserted: '#009100',
        Generic.Deleted: '#bc0000',
        Generic.Traceback: '#ffff00',
        Keyword.Type: '#00afd7',
    }
