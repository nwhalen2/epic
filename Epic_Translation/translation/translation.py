###########################################################################
# 
# translation.py
# Authors: Epic Systems Preternship Team
# Date: April 18, 2021
#
# main logic and functions for translation system
#
############################################################################

import googletrans
#import goslate
import nltk
import json
import string
import pprint
import os


# Split prescription into phrases
# @param    string
# @return   list of separated phrases
def tokenize_prescrip(prescription):
    tokenizer = nltk.tokenize.MWETokenizer([('by', 'mouth'), 
        ('into', 'affected', 'nostril(s)'), ('as', 'instructed'), 
        ('into', 'one', 'nostril'), ('as', 'directed'), ('blood', 'sugar'), 
        ('into', 'affected', 'eye(s)'), ('under', 'the', 'skin'), 
        ('each', 'day'), ('a', 'day'), ('for', 'up', 'to', 'seven', 'days'), 
        ('for', 'pain'), ('with', 'meals'), ('if', 'needed'), 
        ('at', 'bed', 'time'), ('mild', 'pain'), ('for', 'moderate', 'pain'), 
        ('do', 'not', 'crush', 'or', 'chew'), ('for', 'wheezing'), 
        ('for', 'cough'), ('for', 'blood', 'pressure'), 
        ('at', 'the', 'same', 'time'), ('for', 'cholesterol'), 
        ('in', 'the', 'morning'), ('in', 'the', 'evening')])

    punctuation = string.punctuation
    for c in punctuation:
        prescription = prescription.replace(c, "")
    
    words = tokenizer.tokenize(prescription.split());

    return words


# Loop through all phrases in tokenized list
# @param    list of phrases
# @param    source language
# @param    target language
# @return   list of translated phrases
def check_tokenized_phrases(phrases, source, target):

    translated = []

    # open JSON file
    with open(os.path.abspath("Epic_Translation/translation/translation_dict.json"), "r+") as json_file:
        dictionary = json.load(json_file)

    # convert source and target integers to string for JSON
    source = str(source)
    traget = str(target)

    # loop through all phrases
    for phrase in phrases:
        # remove any hyphens before searching
        phrase = phrase.replace("-", "")
        word = find_in_dict(phrase, source, target, dictionary)

        # check if None
        if not word:
            word = call_translate_api(phrase, target)
            # add word into dictionary
            dictionary["extra"][source][phrase] = {target : word}
            # TODO: update file
        
        translated.append(word)

    return translated


# Check if phrase is in dictionary
# @param    string to translate
# @param    string source language
# @param    string target language
# @param    json dictionary
# @return   return translated value
def find_in_dict(phrase, source, target, json_dict):

    # search in dictionary
    for category in json_dict:
        if phrase in json_dict[category][source]:
            translation = json_dict[category][source][phrase][target]
            return translation
        
    return None


# Call translation API if phrase is not found
# @param    string to translate
# @param    integer target language
# @return   return translated value
def call_translate_api(phrase, target):

    if target == 42:
        to_lang = 'EN'
    elif target == 47:
        to_lang = 'FR'
    elif target == 136:
        to_lang = 'ES'
    elif target == 41:
        to_lang = 'NL'
    # default to auto detect
    else:
        to_lang = 'auto'
    
    # call translator api 
    #gs = goslate.Goslate(service_urls=['http://translate.google.com'])
    #translation = gs.translate(phrase, to_lang)
    translation = ""

    return translation


# Concatenate translated words together into one phrase
# @param    list of strings
# @return   translated phrase
def concat_translation(phrases):
    pass


# Prompt user for input
# @return   string phrase to be translated
# @return   int source language
# @return   int target language
def get_input():
    
    phrase = input("Enter prescription message: ")
    source = input("Enter source language (ex: English): ")
    target = input("Enter target language (ex: Spanish): ")

    # match source input with language codes
    source = source.lower()
    if source == "english":
        source = 42
    elif source == "spanish":
        source = 136
    elif source == "dutch":
        source = 41
    elif source == "french":
        source = 47
    else:
        source = 42 
        
    
    # match target input with language codes
    target = target.lower()
    if target == "english":
        target = 42
    elif target == "spanish":
        target = 136
    elif target == "dutch":
        target = 41
    elif target == "french":
        target = 47
    else:
        target = 42

    return phrase, source, target
