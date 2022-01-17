from typing import List

from recipe_engine.ingredient import Ingredient
from recipe_engine.step import Step


class Recipe:

    def __init__(self, raw_data: dict) -> None:
        self.name: str = raw_data["NAME"]
        self.type: str = raw_data["TYPE"]
        self.country: str = raw_data["COUNTRY"]
        self.ingredients: List[Ingredient] = [Ingredient(raw_data=i) for i in raw_data["INGREDIENTS"]]
        self.steps: List[Step] = [Step(raw_data=i) for i in raw_data["STEPS"]]
