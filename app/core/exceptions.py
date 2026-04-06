class AppBaseException(Exception):
    """
    This is the base class for all our application errors.
    If you throw this (or any subclass), the user will see a nice JSON response.
    """

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundException(AppBaseException):
    """Use this when something (like a User or Product) isn't in the database."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class UnauthorizedException(AppBaseException):
    """Use this when login fails or a token is invalid."""

    def __init__(self, message: str = "Unauthorized access"):
        super().__init__(message, status_code=401)


class BadRequestException(AppBaseException):
    """Use this for invalid input, like a bad ID format or missing fields."""

    def __init__(self, message: str = "Bad request"):
        super().__init__(message, status_code=400)


class ForbiddenException(AppBaseException):
    """Use this when a user is logged in but doesn't have permission (e.g., not an Admin)."""

    def __init__(self, message: str = "Forbidden access"):
        super().__init__(message, status_code=403)
