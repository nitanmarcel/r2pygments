import importlib
import glob
from os.path import basename, dirname, isfile, join

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]


def get_style(name: str):
    split = name.splitlines()
    if len(split) > 1:
        for line in split:
            if line.startswith("-"):
                name = line.split(None, 1)[-1].strip()
    module = importlib.import_module(f".{name}", package=__name__)
    return getattr(module, f"R2{name.title()}Style")
