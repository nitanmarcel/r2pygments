
from pygments.style import Style
from pygments.token import *

class R2ConsonanceStyle(Style):
    name = 'r2consonance'
    background_color = "#4cf"
    highlight_color = "#004"
    styles = {
        Name.Function: '#ee0',
        Keyword: '#f2a',
        Comment: '#fcc',
        Comment.Special: '#f2a',
        Generic.Emph: '#ee0',
        Name.Label: '#888',
        Number: '#fff',
        Text: '#577',
        Generic.Prompt: '#4cf',
        Name.Variable: '#fcc',
        Name.Constant: '#4cf',
        Generic: '#4cf',
        Generic.Inserted: '#4f2',
        Generic.Deleted: '#d41',
        Generic.Strong: '#af2',
        Generic.Traceback: '#090',
        Keyword.Type: '#f2a',
    }
