

class Step:

    def __init__(self, raw_data: dict) -> None:
        self.time: int = raw_data["TIME"]
        self.time_type: str = raw_data["TIME_TYPE"]
        self.ingredients: str = raw_data["INGREDIENTS"]
        self.instruction: str = raw_data["INSTRUCTION"]
