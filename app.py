from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)


