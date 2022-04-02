#Le consentement est important!

print("\nSalut et bienvenue!\n")
consentment = input("Une petite partie? ")

if consentment.lower() != "oui":
	quit()
print("Allons-y! \n")

#Données

questionnaire = {
    "question1": ["De quelle couleur est une fraise pour un non-daltonien?  ", "rouge"],
    "question2": ["Qui a dit: 'Mieux vaut dehors que dedans?'  ", "shrek"],
    "question3": ["Dit-on plutôt 'zigouiller' ou 'tuer' dans une réunion de bourgeois? ", "tuer"]
}

#Fonctions

def end_game():
	print("Vous avez " + str(score) + " bonnes réponses sur " + str(questionnaire.len()) + " !")
	if score == numberOfQuestions:
		print("\n Félicitations!")
	else:
		print("Merci d'avoir joué")  # mais vous êtes mauvais..

def main_game(question):
	score = 0
	count = 0
	answer = input(questionnaire[question][0]).lower()
	reponse = questionnaire[question][1]
	while count < 3:
		if answer == reponse:
			print("Bien joué, poulet")
			score += 1
			break
		else:
			print("Mauvaise réponse, il fallait répondre :", reponse)
			break
		count+= 1
	end_game()


main_game("question1")
main_game("question2")
main_game("question3")


