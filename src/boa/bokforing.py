"""# Bokföring

Dataklasser för att representera bokföringsinformation.
"""
from dataclasses import asdict, dataclass, field
from typing import Self

import marshmallow.validate


@dataclass
class KonteringsPost:
    """# KonteringsPost

    En konteringspost är en postering på ett konto. Den kan vara en debitering
    eller en kreditering.

    Args:
    ----
        belopp (float): Beloppet konteringsposten innehåller.
        kontonummer (int): Kontonumret som konteringsposten ska bokföras på.

    """

    belopp: float = field(
        metadata={"validate": marshmallow.validate.Range(min=0)})
    kontonummer: int = field(
        metadata={"validate": marshmallow.validate.Range(min=0)})


@dataclass
class Kontering:
    """# Kontering

    Att fördela affärshändelser på olika konton kallas för kontering.
    En kontering har två sidor, en debet och en kredit. Debet är vänstersidan
    och kredit är högersidan.

    Summan av debet och kredit måste vara lika.

    Args:
    ----
        debet (list[KonteringsPost]): En lista av konteringsposter som ska debiteras.
        kredit (list[KonteringsPost]): En lista av konteringsposter som ska krediteras.

    """

    debet: list[KonteringsPost] = field(default_factory=list)
    kredit: list[KonteringsPost] = field(default_factory=list)


@dataclass
class Verifikation:
    """# Verifikation

    En verifikation fungerar som ett bevis för en finansiell transaktion. Den följer principerna för dubbel bokföring
    där debiteringar och krediteringar balanseras. För varje affärshändelse ska det finnas en verifikation.

    Args:
    ----
        verifikationsnummer (int): Verifikationsnummer eller annat identifikationstecken för att sammankoppla verifikationen med den bokförda händelsen.
        datum (str): Datum när verifikationen upprättades.
        beskrivning (str): Beskrivning av affärshändelsen.
        skapad_av (str): Namnet på den som skapade verifikationen.
        affärshändelse_datum (str): Datum när affärshändelsen inträffade.
        debiteringar (list[Kontohändelse]): En lista av kontohändelser som representerar debiteringar på verifikationen.
        krediteringar (list[Kontohändelse]): En lista av kontohändelser som representerar krediteringar på verifikationen.

    ## Lagkrav

    - **Sporbarhet:** Verifikationer måste vara spårbara och kopplade till sina käll-dokument för revisionsändamål.
    - **Noggrannhet:** Informationen på verifikationen måste korrekt återspegla den finansiella transaktionen den representerar.
    - **Tidstämplar:** Varje verifikation bör inkludera transaktionsdatum för att etablera en kronologisk ordning av händelser.
    - **Auktorisation:** Verifikationer måste auktoriseras av ansvariga individer inom organisationen för att säkerställa ansvarsskyldighet.
    - **Efterlevnad:** Efterlevnad av svensk bokföringslag (Bokföringslagen) är väsentlig. Detta inkluderar korrekt klassificering av konton och överensstämmelse med redovisningsstandarder.

    ## Syfte

    - **Revisionspår:** Verifikationer fungerar som en vital del av revisionspåret, vilket gör det möjligt för revisorer att verifiera noggrannheten och fullständigheten av finansiella poster.
    - **Finansiell rapportering:** Data från verifikationer används för att generera finansiella rapporter och ge en översikt över organisationens ekonomiska hälsa.

    ## Arkivering

    - Verifikationer bör behållas under en specifik period, enligt svensk lag, för att underlätta revisioner och inspektioner.

    """

    verifikationsnummer: str
    datum: str
    beskrivning: str
    skapad_av: str
    affärshändelse_datum: str
    kontering: Kontering

    def dict(self: Self) -> dict:
        """Returnera verifikationen som en dictionary."""
        return {k: str(v) for k, v in asdict(self).items()}
