from typing import Union


class Ingredient:

    def __init__(self, raw_data: dict) -> None:
        self.name: str = raw_data["NAME"]
        self.amount: Union[float, int] = raw_data["AMOUNT"]
        self.measurement_type: str = raw_data["MEASUREMENT_TYPE"]
