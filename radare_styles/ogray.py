
from pygments.style import Style
from pygments.token import *

class R2OgrayStyle(Style):
    name = 'r2ogray'
    background_color = "#f72"
    styles = {
        Name.Function: '#f72',
        Keyword: '#f72',
        Comment: '#f72',
        Name.Variable: '#fff',
        Name.Constant: '#f72',
        Generic.Emph: '#f72',
        Name.Function: '#f72',
        Generic.Emph: '#f72',
        Keyword: '#f72',
        Name.Label: '#f72',
        Number: '#f72',
        Name.Label: '#555',
        Generic.Prompt: '#f72',
        Keyword: '#f72',
        Name.Variable: '#f72',
        Keyword.Type: '#777',
        Name.Variable: '#f72',
    }
