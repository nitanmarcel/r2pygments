
from pygments.style import Style
from pygments.token import *

class R2IaitoStyle(Style):
    name = 'r2iaito'
    background_color = "#4cf"
    styles = {
        Comment: '#8e8c8b',
        Name.Function: '#0693c9',
        Name.Constant: '#0a8ab0',
        Name.Label: '#0068bd',
        Generic.Emph: '#005f87',
        Generic.Emph: '#5f8700',
        Generic.Prompt: '#30a000',
        Name.Label: '#8e8c8b',
        Keyword: '#5f8700',
        Keyword: '#5f8700',
        Keyword: '#5f8700',
        Name.Function: '#0693c9',
        Name.Variable: '#005f87',
        Number: '#ef5919',
        Name.Variable: '#d03080',
        Keyword.Type: '#876ac1',
        Name.Variable: '#d03080',
    }
