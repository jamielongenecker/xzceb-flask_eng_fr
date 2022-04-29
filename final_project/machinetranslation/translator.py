import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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
def english_to_french(englishText):
    """
    This function translates English to French
    """
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()

    return frenchText

# french to english translator
def french_to_english(frenchText):
    """
    This function translates French to English
    """
    englishText = language_translator.translate(
        text=frenchText,
        model_id='en-fr'
    ).get_result()

    return englishText