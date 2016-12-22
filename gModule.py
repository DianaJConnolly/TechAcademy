# GModule.py
# required by dianasGame.py
from random import randint

def getName(name): #if name is empty string, get it and return name
	if name == "":
		name = raw_input("\nWhat is your name? ").capitalize()
		print "Hi {} ! Let's see what kind of person you are!".format(name)
	return name

def getQuest(prevQuest):
	scenarios = [ #scenarios[0] is the score if yes, scenarios[1] is score if no, scenarios[2] is quest
		[3, -1, "gaze in awe at the sky?"],
		[3, -1, "be friendly if someone bumped into you?"],
		[4, -2, "go for a hike with a friend that's too broke to go to the club?"],
		[4, -2, "give a dollar to a homeless person?"],
		[5, -3, "help a neighbor move?"],
		[5, -3, "adopt an orphan kitten?"],
		[-3, 1, "hide the cookies?"],
		[-3, 1, "squash a spider?"],
		[-4, 2, "step on a bug?"],
		[-4, 2, "curse a bad driver?"],
		[-5, 3, "ignore a friend's text?"],
		[-5, 3, "leave the scene if no one saw you bump and dent a car with yours?"]]
	i = randint(0,11)
	while i in prevQuest: # the probablility that we'll get a previously used quest is too high, so:
		i = randint(0,11) # get a quest not used before in current game
	prevQuest.append(i)
	quest = [scenarios[i][0], scenarios[i][1], scenarios[i][2]]
	return quest

def getAction(quest, name):
	print ("\n{}, Would you".format(name)),
	print (quest[2])
	action = raw_input( "yes/no: ").lower()
	return action

def calcScore(action, quest, score):
	if action == "y" or action == "yes":
		score += quest[0]
	else:
		score += quest[1]
	return score

def outputResult(name, score): #scores can range from -25 .. 25
	judgements = [
		"Stay away from me, you seem dangerous!!!!",
		"Maybe you should relax a little and not be such a turd.",
		"I might hang around with you, on a good day!",
		"You seem fun and normal!",
		"Wow, you are oozing with superhuman niceness!"]
	if score >= -25 and score < -16:
		j = judgements[0]
	if score >= -16 and score < -4:
		j = judgements[1]
	if score >= -4 and score < 5:
		j = judgements[2]
	if score >= 5 and score < 16:
		j = judgements[3]
	if score >= 16 and score <= 25:
		j = judgements[4]
	print "\n{},".format(name),
	print j
	print "Your score was " + str(score) + " on a scale of -25 to 25."

def goAgain(again, name, score, prevQuest):
	loop = raw_input( "\nWant to try again?: yes/no: ").lower()
	if loop == "n" or loop == "no":
		again = False
		print "\nGoodbye, {}!\n".format(name)
	else:
		score = 0
		prevQuest = []
		print "\nAlright, {}! Let's go again!".format(name)
	return [again, score, prevQuest]

