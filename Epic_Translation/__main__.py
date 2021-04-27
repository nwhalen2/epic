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

if __name__ == '__main__':

    prescrip, source, target = translation.get_input()
    tok_strings = translation.tokenize_prescrip(prescrip)
    trans_strs = translation.check_tokenized_phrases(tok_strings, source, target)
    translation.concat_translation(trans_strs)
