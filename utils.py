def str_to_bool(val):
    """Convert a string representation of truth to True or False:

    Args:
        val (String):
        True values are 'y','yes' or ''; case-insensitive
        False values are 'n'or'no'; case-insensitive
        Raises ValueError if 'val' is anything else
    """
    true_values = ['yes', 'y', '']
    false_values = ['no', 'n']
    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_values:
        return True
    elif val in false_values:
        return False
    else:
        raise ValueError(f"Invalid input value {val}")
