
def intro():
    print("\nSalut et bienvenue!\n")
    consentment = input("Une petite partie? ")

    if consentment.lower() != "oui":
        quit()
    print("Allons-y! \n")


class Question:
    SCORE = 0
    def __init__(self, titre=str, bonne_reponse=str):
        self.titre = titre
        self.bonne_reponse = bonne_reponse


    def poser(self):
        answer = input(self.titre)
        if answer.lower() == self.bonne_reponse:
            print("Bien joué, poulet")
            Question.SCORE += 1
        else:
            print("Mauvaise réponse, il fallait répondre :", self.bonne_reponse)


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        for question in self.questions:
            question.poser()
        print("Vous avez " + str(Question.SCORE) + " bonnes réponses sur " + str(len(self.questions)) + " !")

    def get_score(self):
        score = 0
        return score


questions = (
    Question("De quelle couleur est une fraise pour un non-daltonien?  ", "rouge"),
    Question("Qui a dit: 'Mieux vaut dehors que dedans?'  ", "shrek"),
    Question("Dit-on plutôt 'zigouiller' ou 'tuer' dans une réunion de bourgeois? ", "tuer")
)

questionnaire = Questionnaire(questions)

intro()
questionnaire.get_score()
questionnaire.lancer()
