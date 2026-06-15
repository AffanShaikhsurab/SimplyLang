class StopSignal(BaseException):
    """Control signal for `stop` that halts the program without killing tests."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)
        self.message = message
