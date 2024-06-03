# Schooner Dice
This project is a python package containing modules for implementing a dice game called "Schooner Dice".

The game is played by rolling five eight-sided dice and choosing a category that will be used to score
the roll. If the roll qualifies for a category, a certain number of points are awarded to the player based
on the rules for the chosen category.

Currently, there is only one module implemented in this package: a scoring module (described below).

## Requirements
- python3 (python 3.11 was used in development, only >=3.6 should be strictly necessary but this was not tested)

## Set up environment for testing/development (Linux/MacOS)
Each instruction is followed by a command to be executed from a terminal.

1. Create a python virtual environment (replace the path with your desired file location):  
    `python3 -m venv path/to/schooner_dice_venv`

2. Activate the virtual environment, once again replacing the path with the one used in Step 1:  
    `source path/to/schooner_dice_venv/bin/activate`

    This should add the virtual environment name to your terminal prompt, but you can otherwise verify that it is activated
    by running:  
    `which python`

    This should output path/to/schooner_dice_venv/bin/python

3. From the top level of the project directory (where the pyproject.toml file is located), run the following:  
    `python -m pip install -e .`

## Build the project into a distribution package (Linux/MacOS)
If you already have a testing/development environment for this project (see above) you can start at Step 2.

1. Create a python virtual environment (replace the path with your desired file location):  
    `python3 -m venv path/to/schooner_dice_venv`

2. Activate the virtual environment, once again replacing the path with the one used in Step 1:  
    `source path/to/schooner_dice_venv/bin/activate`

    This should add the virtual environment name to your terminal prompt, but you can otherwise verify that it is activated
    by running:  
    `which python`

    This should output path/to/schooner_dice_venv/bin/python

3. Install build tools:  
    `python -m pip install --upgrade build`

4. From the top level of the project directory (where the pyproject.toml file is located), run the following:  
    `python -m build`

    This will output distribution packages into the `dist` folder of the project directory.

## Usage
The package needs to be installed in whatever python environment you plan on using it.
See above methods for installing or creating an installable distribution package.

Unit tests can be run by evoking the python interpreter on the test source file directly, like so:  
    `python tests/test_score_calculator.py`

The score_calculator module itself can be imported in another python module or the python REPL with:  
    `from schooner_dice import score_calculator`

The methods exposed from the score_calculator module are:  
| Method Name | Parameters : Type | Returns : Type |
| ----------- | ---------- | ------ |
| score() | category : Category(Enum) <br/> dice_roll : List[int] | The score of the dice_roll in the given category : int |
| top_categories() | dice_roll -> List[int] | List of one or more top scoring Category for the given dice_roll : List[Category(Enum)] |