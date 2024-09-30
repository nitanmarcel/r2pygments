
from pygments.style import Style
from pygments.token import *

class R2ChromeStyle(Style):
    name = 'r2chrome'
    background_color = "#fff"
    styles = {
        Name.Function: 'white',
        Keyword: 'white',
        Comment: 'white',
        Name.Variable: '#fff',
        Name.Constant: '#fff',
        Generic.Emph: '#fff',
        Name.Function: '#fff',
        Generic.Emph: '#fff',
        Keyword: '#fff',
        Name.Label: '#fff',
        Number: '#fff',
        Name.Label: '#555',
        Generic.Prompt: '#fff',
        Keyword: '#fff',
        Name.Variable: '#fff',
        Keyword.Type: '#777',
        Name.Variable: '#fff',
    }
