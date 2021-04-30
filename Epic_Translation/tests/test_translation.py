#
#############################################################################
# 
# test_translation.py
#
# Authors: Epic Systems Preternship Team
# Date:    April 20, 2021
#
# test_translation.py provides unit tests to check the accuracy of the
# translation script as compared to the sample data.
# 
###############################################################################

from .context import translation
from translation import translation as tr
import os
import json
import unittest


class TestTranslationMethods(unittest.TestCase):
    '''Test translation methods'''

    def test_call_api(self):
        phrase = tr.call_translate_api("as directed", "ES")
        self.assertEqual(phrase, "como se indica")
        phrase = tr.call_translate_api("como se indica", "EN")
        self.assertEqual(phrase, "as directed")

    def test_tokenize_prescrip(self):
        phrase = "Take 1 tablet by mouth"
        tokenized = tr.tokenize_prescrip(phrase)
        self.assertEqual(tokenized, ["Take", "1", "tablet", "by_mouth"])
        
        phrase = "Apply 1 application topically 2 (two) times a day."
        tokenized = tr.tokenize_prescrip(phrase)
        self.assertEqual(tokenized, ["Apply", "1", "application", "topically", "2",
            "two", "times", "a_day"])
        
        phrase = "Take 1 capsule (400 mg total) by mouth every 6 (six) hours if needed for mild pain for up to 7 days."
        tokenized = tr.tokenize_prescrip(phrase)
        self.assertEqual(tokenized, ["Take", "1", "capsule", "400", "mg",
            "total", "by_mouth", "every", "6", "six", "hours", "if_needed", "for", 
            "mild_pain", "for_up_to", "7", "days"])

    def test_check_tokenized_phrases(self):
        phrase = "Apply 1 application topically 2 (two) times a day."
        tokenized = tr.tokenize_prescrip(phrase)
        translated = ["aplique", "1", "aplicación", "por vía tópica", "2", "dos",
                "veces", "al día"]
        test_phrases = tr.check_tokenized_phrases(tokenized, 42, 136)
        self.assertEqual(translated, test_phrases)

        phrase = "Take 1 capsule (400 mg total) by mouth every 6 (six) hours if needed for mild pain for up to 7 days."
        tokenized = tr.tokenize_prescrip(phrase)
        test_phrases = tr.check_tokenized_phrases(tokenized, 42, 136)
        translated = ["tome", "1", "cápsula", "400", "mg", "en total", "por vía oral",
                      "cade", "6", "seis", "horas", "si necesario", "7", "días"]
        print(test_phrases)
        #self.assertEqual(translated, test_phrases)

    # def test_eng_to_esp_words(self):
        # self.assertEqual('method call', 'expected result')

    # def test_esp_to_eng_words(self):
        # self.assertEqual('method call', 'expected result')

    # def test_eng_to_esp_sentence(self):
        # self.assertEqual('method call', 'expected result')
    
    # def test_esp_to_eng_sentence(self):
        # self.assertEqual('method call', 'expected result')
    
    # def test_api_translation(self):
        # self.assertEqual('method call', 'expected result')

    def test_find_in_dict(self):
        with open(os.path.abspath("Epic_Translation/translation/translation_dict.json"), "r") as fh:
            dictionary = json.load(fh)

        translation = tr.find_in_dict("apply", "42", "136", dictionary)
        self.assertEqual(translation, "aplique")
        
        translation = tr.find_in_dict("days", "42", "136", dictionary)
        self.assertEqual(translation, "días")

        translation = tr.find_in_dict("by mouth", "42", "136", dictionary)
        self.assertEqual(translation, "por vía oral")

        translation = tr.find_in_dict("as directed", "42", "136", dictionary)
        self.assertEqual(translation, "como se indica")

        translation = tr.find_in_dict("para la tos", "136", "42", dictionary)
        self.assertEqual(translation, "for cough")

        translation = tr.find_in_dict("para el colesterol", "136", "42", dictionary)
        self.assertEqual(translation, "for cholesterol")
        
        translation = tr.find_in_dict("aplicación", "136", "42", dictionary)
        print(translation)
        self.assertEqual(translation, "application")
if __name__ == '__main__':
    unittest.main()
