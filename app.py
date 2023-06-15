from flask import Flask, render_template
import requests
import datetime

today = datetime.date.today()
year = today.year

posts = requests.get("https://api.npoint.io/1aae2705ffab608abf4e").json()

app = Flask(__name__)


@app.route('/')
def home():
    #return render_template("index.html", cur_year=year, my_name=AUTHOR, all_posts=post_objects)
    return render_template("index.html", all_posts=posts, cur_year=year)

@app.route("/about")
def about():
    return render_template("about.html", cur_year=year)


@app.route("/contact")
def contact():
    return render_template("contact.html", cur_year=year)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", all_posts=posts, post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


