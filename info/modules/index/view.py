from flask import current_app
from flask import render_template

from . import index_blu, register_blu, login_blu


@index_blu.route('/')
def index():
    return render_template('news/index.html')
@register_blu.route('/register')
def register():
    return 'register'
@login_blu.route('/login')
def index():
    return 'login'

@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')