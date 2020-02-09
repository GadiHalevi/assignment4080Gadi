"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, flash
from DemoFormProject import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, BooleanField, PasswordField, validators, TextField, TextAreaField, SelectField, DataField, ValidationError
from wtforms.validators import DataRequired
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests
import io
import base64
from os import path

from assingment4080Gadi import app
from assingment4080Gadi.Models.QueryFormStructure import QueryFormStructure





@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/gallery')
def gallery():
    """Renders the about page."""
    return render_template(
        'gallery.html',
        title='Gallery',
        year=datetime.now().year,
        message='Your gallery page.'
    )

@app.route('/Query', methods=['GET', 'Post'])
def Query():
    
    name = None
    Capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\capitals.csv'))
    df = df.set_index('Country')

    form = QueryFormStructure(request.form)

    if (request.method == 'POST' ):
        name = form.name.data
        if (name in df.index):
            capital = df.loc[name, 'Capital']
        else:
            capital = name + ', no such country'
        form.name.data = ''

    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('Query.html',
            form = form,
            name = capital,
            raw_data_table = raw_data_table,
            title = 'Query by the user',
            year=datetime.now().year,
            message='This page will use the web forms to get user input'
         )



