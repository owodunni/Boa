"""Stub unit test file."""

from boa.bokforing import Verifikationer

import marshmallow_dataclass


def test_adder():
    """Test the adder function."""
    verifikationer_schema = marshmallow_dataclass.class_schema(
        Verifikationer)()
    verifikationer1 = verifikationer_schema.load(
        {"beskrivning": "test",
         "verifikationsnummer": 24,
         "datum": "hej",
         "skapad_av": "Alex",
         "kontering": {"debet": [{"belopp": 100, "kontonummer": 1930}],
                       "kredit": [{"belopp": 100, "kontonummer": 1930}]},
         "affärshändelse_datum": "hej"})

    verifikationer2 = verifikationer_schema.load(
        {"beskrivning": "test",
         "datum": "hej",
         "verifikationsnummer": 24,
         "skapad_av": "Alex",
         "kontering": {
             "kredit": [{"belopp": 100, "kontonummer": 1930}],
             "debet": [{"belopp": 100, "kontonummer": 1930}],
         },
         "affärshändelse_datum": "hej"})
    assert verifikationer_schema.dump(
        verifikationer1) == verifikationer_schema.dump(verifikationer2)
