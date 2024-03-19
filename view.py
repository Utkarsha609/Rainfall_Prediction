from flask import render_template, request
import first

def front():
    return render_template('Front_ Page.html')

def index():
    return render_template('index.html')



