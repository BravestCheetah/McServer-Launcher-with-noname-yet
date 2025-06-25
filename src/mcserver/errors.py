class RequestJsonFailedError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


class LoadDownloadsDataError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


class UnknownSoftwareError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


class UnknownVersionError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


class ServerAlreadyExistsError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


class ServerDeleteNoConfirm(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

class ServerDoesNotExistError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
