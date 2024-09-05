#自定义异常：
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def do_something(value):
    if value < 0:
        raise MyCustomError("Value must be non-negative")

try:
    do_something(-1)
except MyCustomError as e:
    print(f"MyCustomError: {e.message}")