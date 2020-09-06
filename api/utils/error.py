class AppError(Exception):
    def __init__(self, err_msg, err_code, status, context=None, reason=None):
        self.err_msg = err_msg
        self.err_code = err_code
        self.status = status
        self.context = context
        self.reason = reason

    def __str__(self):
        return f'{self.err_code} | {self.err_msg}'
