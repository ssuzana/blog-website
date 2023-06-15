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

### Step 4. 
* Upgraded the website using the Bootstrap Clean Blog Template found at: https://startbootstrap.com/previews/clean-blog/ with the following features:
     - multi-page website with an interactive navigation bar
     - dynamically generated blog post pages with full screen titles
     - fully mobile responsive with an adaptive navigation bar

* Created the `static` and `templates` folders and moved the files in the project to the correct folders 

* Fixed the url's for the static resources so that the styling and bootstrap all appear

* Updated `app.py` so that when you click on the `About` link in the navigation bar it goes to the About page and likewise with the Contact page.

* Using the documentation from Jinja: https://jinja.palletsprojects.com/en/2.11.x/templates/#include
  - removed the `<head>` & navigation code from index.html and place it in the header.html file.
  - removed the `<footer>` from index.html and place it in the footer.html file.
  create a header and footer template which can then be applied to all web pages in your website.
   - used `{% include "header.html" %}` and `{% include "footer.html" %}` to make the website still function exactly the same as before.

* Step 5. 
 To be updated.   

