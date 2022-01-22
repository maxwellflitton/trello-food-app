import argparse
import glob
import os
import yaml

from food_organiser.recipe_engine.recipe_loader import RecipeLoader


def main() -> None:
    current_directory = os.getcwd()

    my_parser = argparse.ArgumentParser(description='arguments for the injestion of recipe files')
    my_parser.add_argument('path', default=str(current_directory), type=str, help='the path to recipe files')
    args = my_parser.parse_args()

    for i in glob.glob(args.path + "/*.yml"):
        RecipeLoader.transfer_recipe(path=i)
        print(f"{i} copied to data")


def read_recipes() -> None:
    for i in glob.glob(str(RecipeLoader.RECIPE_PATH) + "/*.yml"):
        print(i)
        with open(i) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        print(data["NAME"])
