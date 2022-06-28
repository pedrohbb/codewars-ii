from lib2to3.pytree import Base
from .base_error import BaseError


class NotFoundError(BaseError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)