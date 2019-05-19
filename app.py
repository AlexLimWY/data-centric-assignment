from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os
import pymysql

conn = pymysql.connect(host='localhost', user='alexlimwy', password='', db='cookbook')

app = Flask (__name__)

@app.route('/')
def home():
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
    print(recipes)
    return render_template('index.html', all_recipes=recipes)


@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute('SELECT * from Ingredient')
        Ingredients = cursor.fetchall()
        
        cursor.execute('SELECT * from Allergen')
        Allergens = cursor.fetchall()
        
        cursor.execute('SELECT * from Cuisine')
        Cuisines = cursor.fetchall()
        
        cursor.execute('SELECT * from Author_country_of_origin ORDER BY author_country_of_origin_name')
        Countries = cursor.fetchall()        
        return render_template('add.html', all_ingredients=Ingredients, all_allergens=Allergens, all_cuisines = Cuisines, all_countries = Countries)
    else:
        print(request.form)
        recipe_name = request.form['recipe']
        description = request.form['description']
        ingredient_id = request.form['ingredient']
        allergen_id = request.form['allergen']
        cuisine_id = request.form['cuisine']
        cooking_instructions = request.form['instructions']
        author_name = request.form['author']
        author_country_of_origin_id = request.form['country']
        cursor = pymysql.cursors.DictCursor(conn)
        
        sql = "INSERT INTO Author (author_id, author_name, author_country_of_origin_id) VALUES (null, %s, %s)"
        values = (author_name, author_country_of_origin_id)
        cursor.execute(sql, values)
        new_author_id = cursor.lastrowid
        
        sql = "INSERT INTO Recipe (cuisine_id, recipe_name, description, cooking_instructions, image, author_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (cuisine_id, recipe_name, description, cooking_instructions,'', new_author_id)
        cursor.execute(sql, values)
        new_recipe_id = cursor.lastrowid
        
        sql = """
            INSERT INTO Recipe_ingredient (recipe_ingredient_id, recipe_id, ingredient_id)
            VALUES (null, %s, %s)
        """
        values = (new_recipe_id, ingredient_id)
        cursor.execute(sql, values)
        
        sql = """
            INSERT INTO Recipe_allergen (recipe_allergen_id, recipe_id, allergen_id)
            VALUES (null, %s, %s)
        """
        values = (new_recipe_id, allergen_id)
        cursor.execute(sql, values)

        conn.commit()
        cursor.close();
        return redirect('/')        
    
@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    if request.method == 'GET':
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute('SELECT * from Ingredient')
        Ingredients = cursor.fetchall()
        
        cursor.execute('SELECT * from Allergen')
        Allergens = cursor.fetchall()
        
        cursor.execute('SELECT * from Author_country_of_origin ORDER BY author_country_of_origin_name')
        Countries = cursor.fetchall()    
        
        cursor.execute('SELECT * from Cuisine')
        Cuisines = cursor.fetchall()
        
        cursor.execute('SELECT * from Author')
        Authors = cursor.fetchall()
        
        cursor.execute("SELECT * FROM Recipe WHERE recipe_id = " + recipe_id)
        recipe = cursor.fetchone()
        return render_template('edit.html', recipe=recipe, all_ingredients=Ingredients, all_allergens=Allergens, all_countries = Countries, all_cuisines = Cuisines, all_authors=Authors)    
    
    else:
        recipe_name = request.form['recipe']
        description = request.form['description']
        ingredient_id = request.form['ingredient']
        allergen_id = request.form['allergen']
        cuisine_id = request.form['cuisine']
        cooking_instructions = request.form['instructions']
        author_name = request.form['author']
        author_country_of_origin_id = request.form['country']
        cursor = pymysql.cursors.DictCursor(conn)

        sql = """
        UPDATE Recipe
        JOIN Author
        ON Recipe.author_id = Author.author_id
        JOIN Author_country_of_origin 
        ON Author.author_country_of_origin_id = Author_country_of_origin.author_country_of_origin_id
        SET Recipe.cuisine_id = {},
        Recipe.recipe_name = "{}", 
        Recipe.description = "{}",
        Recipe.cooking_instructions = "{}",
        Author.author_name = "{}",
        Author.author_country_of_origin_id = {}
        WHERE Recipe.recipe_id = {}
        """.format(cuisine_id, recipe_name, description, cooking_instructions, author_name, author_country_of_origin_id, recipe_id)
        cursor.execute(sql)   

        sql = """
        UPDATE Recipe_allergen SET allergen_id = {}
        WHERE recipe_id = {}
        """.format(allergen_id, recipe_id)
        cursor.execute(sql)        

        sql = """
        UPDATE Recipe_ingredient SET ingredient_id = {}
        WHERE recipe_id = {}
        """.format(ingredient_id, recipe_id)
        cursor.execute(sql)   
        
        conn.commit()
        cursor.close();
        return redirect('/')
        
@app.route('/delete/<recipe_id>') 
def delete(recipe_id):
    cursor = pymysql.cursors.DictCursor(conn)
    
    sql = "DELETE FROM Recipe_allergen WHERE recipe_id = {}".format(recipe_id)
    cursor.execute(sql)
    
    sql = "DELETE FROM Recipe_ingredient WHERE recipe_id = {}".format(recipe_id)
    cursor.execute(sql)
    
    sql = "DELETE FROM Recipe WHERE recipe_id = {}".format(recipe_id)
    cursor.execute(sql)

    conn.commit()
    cursor.close();
    return redirect('/')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    
