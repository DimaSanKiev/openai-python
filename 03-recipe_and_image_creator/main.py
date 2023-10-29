from recipe import RecipeGenerator
from dalle import Dish2Image


def main():
    # Create an instance of the RecipeGenerator class
    gen = RecipeGenerator()
    # Ask the user for ingredients input and create the recipe
    recipe = gen.generate_recipe()
    # Print the recipe
    print(recipe)
    # Create an instance of the Dish2Image class
    dalle = Dish2Image(recipe)
    # Visualize the dish
    dalle.generate_image()
    # Store the recipe in a text file
    gen.store_recipe(recipe, f"recipes_log/{dalle.title}.txt")


if __name__ == '__main__':
    main()
