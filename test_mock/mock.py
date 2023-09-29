import json
import unittest
from unittest.mock import patch

from pokemon_name_translator import PokemonNameTranslator
from pokemon_report import PokemonReport, config
from pokemon_service import PokemonService

expected_name = "good_pokemon_name"


class PokemonNameTranslatorMock:
    def __init__(self):
        self.client = ""

    def translate(self, *args, **kwargs):
        return expected_name


class TestPokemonNameTranslator(unittest.TestCase):
    @patch('mock.PokemonNameTranslator', PokemonNameTranslatorMock)
    def test_pokemon_name_translator(self):
        expected = expected_name * 3
        pokemon_name_translator = PokemonNameTranslator()
        actual = pokemon_name_translator.translate("abra-kadabra")

        self.assertEqual(expected, actual * 3)


class PokemonReportMock:
    def create_html_report(self, *args, **kwargs):
        return "HTML report"


class TestPokemonReport(unittest.TestCase):

    @patch('mock.config', "")
    @patch('mock.PokemonReport', PokemonReportMock)
    def test_create_html_report(self):
        print(config)
        expected = "HTML report"
        pokemon_info = {"a": 1}
        translated_name = "good_name"
        pokemon_report = PokemonReport()
        actual = pokemon_report.create_html_report(pokemon_info, translated_name)
        self.assertEqual(expected, actual)


class PokemonServiceMock:
    def get_pokemon_info(self, *args, **kwargs):
        dict_1 = {"name": "name1"}
        return json.dumps(dict_1)


class TestPokemonService(unittest.TestCase):

    @patch('mock.PokemonService', PokemonServiceMock)
    def test_get_pokemon_info(self):
        pokemon_name = "good_name"
        pokemon_service = PokemonService()
        pokemon_info = pokemon_service.get_pokemon_info(pokemon_name=pokemon_name)
        self.assertEqual('{"name": "name1"}', pokemon_info)
