from flask import Flask, render_template
import requests
import random
import datetime

today = datetime.date.today()
year = today.year

AUTHOR = "Suzana Serboi"

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", rand_num=random_number, cur_year=year, my_name=AUTHOR)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/93d4fda66d6ecc6f55dd"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


