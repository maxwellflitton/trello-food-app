from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name='food_organiser',
   version='0.1.0',
   author='maxwell flitton',
   author_email='maxwellflitton@gmail.com',
   packages=find_packages(exclude=("tests",)),
   scripts=[],
   url="https://github.com/maxwellflitton/trello-food-app",
   description='basic automation tool',
   long_description=read('README.md'),
   package_data={
        'data': ['*']
    },
   include_package_data=True,
   install_requires=[
   ],
   entry_points={
       "console_scripts": [
           "fo-injest=food_organiser.injest:main",
           "fo-get all=food_organiser.injest:read_recipes",
        ]
   },
)
