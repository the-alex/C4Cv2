from flask import Flask, render_template, session, url_for, redirect, request, flash
import controllers

# Used for sessions
from os import urandom
from datetime import timedelta

app = Flask(__name__, template_folder='templates')

app.secret_key = urandom(24)
app.permanent = True
app.permanent_session_lifetime = timedelta(minutes=(60*24)) # One day


# Example how to add a blueprint to hierarchy
# app.register_blueprint(controllers.login)

app.register_blueprint(controllers.index)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)
