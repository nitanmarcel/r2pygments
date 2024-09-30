import re
import os
import argparse

from typing import Dict, Tuple, Any
from pygments.style import Style
from pygments.token import Comment, String, Number, Name, Keyword, Generic, Text

class R2Style(Style):
    name = "r2style"
    background_color = "#000"
    styles = {
        Name.Function: "#000",
        Keyword: "#000",
        Keyword: "#000",
        Keyword: "#000",
        Comment: "#000",
        Generic.Emph: "white",
        Name.Function: "#000",
        Name.Label: "#000",
        Number: "#000",
        Name.Label: "#000",
        Generic.Prompt: "#000",
        Name.Variable: "#000",
        Generic.Emph: "#000",
        Name.Constant: "#000",
        Name.Variable: "#000",
        Keyword.Type: "#000",
        Name.Variable: "#000",
    }

token_map = {
    "comment": (Comment, "Comment"),
    "num": (Number, "Number"),
    "offset": (Name.Label, "Name.Label"),
    "call": (Name.Function, "Name.Function"),
    "jmp": (Keyword, "Keyword"),
    "cjmp": (Keyword, "Keyword"),
    "ujmp": (Keyword, "Keyword"),
    "reg": (Name.Variable, "Name.Variable"),
    "var": (Name.Variable, "Name.Variable"),
    "var.type": (Keyword.Type, "Keyword.Type"),
    "var.name": (Name.Variable, "Name.Variable"),
    "fname": (Name.Function, "Name.Function"),
    "flag": (Name.Constant, "Name.Constant"),
    "label": (Name.Label, "Name.Label"),
    "help": (Generic.Emph, "Generic.Emph"),
    "prompt": (Generic.Prompt, "Generic.Prompt"),
    "flow": (Generic.Emph, "Generic.Emph"),
    "error": (Generic.Error, "Generic.Error"),
    "other": (Text, "Text"),
    "push": (Keyword, "Keyword"),
    "pop": (Keyword, "Keyword"),
    "cmp": (Keyword, "Keyword"),
    "ret": (Keyword, "Keyword"),
    "trap": (Keyword, "Keyword"),
    "swi": (Keyword, "Keyword"),
    "creg": (Name.Variable, "Name.Variable"),
    "usrcmt": (Comment.Special, "Comment.Special"),
    "graph.true": (Generic.Inserted, "Generic.Inserted"),
    "graph.false": (Generic.Deleted, "Generic.Deleted"),
    "graph.trufae": (Generic, "Generic"),
    "graph.current": (Generic.Strong, "Generic.Strong"),
    "graph.traced": (Generic.Traceback, "Generic.Traceback"),
    "graph.box": (Generic, "Generic"),
}


def key_to_token(key) -> Tuple[str, Any]:
    return token_map.get(key)

def parse_color(color: str) -> str:
    if color.startswith("rgb:"):
        return f"#{color[4:]}"
    return color

def parse_syntax(syntax) -> Dict[str, str]:
    styles = {}
    for line in syntax.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        match = re.match(r"ec\s+(\S+)\s+(.+)", line)
        if match:
            key, value = match.groups()
            color = parse_color(value.split()[0])
            styles[key] = color
    
    return styles

def generate_pygments_style_dict(r2style: str, name: str) -> Dict[Any, str]:
    styles = parse_syntax(r2style)
    _dict = {"background_color": styles.get("widget.bg", "#000"),
             "highlight_color": styles.get("linehl", "#000000"),
             "name": f"r2{name}"}
    for k,v in styles.items():
        token = key_to_token(k)
        if token:
            _dict[token[0]] = v
    return _dict

def generate_pygments_style(r2style: str, name: str) -> Style:
    _dict = generate_pygments_style_dict(r2style, name)
    cls = type(f"R2{name.capitalize()}Style", (Style,), {
        "name": _dict["name"],
        "background_color": _dict["background_color"],
        "highlight_color": _dict["highlight_color"],
        "styles": {k: v for k, v in _dict.items() if k not in ["name", "background_color", "highlight_color"]}
    })
    return cls

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path", help="File or directory with radare2 scheme schema to parse")
    argparser.add_argument("output", help="File or directory to output the parsed style")
    
    args = argparser.parse_args()
    
    is_in_dir = os.path.isdir(args.path)
    is_out_dir = os.path.isdir(args.output)
    
    if is_in_dir:
        instyles = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]
        inpaths = [os.path.join(args.path, f) for f in instyles]
    else:
        instyles = [os.path.basename(args.path)]
        inpaths = [args.path]
    
    if is_out_dir:
        outstyles = [os.path.join(args.output, f"{os.path.splitext(f)[0]}.py") for f in instyles]
    else:
        outstyles = [args.output]
    
    for inpath, outfile in zip(inpaths, outstyles):
        with open(inpath, "r") as f:
            r2style = f.read()
        
        name = os.path.splitext(os.path.basename(inpath))[0]
        style_dict = generate_pygments_style_dict(r2style, name)
        
        style_definitions = []
        for k, v in style_dict.items():
            if k not in ["name", "background_color"]:
                token_str = None
                for t, (token, token_name) in token_map.items():
                    if k == token:
                        token_str = token_name
                        break
                if token_str:
                    style_definitions.append(f"        {token_str}: '{v}',")
        
        style_template = """
from pygments.style import Style
from pygments.token import *

class R2{name_title}Style(Style):
    name = '{name}'
    background_color = "{background_color}"
    highlight_color = "{highlight_color}"
    styles = {{
{style_definitions}
    }}
"""
        
        with open(outfile, "w") as out:
            out.write(style_template.format(
                name_title=name.capitalize(),
                name=style_dict["name"],
                background_color=style_dict["background_color"],
                highlight_color=style_dict["highlight_color"],
                style_definitions="\n".join(style_definitions)
            ))
        
        print(f"Generated {outfile}")