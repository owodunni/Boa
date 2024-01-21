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
from typing import Self

from boa.bokforing import Verifikation


@dataclass
class VerifikationWithHash(Verifikation):
    """# VerifikationWithHash

    En verifikation med en hash som används för att verifiera att verifikationen inte har ändrats.
    """

    hash: str

class GrundbokError(Exception):
    """# GrundbokException

    Ett undantag som kastas när något går fel i grundboken.
    """

@dataclass
class Grundbok:
    """# Grundbok

    hello
    """

    verifikationer: list[VerifikationWithHash] = field(default_factory=list)

    def add_verifikation(self: Self, verifikation: VerifikationWithHash) -> None:
        """Lägg till en verifikation i grundboken.

        Args:
        ----
            verifikation (VerifikationWithHash): Verifikationen som ska läggas till i grundboken.
        """
        self.verifikationer.append(verifikation)

class GrundbokService:
    """# GrundbokService

    Service för att hantera grundboken.
    """

    def __init__(self: Self) -> Self:
        """Skapa en ny grundboksservice.

        Args:
        ----
            grundbok (Grundbok): Grundboken som ska hanteras.
        """
        # TODO: Läs in grundboken från filsystemet
        # TODO: Setup merkletree and use it to get the root hash
        self.grundbok = Grundbok()

    def add_verifikation(self: Self, verifikation: Verifikation) -> None:
        """Lägg till en verifikation i grundboken.

        Args:
        ----
            verifikation (Verifikation): Verifikationen som ska läggas till i grundboken.
        """
        # TODO: Verify that the verifikation is valid
        d = verifikation.dict()
        # TODO: Get the hash from the merkletree
        d["hash"] = ""
        # TODO: Save the grundbok to the filesystem
        self.grundbok.add_verifikation(VerifikationWithHash(**d))

    def get_verifikation(self: Self, verifikationsnummer: int) -> VerifikationWithHash:
        """Hämta en verifikation från grundboken.

        Args:
        ----
            verifikationsnummer (int): Verifikationsnumret för verifikationen som ska hämtas.

        Returns:
        -------
            Verifikation: Verifikationen som hittades.
        """
        for verifikation in self.grundbok.verifikationer:
            if verifikation.verifikationsnummer == verifikationsnummer:
                return verifikation

        err = "Verifikatione hittades inte"
        raise GrundbokError(err)
