"""# Grundbok

Grundboken innehåller alla verifikationer som företaget har gjort. Verifikaten
ska kunna presenteras i kronologisk ordning både efter när affärshändelsen gjordes,
samt i ordningen de bokfördes. Det ska också vara möjlight att se om bokföringen
har ändrats efter att den gjordes.

För att åstadkomma detta behöver vi en datastruktur som kan hålla reda på verifikationerna
samt ett sätt att verifiera att bokföringen inte har ändrats.

Vi kommer använda oss av ett [merkletree](https://en.wikipedia.org/wiki/Merkle_tree)
för att verifiera att bokföringen inte har ändrats.
Genom att hålla reda på root-noden i trädet när olika verifikationer läggs till kan vi
skapa [consistency proofs](https://transparency.dev/verifiable-data-structures/)
som kan användas för att granska bokföringen i efterhand.
"""

from dataclasses import dataclass, field

from boa.bokforing import Verifikation


@dataclass
class VerifikationWithHash(Verifikation):
    """# VerifikationWithHash

    En verifikation med en hash som används för att verifiera att verifikationen inte har ändrats.
    """

    hash: str = field(default_factory=str)

class Grundbok:
    """# Grundbok

    hello
    """

    verifikationer: list[VerifikationWithHash] = field(default_factory=list)
