from .base_exception import BaseException


class NotFoundException(BaseException):
    def __init__(self, message: str, id_name: str, id: int = None):
        super().__init__(
            status_code=404,
            message=message,
            code="NOT_FOUND",
            details={id_name: id}
        )

class InternalServerError(BaseException):
    def __init__(self, error: Exception):
        super().__init__(
            status_code=500,
            message="내부 서버 오류가 발생했습니다.",
            code="INTERNAL_SERVER_ERROR",
            details={"error": str(error)}
        )

class ForbiddenException(BaseException):
    def __init__(self, message: str):
        super().__init__(
            status_code=403,
            message=message,
            code="FORBIDDEN",
            details={}
        )