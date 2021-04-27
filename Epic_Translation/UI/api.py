#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def translate_string(original, source, target):
	strang = "something's happening"
	return "yoyoyoyoyoyoyo"

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
	original = request.form['original']
	source = request.form['source']
	target = request.form['target']

	newstring = translate_string(original, source, target)
	result = {
		"output": newstring
	}
	result = {str(key): value for key, value in result.items()}
	#result = newstring
	return jsonify(result=result)


if __name__ == '__main__':
	app.run(debug=True)
