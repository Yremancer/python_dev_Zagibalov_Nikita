from pydantic import BaseModel

from core.exceptions import CustomHTTPException, UserNotFoundHTTPException


class CustomResponse(BaseModel):
    status_code: int
    description: str
    content: dict[str, dict[str, dict[str, str]]] | None = None

    @classmethod
    def create_response(
        cls,
        status_code: int,
        detail: str | None = None,
        error_code: str | None = None,
    ) -> dict:
        response: dict = {status_code: {}}

        if detail and error_code:
            response[status_code]["content"] = {
                "application/json": {
                    "example": {
                        "detail": {"message": detail, "error_code": error_code}
                    }
                }
            }
        return response

    @classmethod
    def from_exception(cls, exc: type[CustomHTTPException]) -> dict:
        return cls.create_response(
            status_code=exc.status_code,
            detail=exc.detail,
            error_code=exc.error_code or None,
        )


responses = {
    "404_user_not_found": CustomResponse.from_exception(
        UserNotFoundHTTPException
    ),
    "500_internal_error": CustomResponse.from_exception(CustomHTTPException),
}
