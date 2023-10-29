import openai

openai.api_key_path = "../secret/openai_api_key.txt"


class RecipeGenerator:
    def __init__(self):
        self.list_of_ingredients = self.ask_for_ingredients()

    @staticmethod
    def ask_for_ingredients():
        list_of_ingredients = []
        while True:
            ingredient = input("Enter an ingredient (or type 'done' to finish): ")
            if ingredient.lower() == "done":
                break
            list_of_ingredients.append(ingredient)

        print(f"Your ingredients are: {', '.join(list_of_ingredients)}")
        return list_of_ingredients

    def generate_recipe(self):
        prompt = RecipeGenerator.create_recipe_prompt(self.list_of_ingredients)
        if self._verify_prompt(prompt):
            response = self.generate(prompt)
            return response["choices"][0]["text"]
        raise ValueError("Prompt not accepted.")

    @staticmethod
    def create_recipe_prompt(list_of_ingredients):
        prompt = (
            f"Create a detailed recipe based on only the following ingredients: {', '.join(list_of_ingredients)}.\n"
            f"Additionally, assign a title starting with 'Recipe Title: ' to this recipe.")
        return prompt

    def _verify_prompt(self, prompt):
        print(prompt)
        response = input("Are you happy with the prompt? (y/n)")

        if response.upper() == "Y":
            return True
        return False

    @staticmethod
    def generate(prompt):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=512,
            temperature=0.7
        )
        return response

    def store_recipe(self, recipe, filename):
        with open(filename, "w") as f:
            f.write(recipe)


if __name__ == '__main__':
    """
    Test Recipe Generator class without creating an image of the dish.
    """
    recipe = RecipeGenerator.generate()
