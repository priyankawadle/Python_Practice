class DinnerBillError(Exception):
    pass
class PriceNotInteger(DinnerBillError):
    def __init__(self, name ,price):
        message = "Error for "+ str(name) + "where Price: " + str(price )+ " which must be proper interger "
        super().__init__(message)

class PriceNegativeOrZeroError(DinnerBillError):
     def __init__(self, name ,price):
        message = "Error for "+ str(name) + "where Price: " + str(price) + " which must be greater than zero "
        super().__init__(message)

class FileMissingError(DinnerBillError):
    def __init__(self, filename):
        message = "File  "+ str(filename) + "is missing."
        super().__init__(message)

class MalFormedEntryError(DinnerBillError):
    def __init__(self, entry):
        message = "Malformed entry:  "+ str(entry)
        super().__init__(message)

