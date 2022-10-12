from pydash.strings import snake_case, pascal_case


def get_snake_and_camel_case(s: str):
    return snake_case(s), pascal_case(s, strict=False)
