Cookbook
========

Cookbook is a command-line recipe book which stores your recipes as plaintext files.


The .recipe format
------------------

Recipe files have two essential parts: the Ingredients and the Method.

Ingredients
~~~~~~~~~~~

The ingredients section has a fixed format.
Each line should contain a single ingredient, and its quantity for the recipe.
The name of the ingredient and the quantity needs to be separated by at least three spaces or a tab, but the quantity and its units do not need to be separated by a space.

For example
::
   # Ingredients

   Flour         125g
   Egg           2
   Water         10ml

Method
~~~~~~~

The methods section is free-form text.

Metadata
~~~~~~~~

Metadata can be stored anywhere in the recipe file by adding a line which starts with a key in square brackets followed by a value.
It may be helpful to keep most of the metadata at the top of the file, but `cookbook` should be able to find it anywhere in the file.

You can include things like the preparation time, or categories for the recipe this way.

For example
::
   [Cooking time] 18 hours
   [Preparation time] 3 minutes


Example recipe
~~~~~~~~~~~~~~
::
   [Preparation time] 30 min
   [Cooking time] 30 min
   [Categories] Tray-bake
   [Servings] 8

   # Description

   A blondie is essentially a brownie variant - a dense cake with butterscotch being the predominant flavor instead of chocolate. Characteristics to strive for include a rich, buttery flavor with good balance between sweetness and saltiness, moist texture, and a golden blonde appearance. This recipe should provide good foundation for further experimentation if you are so inclined.

   # Ingredients

   Flour			125 g
   Baking powder		1 tsp
   Salt   			0.75 tsp
   Unsalted butter		120 g
   Dark brown sugar	240 g
   Vanilla extract		1 tbsp
   Egg			1
   Chopped pecans		180 g

   # Method

   1. Preheat oven to 325°F (170°C).
   2. Dry toast the chopped pecans until fragrant and slightly colored. This can either be done in a dry skillet on the stove top over medium high heat while stirring frequently or else by roasting the nuts in the oven on a cookie sheet while you prepare the batter. The stove top method is faster but requires more attention. It is also possible to buy dry toasted nuts instead of raw to avoid this step. The pecans should be crunchy and nutty, not rubbery or mealy.
   3. In a small bowl stir together the flour, baking powder and salt. Set aside.
   4. In a large bowl, stir the melted butter, brown sugar, and vanilla until uniform, breaking any large lumps of sugar.
   5. Beat in egg until creamy.
   6. Gently fold in flour mixture. When flour is nearly incorporated, gently fold in toasted pecans. Do not overmix.
   7. Spread mixture into buttered 8"x8" (20cm x 20cm)baking dish.
   8. Bake @ 325°F (170°C) for 30 minutes or until desired doneness.
   9. Let cool and cut into bars.
