class CustomException(Exception):
    def __init__(self, message,error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"[Error {self.error_code}]: {self.args[0]}"

try:
    raise CustomException("Something went wrong!", 404)
except CustomException as e:
    print(e)
