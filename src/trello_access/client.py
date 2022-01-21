from typing import List

from trello import TrelloClient

from errors import BoardNotFoundError, ListNotFoundError
from recipe_engine.ingredient_map import IngredientMap, Ingredient, Recipe


class TrelloRecipeCardGenerator:

    def __init__(self, recipes: List[str], api_key: str, token: str, board_name: str, list_name: str) -> None:
        self.ingredient_map: IngredientMap = IngredientMap(input_recipes=recipes)
        self.client = TrelloClient(api_key=api_key, token=token)
        self.list_name: str = list_name
        self.board_id: str = self._get_board_id(board_name=board_name)
        self.board = self.client.get_board(self.board_id)
        self.list_id: str = self._get_list_id(list_name=list_name)
        self.target_list = self.board.get_list(self.list_id)

    def _get_board_id(self, board_name: str) -> str:
        for board in self.client.list_boards():
            if board.name == board_name:
                return board.id
        raise BoardNotFoundError(message=f"board {board_name} not found on your trello account")

    def _get_list_id(self, list_name: str) -> str:
        for list_object in self.board.all_lists():
            if list_object.name == list_name:
                return list_object.id
        raise ListNotFoundError(message=f"list called {list_name} not found in board called {self.board.name}")

    def _generate_all_ingredients(self) -> List[str]:
        buffer: List[str] = []

        for key in self.ingredient_map.keys():
            ingredient: Ingredient = self.ingredient_map[key]
            message: str = f"{key}: {ingredient.amount} {ingredient.measurement_type}"
            buffer.append(message)
        return buffer

    def create_recipe_card(self, recipe: Recipe):
        created_card = self.target_list.add_card(f"{recipe.name} recipe", "collated food shopping for the week")
        buffer: List[str] = []

        for ingredient in recipe.ingredients:
            message = f"{ingredient.name}: {ingredient.amount} {ingredient.measurement_type}"
            buffer.append(message)

        created_card.add_checklist(title="ingredients", items=buffer)

        buffer: List[str] = []
        for step in recipe.steps:
            message = f"minutes: {step.time} description: {step.instruction} ingredients: {step.ingredients}"
            buffer.append(message)
        created_card.add_checklist(title="steps", items=buffer)

    def create_all_recipe_cards(self):
        for recipe in self.ingredient_map.loaded_recipes:
            self.create_recipe_card(recipe=recipe)

    def create_full_shopping_list(self) -> None:
        created_card = self.target_list.add_card("Shopping for the week", "collated food shopping for the week")
        created_card.add_checklist(title="ingredients", items=self._generate_all_ingredients())

    def generate_recipes(self) -> None:
        self.create_full_shopping_list()
        self.create_all_recipe_cards()
