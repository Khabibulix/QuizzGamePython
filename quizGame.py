#Le consentement est important!
print("\nSalut et bienvenue!\n")
consentment = input("Une petite partie? ")

if consentment.lower() != "oui":
	quit()
print("Allons-y! \n")

#Main game

score = 0
numberOfQuestions = 3

#1
answer = input("De quelle couleur est une fraise pour un non-daltonien?  ").lower()
if (answer == "rouge"):
	print("Bien joué, poulet")
	score += score
else:
	print("Mauvaise réponse, il fallait répondre : rouge")

#2
answer = input("Qui a dit: 'Mieux vaut dehors que dedans?'  ").lower()
if (answer == "shrek"):
	print("Bien joué, poulet")
	score += score
else:
	print("Mauvaise réponse, il fallait répondre : Shrek")

#3
answer = input("Dit-on plutôt 'zigouiller' ou 'tuer' dans une réunion de bourgeois? ").lower()
if (answer == "tuer"):
	print("Bien joué, poulet")
	score += score
else:
	print("Mauvaise réponse, il fallait répondre : tuer")

#Endgame

print("Vous avez " +str(score)+ " bonnes réponses sur " +str(numberOfQuestions) +" !")
if score == numberOfQuestions:
	print("\n Félicitations!")
else:
	print("Merci d'avoir joué")#mais vous êtes mauvais...