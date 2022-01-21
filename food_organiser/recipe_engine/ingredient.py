from typing import Union


class Ingredient:

    def __init__(self, raw_data: dict) -> None:
        self.name: str = raw_data["NAME"]
        self.amount: Union[float, int] = raw_data["AMOUNT"]
        self.measurement_type: str = raw_data["MEASUREMENT_TYPE"]

    def increase_amount(self, amount: Union[float, int]) -> None:
        self.amount += amount

    def __repr__(self):
        return f"{self.name}: {self.amount} {self.measurement_type}"

    def __str__(self) -> str:
        return f"{self.name}: {self.amount} {self.measurement_type}"
