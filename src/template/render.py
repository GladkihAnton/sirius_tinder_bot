from jinja2 import Environment, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath='src/template/templates'),
    autoescape=select_autoescape()
)


def render(template_name: str, *args, **kwargs) -> str:
    template = env.get_template(template_name)
    return template.render(*args, **kwargs)
