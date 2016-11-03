from appers import application
from flask import flash, redirect, render_template, request, session, abort, url_for, jsonify
from dbconnect import *

@application.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		temp_name = request.form['email']
		print temp_name
		insert_email(temp_name)
		flash("Thank you for signing Up")
	return render_template('index.html')