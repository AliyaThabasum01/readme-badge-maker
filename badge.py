from urllib.parse import quote


def make_badge(label, message):
    label = quote(label.replace("-", "--"))
    message = quote(message.replace("-", "--"))

    return f"![{label}](https://img.shields.io/badge/{label}-{message}-blue)"
