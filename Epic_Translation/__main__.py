###############################################################################
# 
# __main__.py
# Authors: Epic Systems Preternship Team
# Date: April 25, 2021
#
# This is the main driver to execute translate.py
#
###############################################################################

from translation import translation
import json
from flask import Flask, request, render_template,jsonify

if __name__ == '__main__':

	app = Flask(__name__)
	@app.route('/')
	def home():
		return render_template('home.html')
	@app.route('/join', methods=['GET','POST'])
	def my_form_post():
		text1 = request.form['text1']
		word = request.args.get('text1')
		text2 = request.form['text2']
		text3 = request.form['text3']

		prescrip, source, target = translation.get_input(text1,text2,text3)
		tok_strings = translation.tokenize_prescrip(prescrip)
		trans_strs = translation.check_tokenized_phrases(tok_strings, source, target)
		final_trans = translation.concat_translation(trans_strs)
		
		result = {
			"output": final_trans
		}
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)
	if __name__ == '__main__':
		app.run(debug=True)
