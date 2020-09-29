""" Module for common helpers """


def request_data_strip(request_data):
    """
    Removes spaces at the beginning and at the end of request data values
    Args:
        request_data(dict): request body
    Returns:
        request_data(dict): request body with removed spaces
    """

    for key, value in request_data.items():
        if isinstance(value, str):
            request_data[key] = value.strip()

    return request_data
