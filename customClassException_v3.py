class InvalidAgeError(Exception):
    def __init__(self, message, age):
        super().__init__(message)
        self.age = age

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.", age)  # Raise with additional info
    return age

try:
    check_age(21)
except InvalidAgeError as e:
    print(f"{e} (Entered Age: {e.age})")  # Output: Age must be at least 18. (Entered Age: 16)
