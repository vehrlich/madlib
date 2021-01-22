from urllib.parse import urljoin
from django.conf import settings
import requests


class GlitchService:
    def fetch_word(self, word_type: str):
        url = urljoin(settings.GLITCH_URL, settings.GLITCH_ROUTES[word_type])

        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def get_adjective(self):
        return self.fetch_word(settings.GLITCH_ADJECTIVE)

    def get_verb(self):
        return self.fetch_word(settings.GLITCH_VERB)

    def get_noun(self):
        return self.fetch_word(settings.GLITCH_NOUN)

    def get_all(self):
        return self.get_adjective(), self.get_verb(), self.get_noun()


glitch_service = GlitchService()


