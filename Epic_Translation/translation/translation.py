###########################################################################
# 
# translation.py
# Authors: Epic Systems Preternship Team
# Date: April 18, 2021
#
# main logic and functions for translation system
#
############################################################################

from . import translation_dict
import pydeepl
import nltk

print("running translation.py")

# Split prescription into phrases
# @param    string
# @return   list of separated phrases
def tokenize_prescrip(prescription):
    pass


# Check if phrase is in dictionary
# @param    string to translate
# @param    integer source language
# @param    integer target language
# @param    translation dictionary
# @return   return translated value
def find_in_dict(phrase, source, target, dictionary):

    # search in dictionary
    if false:
        pass
    # call translation api
    else:
        translation = call_translate_api(dictionary, phrase, target)
        # place new word in 'extra' category


# Call pydeepl API if phrase is not found
# @param    string to translate
# @param    integer target language
# @return   return translated value
def call_translate_api(phrase, target):

    if target == 42:
        to_lang = "EN";
    elif target == 47:
        to_lang = "FR"
    elif target == 136:
        to_lang = "ES"
    elif target == 41:
        to_lang = "NL"
    # default to auto detect
    else:
        to_lang = "auto"
    
    # call pydeepl api w/ auto translation
    translation = pydeepl.translate(phrase, to_lang)

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
