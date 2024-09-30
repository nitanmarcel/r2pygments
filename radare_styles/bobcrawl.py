
from pygments.style import Style
from pygments.token import *

class R2BobcrawlStyle(Style):
    name = 'r2bobcrawl'
    background_color = "#099"
    styles = {
        Name.Function: '#ffff00',
        Comment: '#32302f',
        Name.Function: '#fad200',
        Name.Constant: '#d75f00',
        Name.Label: '#8787d7',
        Generic.Emph: '#ff5f87',
        Generic.Prompt: '#d75f00',
        Name.Label: '#afafaf',
        Keyword: '#ff5f87',
        Keyword: '#afaf00',
        Keyword: '#ff5f87',
        Name.Variable: '#73adad',
        Number: '#d25032',
        Name.Variable: '#64604f',
        Keyword.Type: '#00afd7',
        Name.Variable: '#64604f',
    }
