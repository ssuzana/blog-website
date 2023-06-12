# blog-website

## Project Step by Step
### Step 1.  
 * Created a project environment in VS Code.
 * Installed Flask in the virtual environment using `python -m pip install flask`
 * Created a simple Flask app. 
 * See [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask) for more details.

### Step 2. 
* Used [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating engine to pass variables defined in `app.py` to `index.html`. In the html file we write variables surrounded by double curly braces, such as `{{ variable_name }}`. Jinja also allows us to write code similar to Python syntax inside an html file.
* Updated webpage footer to display the current year.

### Step 3.
* Created a JSON storage bin containing fake blog data using [npoint.io](npoint.io). You can access this bin via the API at:
   https://api.npoint.io/93d4fda66d6ecc6f55dd. Anyone with the link is able to view this JSON bin.
* Used the `requests` module to get the json data from the bin.

### Step 4. 
* Wrote multiline statements with Jinja in `index.html` to display the blog data.
* Made a "Read" anchor tag at the end of each blog post preview link to a page with the entire blog post - title, subtitle and body.
* The individual blog posts live at the path: URL/post/post_id.
* Added static files for webpage styling.

