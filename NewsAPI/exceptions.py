###################################################################
#
# Common Exceptions
#
###################################################################

class FreeLimitExceededError(Exception):
    """Raised whenever the counter exceeds 100 API calls a day.
    
    Attributes:
        counter: The current number of API calls.
        message: The message when an exception is raised.
    """

    def __init__(self, counter: int, message = "Free API Calls Exceeded.") -> None:
        """Initialize the FreeLimitExceededError Exception class."""

        self.counter = counter
        self.message = message
        super().__init__(self.message)