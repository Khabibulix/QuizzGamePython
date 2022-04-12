class Question:
    def __init__(self, titre=str, bonne_reponse=str):
        self.titre = titre
        self.bonne_reponse = bonne_reponse


    def poser(self):
        answer = input(self.titre)
        if answer.lower() == self.bonne_reponse:
            print("Bien joué, poulet")
        else:
            print("Mauvaise réponse, il fallait répondre :", self.bonne_reponse)


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
           if question.poser():
              score += 1
              print(score)
        print("Vous avez " + str(score) + " bonnes réponses sur " + str(len(self.questions)) + " !")
        return score

questions = (
    Question("De quelle couleur est une fraise pour un non-daltonien?  ", "rouge"),
    Question("Qui a dit: 'Mieux vaut dehors que dedans?'  ", "shrek"),
    Question("Dit-on plutôt 'zigouiller' ou 'tuer' dans une réunion de bourgeois? ", "tuer")
)

questionnaire = Questionnaire(questions)



print("\nSalut et bienvenue!\n")
consentment = input("Une petite partie? ")

if consentment.lower() != "oui":
	quit()
print("Allons-y! \n")


questionnaire.lancer()

