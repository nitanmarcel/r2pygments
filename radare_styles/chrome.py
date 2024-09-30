
from pygments.style import Style
from pygments.token import *

class R2ChromeStyle(Style):
    name = 'r2chrome'
    background_color = "#fff"
    highlight_color = "#111"
    styles = {
        Name.Function: '#fff',
        Keyword: '#fff',
        Comment: 'white',
        Comment.Special: '#333',
        Name.Variable: '#fff',
        Name.Constant: '#fff',
        Generic.Emph: '#fff',
        Name.Label: '#555',
        Number: '#fff',
        Text: '#999',
        Generic.Prompt: '#fff',
        Generic.Inserted: '#fff',
        Generic.Deleted: '#777',
        Generic: '#fff',
        Generic.Strong: '#fff',
        Generic.Traceback: '#f00',
        Keyword.Type: '#777',
    }
