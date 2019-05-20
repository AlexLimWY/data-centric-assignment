# from app import home, add, edit, delete, search
import os
import pymysql

conn = pymysql.connect(host='localhost', user='alexlimwy', password='', db='cookbook')

def test_home():
    cursor=pymysql.cursors.DictCursor(conn)
    cursor.execute("""
    SELECT Recipe.recipe_id, Recipe.recipe_name, Recipe.description, Recipe.cooking_instructions, Cuisine.cuisine_name, Recipe.image, Author.author_name, Author_country_of_origin.author_country_of_origin_name,
    Ingredient.ingredient_name, Allergen.allergen_name
    FROM  `Recipe`
    JOIN Cuisine ON Recipe.cuisine_id = Cuisine.cuisine_id
    JOIN Author ON Recipe.author_id = Author.author_id
    JOIN Author_country_of_origin ON Author.author_country_of_origin_id = Author_country_of_origin.author_country_of_origin_id
    JOIN Recipe_ingredient ON Recipe.recipe_id = Recipe_ingredient.recipe_id
    JOIN Ingredient ON Recipe_ingredient.ingredient_id = Ingredient.ingredient_id
    JOIN Recipe_allergen ON Recipe.recipe_id = Recipe_allergen.recipe_id
    JOIN Allergen ON Recipe_allergen.allergen_id = Allergen.allergen_id
    """)
    recipes = cursor.fetchall()
    assert recipes != None, "'recipes' should not return None"
    assert recipes != "", "'recipes' should not return an empty string"
    assert recipes != 0, "'recipes' should not return 0"
    assert recipes != False, "'recipes' should not return 0"

def test_add():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute('SELECT * from Ingredient')
    Ingredients = cursor.fetchall()
    assert Ingredients != None, "'Ingredients' should not return None"
    assert Ingredients != "", "'Ingredients' should not return an empty string"
    assert Ingredients != 0, "'Ingredients' should not return 0"
    assert Ingredients != False, "'Ingredients' should not return 0"

def test_edit():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute('SELECT * from Author_country_of_origin ORDER BY author_country_of_origin_name')
    Countries = cursor.fetchall()    
    assert Countries != None, "'Countries' should not return None"
    assert Countries != "", "'Countries' should not return an empty string"
    assert Countries != 0, "'Countries' should not return 0"
    assert Countries != False, "'Countries' should not return 0"    

def test_search():
    sql = """
    SELECT Recipe.recipe_id, Recipe.recipe_name, Recipe.description, Recipe.cooking_instructions, Cuisine.cuisine_name, Recipe.image, Author.author_name, Author_country_of_origin.author_country_of_origin_name,
    Ingredient.ingredient_name, Allergen.allergen_name
    FROM  `Recipe`
    JOIN Cuisine ON Recipe.cuisine_id = Cuisine.cuisine_id
    JOIN Author ON Recipe.author_id = Author.author_id
    JOIN Author_country_of_origin ON Author.author_country_of_origin_id = Author_country_of_origin.author_country_of_origin_id
    JOIN Recipe_ingredient ON Recipe.recipe_id = Recipe_ingredient.recipe_id
    JOIN Ingredient ON Recipe_ingredient.ingredient_id = Ingredient.ingredient_id
    JOIN Recipe_allergen ON Recipe.recipe_id = Recipe_allergen.recipe_id
    JOIN Allergen ON Recipe_allergen.allergen_id = Allergen.allergen_id
    """
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute(sql)
    recipes = cursor.fetchall()        
    assert recipes != None, "'recipes' should not return None"
    assert recipes != "", "'recipes' should not return an empty string"
    assert recipes != 0, "'recipes' should not return 0"
    assert recipes != False, "'recipes' should not return 0"
    
test_home()
test_add()
test_edit() 
test_search()
print("All the tests passed")    