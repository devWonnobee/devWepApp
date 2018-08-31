from devWepApp import app 

@app.route('/')
def index():
    return 'Hello Michael!'