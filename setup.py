from setuptools import setup, find_packages


setup(
   name='Obcessive Food Disorder',
   version='0.1.0',
   author='maxwell flitton',
   author_email='maxwellflitton@gmail.com',
   packages=find_packages(exclude=("tests",)),
   scripts=[],
   url="https://github.com/maxwellflitton/trello-food-app",
   description='basic automation tool',
   long_description="automation tool",
   package_data={
        'data': ['*']
    },
   include_package_data=True,
   install_requires=[
   ],
   entry_points={
       "console_scripts": [
           "odf-inject=cli.injest:main"
        ]
   },
)
