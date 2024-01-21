"""Stub unit test file."""

import marshmallow_dataclass

from boa.bokforing import Verifikation


def test_verifikation():
    """Test deserialize verifikation."""
    verifikation_schema = marshmallow_dataclass.class_schema(
        Verifikation)()
    verifikation1 = verifikation_schema.load(
        {"beskrivning": "test",
         "verifikationsnummer": "v24",
         "datum": "hej",
         "skapad_av": "Alex",
         "kontering": {"debet": [{"belopp": 100, "kontonummer": 1930}],
                       "kredit": [{"belopp": 100, "kontonummer": 1930}]},
         "affärshändelse_datum": "hej"})

    verifikation2 = verifikation_schema.load(
        {"beskrivning": "test",
         "datum": "hej",
         "verifikationsnummer": "v24",
         "skapad_av": "Alex",
         "kontering": {
             "kredit": [{"belopp": 100, "kontonummer": 1930}],
             "debet": [{"belopp": 100, "kontonummer": 1930}],
         },
         "affärshändelse_datum": "hej"})
    assert verifikation_schema.dump(
        verifikation1) == verifikation_schema.dump(verifikation2)
