from typing import ParamSpec

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader(searchpath='src/template/templates'), autoescape=select_autoescape())

P = ParamSpec('P')


def render(template_name: str, *args: P.args, **kwargs: P.kwargs) -> str:
    template = env.get_template(template_name)
    return template.render(*args, **kwargs)
