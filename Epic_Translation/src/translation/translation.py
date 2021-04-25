###########################################################################
# 
# translation.py
# Authors: Epic Systems Preternship Team
# Date: April 18, 2021
#
# main logic and functions for translation system
#
############################################################################

import translation_dict
import pydeepl
import nltk


# Split prescription into phrases
# @param    string
# @return   list of separated phrases
def tokenize_prescrip(prescription):
		tokenizer = nltk.tokenize.MWETokenizer([('by', 'mouth'), ('into', 'affected', 'nostril(s)'), ('as', 'instructed'),
								('into', 'one', 'nostril'), ('as', 'directed'), ('blood', 'sugar'), ('into', 'affected', 'eye(s)'), 
								('under', 'the', 'skin'), ('each', 'day'), ('a', 'day'), ('for', 'up', 'to', 'seven', 'days'), ('for', 'pain'), 
								('with', 'meals'), ('if', 'needed'), ('at', 'bed', 'time'), ('mild', 'pain'), ('for', 'moderate', 'pain'), 
								('do', 'not', 'crush', 'or', 'chew'), ('for', 'wheezing'), ('for', 'cough'), ('for', 'blood', 'pressure'), 
								('at', 'the', 'same', 'time'), ('for', 'cholesterol'), ('in', 'the', 'morning'), ('in', 'the', 'evening')])

		words = tokenizer.tokenize(prescription.split());
		return words

# Check if phrase is in dictionary
# @param    string
# @return   if found, return translated value; else return empty string
def find_in_dict(phrase):
    pass

# Call pydeepl API if phrase is not found
# @param    string
# @return   return translated value
def call_translate_api(phrase):
    pass

# Concatenate translated words together into one phrase
# @param    list of strings
# @return   translated phrase
def concat_translation(phrases):
    pass
