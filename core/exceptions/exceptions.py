from fastapi import HTTPException, status

from core.log import get_logger

logger = get_logger(__name__)


class CustomHTTPException(HTTPException):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "Internal Server Error"
    error_code: str = "INTERNAL_SERVER_ERROR"

    def __init__(
        self,
        detail: str | None = None,
        status_code: int | None = None,
        error_code: str | None = None,
    ):
        final_detail = detail or self.detail
        final_status = status_code or self.status_code
        final_error_code = error_code or self.error_code

        super().__init__(
            status_code=final_status,
            detail={"message": final_detail, "error_code": final_error_code},
        )


class NotFoundHTTPException(CustomHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Запись не найдена"
    error_code = "NOT_FOUND"


class UserNotFoundHTTPException(NotFoundHTTPException):
    detail = "Пользователь не найден"
    error_code = "USER_NOT_FOUND"
