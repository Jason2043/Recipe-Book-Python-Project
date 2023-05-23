import json
import csv

class Recipe:
    def __init__(self, name, ingredients, instructions, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.rating = rating

    def __str__(self):
        return f"Name: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}\nRating: {self.rating}"

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, instructions='{self.instructions}', rating={self.rating})"

    def to_dict(self):
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'rating': self.rating
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            ingredients=data['ingredients'],
            instructions=data['instructions'],
            rating=data['rating']
        )

    def get_average_rating(self):
        total_ratings = sum(self.rating)
        return total_ratings / len(self.rating)

recipes = []

def add_recipe():
    try:
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients, separated by commas: ").split(",")
        instructions = input("Enter instructions: ")
        rating = int(input("Enter rating (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a valid rating.")
    else:
        try:
            recipe = Recipe(name, ingredients, instructions, rating)
            recipes.append(recipe)
        except:
            print("Error occurred while adding the recipe.")
        else:
            print("Recipe added successfully!")

def delete_recipe():
    name = input("Enter name of recipe to delete: ")
    for recipe in recipes:
        if recipe.name == name:
            recipes.remove(recipe)
            print("Recipe deleted successfully!")
            return
    print("Recipe not found.")

def view_all():
    if not recipes:
        print("No recipes found.")
    else:
        for recipe in recipes:
            print(recipe)

def search_recipe():
    keyword = input("Enter keyword to search for: ")
    found_recipes = []
    for recipe in recipes:
        if keyword in recipe.name or keyword in recipe.ingredients:
            found_recipes.append(recipe)
    if found_recipes:
        for recipe in found_recipes:
            print(recipe)
    else:
        print("No recipes found matching the keyword.")

def save_recipes_txt():
    if not recipes:
        print("No recipes to save.")
        return
    try:
        with open("recipes.txt", "w") as f:
            for recipe in recipes:
                f.write(str(recipe))
                f.write("\n\n")
        print("Recipes saved successfully!")
    except IOError:
        print("Error occurred while saving the recipes.")

def save_recipes_json():
    if not recipes:
        print("No recipes to save.")
        return
    try:
        with open("recipes.json", "w") as f:
            recipe_data = [recipe.to_dict() for recipe in recipes]
            json.dump(recipe_data, f, indent=4)
        print("Recipes saved successfully!")
    except IOError:
        print("Error occurred while saving the recipes.")

def save_recipes_csv():
    if not recipes:
        print("No recipes to save.")
        return
    try:
        with open("recipes.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Ingredients", "Instructions", "Rating"])
            for recipe in recipes:
                writer.writerow([recipe.name, ', '.join(recipe.ingredients), recipe.instructions, recipe.rating])
        print("Recipes saved successfully!")
    except IOError:
        print("Error occurred while saving the recipes.")

def test_add_recipe():
    recipe = Recipe("Test Recipe", ["Ingredient 1", "Ingredient 2"], "Test Instructions", 5)
    recipes.append(recipe)
    assert recipes[0].name == "Test Recipe"
    assert recipes[0].ingredients == ["Ingredient 1", "Ingredient 2"]
    assert recipes[0].instructions == "Test Instructions"
    assert recipes[0].rating == 5

def test_delete_recipe():
    recipe = Recipe("Test Recipe", ["Ingredient 1", "Ingredient 2"], "Test Instructions", 5)
    recipes.append(recipe)
    delete_recipe()
    assert len(recipes) == 0



while True:
    print("1. Add recipe")
    print("2. Delete recipe")
    print("3. View all recipes")
    print("4. Search for recipe")
    print("5. Save recipes")
    print("6. Save in csv")
    print("7. Quit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_recipe()
    elif choice == 2:
        delete_recipe()
    elif choice == 3:
        view_all()
    elif choice == 4:
        search_recipe()
    elif choice == 5:
        save_recipes_txt()
    elif choice == 6:
        save_recipes_csv()
    elif choice == 7:
        print('See you next time')
        break
    else:
        print("Invalid choice. Try again.")
        
