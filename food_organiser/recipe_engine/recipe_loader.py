import shutil

from food_organiser.data.util_tools import DATA_PATH


class RecipeLoader:

    def __init__(self, recipe_dir: str) -> None:
        self.recipe_dir: str = recipe_dir

    def transfer_recipes(self) -> None:
        shutil.copytree(self.recipe_dir, DATA_PATH)

    @staticmethod
    def transfer_recipe(path: str) -> None:
        filename: str = path.split("/")[-1]
        shutil.copyfile(path, DATA_PATH + f"/{filename}")
