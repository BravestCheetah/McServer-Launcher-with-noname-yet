class RequestJsonFailedError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


class LoadDownloadsDataError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
