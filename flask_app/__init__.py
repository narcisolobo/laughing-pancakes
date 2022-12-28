from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'superhero'
bootstrap = Bootstrap5(app)
