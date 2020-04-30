"""
Various units.
"""
import sys, inspect


class Unit(object):
    symbol = []
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value} {self.symbol[0]}"

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
    symbol = ["l", "ls"]

class Teaspoon(Unit):
    name = "teaspoon"
    symbol = ["tsp", "tsps", "teaspoons"]
    
symbols = {}
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        if issubclass(obj, Unit):
            for symbol in obj.symbol:
                symbols[symbol] = obj
