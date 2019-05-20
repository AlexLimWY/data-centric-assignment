# Online Cookbook
This is a website for user-generated content. Specifically, users or authors can upload cooking recipes and the combination of all these uploads will form an online cookbook. In addition, the users can update or delete recipes on this website.

## Demo
A live demo can be found [here](https://alwy-data-centric-assignment.herokuapp.com/).

## UX
My goal in the design was a single-page application. I wanted to present all the recipes in one page, the home page. Users who wanted to find out more about a recipe can click on the ‘Show Recipe’ button to open a modal which will show the information. This modal functions like a pop-up box which can be easily closed so that the user will not need to navigate away from the home page. The information to be presented to the user and the database relations is based on the ‘Cookbook ER Diagramme.pdf’ file in the main directory of this ‘data-centric-assignment’ Cloud9 workspace.
The user can also search for recipes by their names using the search bar in the ‘Search for Recipe’ page. 
 ### Existing Features
-There is a modal button for each recipe, called ‘Show Recipe’, in the ‘Home’ page and the ‘Search for Recipe’ page so that the user can click on it to open up a pop-up box to show more information about the recipe.
- There is a search bar in in the ‘Search for Recipe’ page for the user to key in a recipe name which he or she wants to find. The user will be able to see the search results after keying in and clicking on the ‘Search’ button below the search bar.
### Features Left to Implement
- Allowing users to upload image(s) of their respective recipe(s).
## Technologies Used
1. HTML
- For structuring the website, e.g. adding content to the website.
2. CSS
- For styling the website, e.g. text alignment.
3. [Bootstrap (Version 4)](https://getbootstrap.com/)
 - The project uses Bootstrap to create mobile-responsive web pages.
## Testing
Python assertions were used to test the code automatically. The Python assert statements can be found in the ‘asserts.py’ file in the main directory of this ‘data-centric-assignment’ Cloud9 workspace.
Where Python assertions were not done, manual tests were done. For example, to test the mobile responsiveness of this website, different screen sizes were used to view the website. For example, a mobile phone screen size was used to test a small view and a desktop computer screen size was used to test a big view. 
In another example, a user trying a to add a recipe on the website would need to key in information for the blank fields such as ‘Recipe Name’ because they are required fields. Submitting the recipe without filling in the blank fields would cause an error message to appear. Successful submission of the recipe will redirect the user to the ‘Home’ page of the website.

## Deployment
This project was deployed to Heroku.
A person who wants to run this code locally can clone or download this repository from https://github.com/AlexLimWY/data-centric-assignment.git and paste it into their editor terminal.

## Credits
### Content
- The text for Chinese Roast Chicken was taken from [RASAMALAYISA](https://rasamalaysia.com/chinese-roast-chicken/)
- The text for Onion Scallion Beef was taken from [RASAMALAYISA](https://rasamalaysia.com/onion-scallion-beef/)
- The text for Braised Pork Belly in Soy Sauce (Tau Yew Bak) was taken from [RASAMALAYISA](https://rasamalaysia.com/braised-pork-belly-in-soy-sauce-tau-yew-bak/)
- The text for Sweet, sour, & spicy Korean fried chicken was taken from [Maangchi](https://www.maangchi.com/recipe/yangnyeom-tongdak)
- The text for Braised beef short ribs was taken from [Maangchi](https://www.maangchi.com/recipe/makgalbijjim)
- The text for Dumplings was taken from [Maangchi](https://www.maangchi.com/recipe/mandu)
- The text for Chicken Karaage was taken from [Japan Food Addict](http://www.japanfoodaddict.com/chicken/chicken-karaage/)
- The text for Beef Bowl was taken from [Japan Food Addict](http://www.japanfoodaddict.com/beef/beef-bowl-gyudon/)
- The text for Katsudon was taken from [Japan Food Addict](http://www.japanfoodaddict.com/pork/katsudon/)
- The list of allergens were taken from [Foodsafety.gov](https://www.foodsafety.gov/poisoning/causes/allergens/index.html)
- Some author details were taken from [Malaysian Women Weekly Magazine: July 2012](https://rasamalaysia.com/celebchef0712.pdf)

###Media
- The image for Chinese Roast Chicken was taken from [RASAMALAYISA](https://rasamalaysia.com/chinese-roast-chicken/)
- The image for Onion Scallion Beef was taken from [RASAMALAYISA](https://rasamalaysia.com/onion-scallion-beef/)
- The image for Braised Pork Belly in Soy Sauce (Tau Yew Bak) was taken from [RASAMALAYISA](https://rasamalaysia.com/braised-pork-belly-in-soy-sauce-tau-yew-bak/)
- The image for Sweet, sour, & spicy Korean fried chicken was taken from [Maangchi](https://www.maangchi.com/recipe/yangnyeom-tongdak)
- The image for Braised beef short ribs was taken from [Maangchi](https://www.maangchi.com/recipe/makgalbijjim)
- The image for Dumplings was taken from [Maangchi](https://www.maangchi.com/recipe/mandu)
- The image for Chicken Karaage was taken from [Japan Food Addict](http://www.japanfoodaddict.com/chicken/chicken-karaage/)
- The image for Beef Bowl was taken from [Japan Food Addict](http://www.japanfoodaddict.com/beef/beef-bowl-gyudon/)
- The image for Katsudon was taken from [Japan Food Addict](http://www.japanfoodaddict.com/pork/katsudon/)

### Acknowledgements
- I was inspired to produce an online cookbook because I like to try different kinds of food. I also believe that people from all over the world should their recipes with one another so that we can improve recipes and the cooking community can benefit as a whole.



