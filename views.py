from devWepApp import app

from Flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title='Homepage')