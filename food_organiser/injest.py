import argparse
import glob
import os


def main() -> None:
    current_directory = os.getcwd()

    my_parser = argparse.ArgumentParser(description='arguments for the injestion of recipe files')
    my_parser.add_argument('path', default=str(current_directory), type=str, help='the path to recipe files')
    args = my_parser.parse_args()
    for i in glob.glob(args.path + "/*.yml"):
        print(i)

