"""
This file contains methods for translating from
English-to-French and French-to-English
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Connect to translator service
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# english to french translator
def english_to_french(english_text):
    """
    This function translates English to French
    """
    if english_text is None:
        return None
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    translation = french_text['translations'][0]['translation']

    return translation

# french to english translator
def french_to_english(french_text):
    """
    This function translates French to English
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    translation = english_text['translations'][0]['translation']

    return translation
