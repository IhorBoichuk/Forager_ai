class PyhunterError(Exception):
    """
    Generic exception class for the library
    """
    pass


class HunterApiError(PyhunterError):
    """
    Represents something went wrong in the call to the Hunter API
    """
    pass