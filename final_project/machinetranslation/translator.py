"""
English to French and French to English Translator
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('t14RuSg7QkhQN8y8R77q0nw4_K2KCVkivOOAXpvzSIVA')
language_translator = LanguageTranslatorV3(
    version='2023-01-13',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):

    """
    This function translates English to French.
    """

    if not english_text:
        return None

    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']

    return french_text


def french_to_english(french_text):

    """
    This function translates French to English.
    """

    if not french_text:
        return None

    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']

    return english_text
