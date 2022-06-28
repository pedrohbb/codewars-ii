from .base_error import BaseError


class DuplicatedEntryError(BaseError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)