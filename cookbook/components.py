import re
from . import units

class Metadata(object):
    def __init__(self, data):
        """
        Store and parse metadata for a recipe.
        """
        self.metadata = self.parse_keyvals(data)

    def __getitem__(self, key):
        return self.metadata[key]

    def __contains__(self, item):
        return item in self.metadata
        
    def parse_keyvals(self, data):
        metadata = re.findall(r"\[([\w\s]*)\] (.*)\s*\n", data)
        keyvals = {}
        for m in metadata:
            keyvals[m[0].lower()] = units.parse_units(m[1])
        return keyvals

    
class Ingredients(object):
    def __init__(self, data):
        self.ingredients = self.parse(data)
        
    def parse(self, data):
        """
        Parse a recipe file and discover any ingredients listed in it.
        """
        
        regex = r"^([\w ]*)\b(?:[\ ]{3,}|[\t]+)([\d\w\,\.]*)$"
        ingredients = re.findall(regex, data, re.MULTILINE)
        parsed = {}
        for ingredient in ingredients:
            parsed[ingredient[0]] = units.parse_units(ingredient[1])
        return parsed

    def scale(self, ryield, dyield):
        """
        Rescale all of the ingredients to achieve the desired recipe yield.

        Parameters
        ----------
        ryield : cookbook.Unit
           The intended yield of the recipe.
        dyield : cookbook.Unit
           The desired yield of the recipe.
        """
        scale_factor = (dyield / ryield).value
        for ingredient, amount in self.ingredients.items():
            self.ingredients[ingredient] = amount * scale_factor

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
