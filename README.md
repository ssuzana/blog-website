# blog-website

## Project Step by Step
### Step 1.  
 * Created a project environment in VS Code.
 * Installed Flask in the virtual environment using `python -m pip install flask`
 * Created a simple Flask app. 
 * See [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask) for more details.

### Step 2. 
* Used [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating engine to produce dynamic HTML pages. 
* Updated webpage footer to display the current year.

### Step 3.
* Created a JSON storage bin containing fake blog data using [npoint.io](npoint.io). You can access this bin via the API at:
   https://api.npoint.io/93d4fda66d6ecc6f55dd. Anyone with the link is able to view this JSON bin.
* Used the `requests` module to get the json data from the bin.
* Created a new app route `/blog` which renders `blog.html`.
* Wrote multiline statements with Jinja in `blog.html` to display the blog data.

