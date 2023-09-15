import pathlib

import jinja2
import yaml

__here__ = pathlib.Path(__file__).parent
template_dir = __here__ / ".." / "templates"
cv_data_path = __here__ / ".." / "cv.yml"
cv_output_path = __here__ / ".." / "cv.html"

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader([template_dir]),
    extensions=["pypugjs.ext.jinja.PyPugJSExtension"],
)


def format_date(date_or_string):
    if isinstance(date_or_string, str):
        return date_or_string
    else:
        return date_or_string.strftime('%B %Y')


def render(data):
    template = jinja_env.get_template("template.pug")
    content = template.render(format_date=format_date, **data)
    return content


def get_data(filepath):
    with filepath.open() as f:
        data = yaml.safe_load(f)
    return data


def write_content(output_file, content):
    with output_file.open("w") as f:
        f.write(content)


def main():
    data = get_data(cv_data_path)
    content = render(data)
    write_content(cv_output_path, content)


if __name__ == "__main__":
    main()
