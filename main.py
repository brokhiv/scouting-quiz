from typing import List, Tuple
import os
import platform
from time import sleep

questions: List[Tuple[str, str]] = [
    ("Hoeveel jaar bestaat de St. Joris Scouts?",
     "90"),
    ("Geef de voornamen van de 7 scoutsleiding, in alfabetische volgorde en gescheiden met een spatie.",
     "Chris Ilona Ivo JJ Nienke Richard Thijs"),
    ("Hoe heet de kachel in de blokhut?",
     "Brutus"),
    ("Wat moet je als eerste aanzetten als je wilt koken in de keuken?",
     "Afzuigkap"),
    ("Waar zijn we in 2010 op Zomerkamp geweest?",
     "Groenlo"),
    ("Welk merk bijlen hebben wij?",
     "Fiskars"),
    ("Welke bloem staat symbool voor Scouting, en is veel terug te vinden in de blokhut?",
     "Franse Lelie"),
    ("Welke dieren kunnen aan de achterkant van de blokhut een onderkomen vinden?",
     "Vleermuizen"),
    ("Waar vertrok de trein naar een 'betoverend' kamp? Gebruik de naam op het aandenken.",
     "Platform 9 3/4"),
    ("Hoeveel banken staan er in de blokhut?",
     "6"),
]

if __name__ == '__main__':
    while True:
        incomplete = True
        while incomplete:
            os.system('cls' if platform.system() == 'Windows' else 'clear')

            print("Welkom bij de St. Joris Scouts quiz!")
            print(f"Beantwoord de volgende {len(questions)} vragen om de aanwijzing te krijgen.")
            print()
            print("Als je een vraag fout beantwoordt, moet je helemaal opnieuw beginnen.")
            print("Hoofdletters zijn niet belangrijk, maar let op de spelling.")
            print("Wanneer een getal gevraagd wordt, schrijf dit dan in cijfers.")
            print("Let op: de toetscombinatie Ctrl+C werkt niet in dit programma en sluit het volledig af.")
            print("Veel succes!")
            print()
            for question, answer in questions:
                user_answer = input(question + " ")
                user_answer = user_answer.strip()
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    print()
                else:
                    print("Fout! Begin maar helemaal opnieuw.")
                    sleep(2)
                    break
            else:
                incomplete = False
        print("Gefeliciteerd! Je hebt alle vragen goed beantwoord. Jullie aanwijzing is:")
        print()
        print("Je hoeft niet verder te zoeken in de blokhut, want de Bloedvlag ligt op een andere plek.")
        print()
        print("Druk op enter om af te sluiten.")
        input()
