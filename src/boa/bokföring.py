from dataclasses import dataclass
from typing import TypeAlias

Konto: TypeAlias = int
Summa: TypeAlias = float
Kontohändelse: TypeAlias = tuple[Konto, Summa]


@dataclass
class Verifikationer:
    """# Verifikationer

    En verifikation fungerar som ett bevis för en finansiell transaktion. Den följer principerna för dubbel bokföring
    där debiteringar och krediteringar balanseras. För varje affärshändelse ska det finnas en verifikation.

    Args:
        id (int): Unikt identifieringsnummer för verifikationen.
        verifikationsnummer (int): Verifikationsnummer eller annat identifikationstecken för att sammankoppla verifikationen med den bokförda händelsen.
        datum (str): Datum när verifikationen upprättades.
        beskrivning (str): Beskrivning av affärshändelsen.
        skapadAv (str): Namnet på den som skapade verifikationen.
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
    id: int
    verifikationsnummer: int
    datum: str
    beskrivning: str
    skapadAv: str
    affärshändelse_datum: str
    debiteringar: list[Kontohändelse]
    krediteringar: list[Kontohändelse]
