from .string import snake_case_to_camel_case


def dict_for_api(data: dict):
    return {snake_case_to_camel_case(key): value for key, value in data.items()}
