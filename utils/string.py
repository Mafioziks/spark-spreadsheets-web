def snake_case_to_camel_case(string):
    """Transforms snake case to camel case"""
    parts = string.split("_")
    return parts[0] + ''.join(part.title() for part in parts[1:])
