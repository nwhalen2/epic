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
# @return   if found, return translated value; else return empty string
def find_in_dict(phrase, source, target, dictionary):

    # search in dictionary

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
        to_lang = auto
    
    # call pydeepl api w/ auto translation
    translation = pydeepl.translate(phrase, to_lang)

    return translation


# Concatenate translated words together into one phrase
# @param    list of strings
# @return   translated phrase
def concat_translation(phrases):
    pass
