from flask import Flask, render_template
from post import Post
import requests
import datetime

today = datetime.date.today()
year = today.year

AUTHOR = "Suzana Serboi"
blog_url = "https://api.npoint.io/93d4fda66d6ecc6f55dd"
response = requests.get(blog_url)
posts = response.json()

post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", cur_year=year, my_name=AUTHOR, all_posts=post_objects)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)


