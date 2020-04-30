import re
import click

from . import units



recipe = "/home/daniel/notes/recipes/soda-bread.recipe"

with open(recipe, "r") as f:
    data = f.read()

@click.group()
def cookbook():
    pass

@cookbook.command()
@click.argument("name")
def recipe(name):
    """
    Display an entire recipe in the terminal
    """

    output = ""

    output += "Ingredients\n"
    output += "*"*len("ingredients")+"\n"

    ingredients = Ingredients(data)
    method = Method(data)
    output += str(ingredients)

    
    output += "\nMethod\n"
    output += "*"*len("ingredients")+"\n"
    output += str(method)
    print(output)
    

def parse_units(line):
    symbols = units.symbols

    regexes = r"([\d\-\<\>\.]*)[\s]*" "(" + "|".join(list(symbols.keys())) + ")"


    parse = re.match(regexes,  line)
    if parse:
        return(symbols[parse[2]](parse[1]))
    else:
        return line

def parse_keyvals(data):
    metadata = re.findall(r"\[([\w\s]*)\] (.*)\s*\n", data)
    keyvals = {}
    for m in metadata:
        keyvals[m[0].lower()] = parse_units(m[1])
    return keyvals


class Ingredients(object):
    def __init__(self, data):
        self.ingredients = self.parse(data)
        
    def parse(self, data):
        """
        Parse a recipe file and discover any ingredients listed in it.
        """
        
        regex = r"^([\w ]*)\b[\s]{3,}([\d\w\,\.]*)$"
        ingredients = re.findall(regex, data, re.MULTILINE)
        parsed = {}
        for ingredient in ingredients:
            parsed[ingredient[0]] = parse_units(ingredient[1])
        return parsed

    def __repr__(self):
        output = ""
        for ingredient, amount in self.ingredients.items():
            output += f"{ingredient:35}   {amount}\n"
        return output

class Method(object):
    def __init__(self, data):
        """
        """
        self.method = self.parse(data)

    def parse(self, data):
        
        regex = r"(?s)(?:^# Method)[\n]+(.*)(?:(?:\n#)|(?:\n\Z))"
        return re.findall(regex, data.strip(), re.MULTILINE|re.DOTALL)[0]

    def __repr__(self):
        return self.method
        


if __name__ == "__main__":
    cookbook()
