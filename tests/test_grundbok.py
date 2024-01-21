"""Stub unit test file."""

import marshmallow_dataclass

from boa.bokforing import Verifikation
from boa.grundbok import Grundbok, GrundbokService


def test_deserialize_empty_grundbok():
    """Test deserialize grundbok."""
    grundbok_schema = marshmallow_dataclass.class_schema(Grundbok)()
    grundbok = grundbok_schema.load({"verifikationer": []})
    assert grundbok_schema.dump(grundbok) == {"verifikationer": []}


def test_deserialize_grundbok():
    """Test deserialize grundbok."""
    grundbok_schema = marshmallow_dataclass.class_schema(Grundbok)()

    raw_grundbok = {
        "verifikationer": [
            {
                "beskrivning": "test",
                "verifikationsnummer": "24",
                "datum": "hej",
                "skapad_av": "Alex",
                "kontering": {
                    "debet": [{"belopp": 100, "kontonummer": 1930}],
                    "kredit": [{"belopp": 100, "kontonummer": 1930}],
                },
                "affärshändelse_datum": "hej",
                "hash": "",
            },
        ],
    }

    grundbok = grundbok_schema.load(raw_grundbok)
    assert grundbok_schema.dump(grundbok) == raw_grundbok


def test_create_grundbok_service():
    """Test create grundbok service."""
    service = GrundbokService()

    service.add_verifikation(
        Verifikation(
            beskrivning="test",
            verifikationsnummer=24,
            datum="hej",
            skapad_av="Alex",
            kontering={
                "debet": [{"belopp": 100, "kontonummer": 1930}],
                "kredit": [{"belopp": 100, "kontonummer": 1930}],
            },
            affärshändelse_datum="hej",
        ),
    )
