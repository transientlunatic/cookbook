import click

from .components import Ingredients, Method, Metadata
from . import units

def find_recipe_file(name):
    """
    Search the recipes storage directory for a recipe which fits this name.

    Parameters
    ----------
    name : str
       The name of the recipe.

    Returns
    -------
    File
    """
    name = name.replace(" ", "-")
    recipe = f"/home/daniel/notes/recipes/{name}.recipe"

    return recipe

def recipe_data(name):
    """
    Open a recipe file for a recipe with a given name.

    """
    
    with open(find_recipe_file(name), "r") as recipe:
        data = recipe.read()
    return data
    
        

@click.group()
def cookbook():
    pass

@cookbook.command()
@click.argument("name", nargs=-1)
@click.option("--yield", "dyield")
def recipe(name, dyield):
    """
    Display an entire recipe in the terminal

    Parameters
    ----------
    dyield : str
       The amount which the recipe should yield
    """

    dyield = units.parse_units(dyield)
    
    name = "-".join(name)
    data = recipe_data(name)

    metadata = Metadata(data)
    
    output = ""

    output += "Ingredients\n"
    output += "*"*len("ingredients")+"\n"

    ingredients = Ingredients(data)
    # Rescale the ingredients for the desired yield
    if "yield" in metadata:
        ingredients.scale(metadata['yield'], dyield)
    method = Method(data)
    output += str(ingredients)

    
    output += "\nMethod\n"
    output += "*"*len("ingredients")+"\n"
    output += str(method)
    print(output)
    





        


if __name__ == "__main__":
    cookbook()
