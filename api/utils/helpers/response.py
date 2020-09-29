""" Module for endpoints responses """


class Response:
    """ Response class """

    @classmethod
    def success(cls, message, data, code):
        """ success response
            Args:
                message (string): response message property
                data (dict): response data property
                code (dict): response status code
            Returns:
                (dict): dictionary with status, message and data properties
        """
        return {
            'status': 'success',
            'message': message,
            'data': data
        }, code

    @classmethod
    def error(cls, error, code):
        """ error response
            Args:
                error (str): response error message
                code (dict): response status code
            Returns:
                (dict): dictionary with status and error properties
        """
        return {
            'status': 'error',
            'error': error
        }, code
