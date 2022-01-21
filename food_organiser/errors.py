

class BoardNotFoundError(Exception):
    """
    This class is responsible for throwing an error when the board is not present.
    """

    def __init__(self, message: str) -> None:
        """
        The constructor for the BoardNotFoundError class.

        :param message: (str) the message that will be logged for the error
        """
        super().__init__(message)


class ListNotFoundError(Exception):
    """
    This class is responsible for throwing an error when the list is not present on a board.
    """

    def __init__(self, message: str) -> None:
        """
        The constructor for the ListNotFoundError class.

        :param message: (str) the message that will be logged for the error
        """
        super().__init__(message)
