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
