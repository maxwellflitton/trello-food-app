from typing import List, Union

import yaml

from data.util_tools import DATA_PATH
from recipe_engine.recipe import Recipe


class IngredientMap(dict):

    RECIPE_PATH = DATA_PATH + "/recipes/"

    def __init__(self, input_recipes: List[str]) -> None:
        super().__init__({})
        self.input_recipes: List[str] = input_recipes
        self.loaded_recipes: List[Recipe] = []
        self._load_all_recipes()
        self._load_all_ingredients()

    def load_ingredient(self, name: str, amount: Union[int, float]) -> None:
        measurement = self.get(name)
        if measurement is None:
            self[name] = amount
        else:
            self[name] += amount

    def load_recipe(self, recipe_name: str):
        full_path: str = f"{self.RECIPE_PATH}{recipe_name.replace(' ', '_')}.yml"
        with open(full_path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        recipe: Recipe = Recipe(raw_data=data)
        self.loaded_recipes.append(recipe)

    def _load_all_recipes(self) -> None:
        for recipe_name in self.input_recipes:
            self.load_recipe(recipe_name=recipe_name)

    def _load_all_ingredients(self) -> None:
        for recipe in self.loaded_recipes:
            for ingredient in recipe.ingredients:
                self.load_ingredient(name=ingredient.name, amount=ingredient.amount)


if __name__ == "__main__":
    test = IngredientMap(input_recipes=["banana_bread", "black_daal", "katsu_curry", "banana_bread"])
    print(test)
