"""
Various units.
"""
import sys, inspect
import re

class Unit(object):
    symbol = [""]
    name = "unit"
    def __init__(self, value, maximum=None, modifier=None):
        self.value = value
        self.maximum = maximum
        self.modifier = modifier

    def __repr__(self):
        return f"{self.value} {self.symbol[0]}"

    def __mul__(self, factor):
        if isinstance(factor, Unit):
            if factor.name == self.name:
                return symbols[self.name](float(self.value) * float(factor.value))
            else:
                raise ValueError
        elif isinstance(factor, float):
            return symbols[self.name](float(self.value) * float(factor))
    
    def __truediv__(self, quotient):
        if quotient.name == self.name:
            if self.name == "unit":
                return Unit(float(self.value) / float(quotient.value))
            else:
                return symbols[self.name](float(self.value) / float(quotient.value))
        else:
            raise ValueError

class Minute(Unit):
    name = "minute"
    symbol = ["min", "minute", "minutes", "mins"]
    
class Gram(Unit):
    name = "gram"
    symbol = ["g", "gm", "gms"]

class Kilogram(Unit):

    name = "kilogram"
    symbol = ["kg"]

    equivalence = {
        Gram: 1000
    }

class Millilitre(Unit):
    name = "millilitre"
    symbol = ["ml", "millilitre", "mls"]

class Litre(Unit):
    name = "litre"
    symbol = ["l", "ls", "litre", "litres"]

class Teaspoon(Unit):
    name = "teaspoon"
    symbol = ["tsp", "tsps", "teaspoons"]
    
symbols = {}
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        if issubclass(obj, Unit):
            for symbol in obj.symbol:
                symbols[symbol] = obj

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        if issubclass(obj, Unit):
            symbols[obj.name] = obj

                
def parse_units(line):

    regexes = r"([\<\>\.]*)[\s]*([\d\.]*)[\s]*[-]?[\s]*([\d\.]*)" "(" + "|".join(list(symbols.keys())) + ")"


    parse = re.match(regexes,  line)
    
    if parse:
        if not parse[4] == "":
            return(symbols[parse[4]](value = parse[2], maximum = parse[3],  modifier = parse[1]))
        else:
            return(Unit(value = parse[2], maximum = parse[3],  modifier = parse[1]))
    else:
        return line
