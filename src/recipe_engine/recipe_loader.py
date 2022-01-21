import shutil

from data.util_tools import DATA_PATH


class RecipeLoader:

    def __init__(self, recipe_dir: str) -> None:
        self.recipe_dir: str = recipe_dir

    def transfer_recipes(self) -> None:
        shutil.copytree(self.recipe_dir, DATA_PATH)