###########################################################################
# 
# translation.py
# Authors: Epic Systems Preternship Team
# Date: April 18, 2021
#
# Main logic and functions for translation system
#
############################################################################

from google_trans_new import google_translator
import nltk
import json
import string
import pprint
import os


# Split prescription into phrases
# @param    string prescription
# @return   list of separated phrases
def tokenize_prescrip(prescription):
    tokenizer = nltk.tokenize.MWETokenizer([('by', 'mouth'), 
        ('into', 'affected', 'nostrils'), ('as', 'instructed'), 
        ('into', 'one', 'nostril'), ('as', 'directed'), ('blood', 'sugar'), 
        ('into', 'affected', 'eyes'), ('under', 'the', 'skin'), 
        ('each', 'day'), ('a', 'day'), ('for', 'up', 'to'), 
        ('for', 'pain'), ('with', 'meals'), ('if', 'needed'), 
        ('at', 'bed', 'time'), ('for', 'mild', 'pain'), 
        ('for', 'moderate', 'pain'), 
        ('do', 'not', 'crush', 'or', 'chew'), ('for', 'wheezing'), 
        ('for', 'cough'), ('for', 'blood', 'pressure'), 
        ('at', 'the', 'same', 'time'), ('for', 'cholesterol'), 
        ('in', 'the', 'morning'), ('in', 'the', 'evening'),
        ('por', 'vía', 'oral'), ('por', 'vía', 'tópica'), 
        ('en', 'los', 'orificios', 'nasales', 'afectados'), 
        ('según', 'las', 'instrucciones'),
        ('en', 'un', 'orificio', 'nasal'), ('como', 'se', 'indica'),
        ('el', 'nivel', 'de', 'azúcar', 'en', 'la', 'sangre'), 
        ('en', 'los', 'ojos', 'afectados'), ('al', 'día'), ('una', 'vez'),
        ('por', 'hasta', '7', 'días'), ('en', 'total'), 
        ('para', 'el', 'dolor'), ('con', 'la', 'comida'), 
        ('si', 'es', 'necesario'), ('al', 'acostarse'),
        ('para', 'el', 'dolor', 'leve'), ('para', 'el', 'dolor', 'moderado'),
        ('no', 'triture', 'ni', 'mastique'), ('para', 'sibilancias'), 
        ('para', 'la', 'tos'), ('a', 'la', 'misma', 'hora'), 
        ('el colesterol'), ('para', 'la', 'presión', 'arterial')])

    punctuation = string.punctuation
    for c in punctuation:
        prescription = prescription.replace(c, "")

    # convert to lowercase to make case insensitive
    prescription = prescription.lower()
    
    words = tokenizer.tokenize(prescription.split());

    return words


# Loop through all phrases in tokenized list
# @param    list of phrases
# @param    int source language
# @param    int target language
# @return   list of translated phrases
def check_tokenized_phrases(phrases, source, target):

    translated = []

    # open JSON file
    with open(os.path.abspath("Epic_Translation/translation/translation_dict.json"), "r") as read_json:
        dictionary = json.load(read_json)

    # convert source and target integers to string for JSON
    source = str(source)
    target = str(target)

    # loop through all phrases
    for phrase in phrases:

        # skip numbers
        if phrase.isdigit():
            translated.append(phrase)
            continue

        # remove any hyphens before searching
        phrase = phrase.replace("_", " ")

        word = find_in_dict(phrase, source, target, dictionary)

        # if multiple translations, default to the first one 
        if type(word) == list:
            word = word[0]

        # check if not found in dictionary
        if not word:
            word = call_translate_api(phrase, target)

            # add word into dictionary
            dictionary["extra"][source][phrase] = {target : word}

            # update JSON file
            with open(os.path.abspath("Epic_Translation/translation/translation_dict.json"), "w") as write_json:
                json.dump(dictionary, write_json, indent = 4, ensure_ascii=False)
        
        translated.append(word)

    return translated


# Check if phrase is in dictionary
# @param    string to translate
# @param    string source language
# @param    string target language
# @param    json dictionary
# @return   string translated value
def find_in_dict(phrase, source, target, json_dict):

    # search in dictionary
    for category in json_dict:
        if phrase in json_dict[category][source]:
            translation = json_dict[category][source][phrase][target]
            return translation
        
    return None


# Call translation API if phrase is not found
# @param    string to translate
# @param    string target language
# @return   string translated value
def call_translate_api(phrase, target):
    
    if target == "42":
        to_lang = 'en'
    elif target == "47":
        to_lang = 'fr'
    elif target == "136":
        to_lang = 'es'
    elif target == "41":
        to_lang = 'nl'
    # default to spanish target
    else:
        to_lang = 'es'
    
    # call translator api
    translator = google_translator()
    translate_text = translator.translate(phrase, lang_tgt=to_lang)
    # default to first translation
    if type(translate_text) == list:
        translate_text = translate_text[0]
    translate_text = translate_text.lower().rstrip()

    return translate_text


# Concatenate translated words together into one phrase
# @param    list of strings
# @return   translated phrase
def concat_translation(phrases):
    
    translation = ""

    for idx, word in enumerate(phrases):
        # capitalize first word
        if idx == 0:
            word = word.title()

        translation += word

        # add spaces in between each word
        if idx != len(phrases) - 1:
            translation += " "
        # add ending punctuation
        else:
            translation += "."

    return translation


# Prompt user for input
# @return   string phrase to be translated
# @return   int source language
# @return   int target language
def get_input(phrase, source, target):
    
    #phrase = input("Enter prescription message: ")
    #source = input("Enter source language (ex: English): ")
    #target = input("Enter target language (ex: Spanish): ")

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
        target = 136

    return phrase, source, target
