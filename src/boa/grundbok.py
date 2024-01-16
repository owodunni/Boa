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


class Grundbok:
    """# Grundbok

    hello
    """
