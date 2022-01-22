import shutil

from food_organiser.data.util_tools import DATA_PATH


class RecipeLoader:

    RECIPE_PATH = DATA_PATH + "/recipes/"

    def __init__(self, recipe_dir: str) -> None:
        self.recipe_dir: str = recipe_dir

    def transfer_recipes(self) -> None:
        shutil.copytree(self.recipe_dir, DATA_PATH)

    @classmethod
    def transfer_recipe(cls, path: str) -> None:
        filename: str = path.split("/")[-1]
        shutil.copyfile(path, cls.RECIPE_PATH + f"/{filename}")
