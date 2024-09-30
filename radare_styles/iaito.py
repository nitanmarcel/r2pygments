
from pygments.style import Style
from pygments.token import *

class R2IaitoStyle(Style):
    name = 'r2iaito'
    background_color = "#4cf"
    highlight_color = "#efefef"
    styles = {
        Comment: '#8e8c8b',
        Comment.Special: '#8e8c8b',
        Name.Function: '#0693c9',
        Name.Constant: '#0a8ab0',
        Name.Label: '#8e8c8b',
        Generic.Emph: '#5f8700',
        Generic.Prompt: '#30a000',
        Text: '#005f87',
        Keyword: '#da3192',
        Name.Variable: '#d03080',
        Number: '#ef5919',
        Keyword.Type: '#876ac1',
        Generic: '#005f87',
        Generic.Inserted: '#5f8700',
        Generic.Deleted: '#e03030',
        Generic.Strong: '#00f0f0',
        Generic.Traceback: '#e03030',
    }
