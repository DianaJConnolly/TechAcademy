'''
Diana Connolly
dianasgame.py
requires gModule.py

My take on the Nice or Mean tutorial
This game randomly chooses from a list of quests and scores response. Will run 5 times, output result,
and give user chance to continue or quit.

These were the program requirements:
	Get user input,
	Use functions that require parameters,
	Use functions that call other functions,
	Loop game until game is over,
	Give user option of playing again or quitting.
'''
import gModule

def main():
	#set up variables:
	again = True
	name = ""
	prevQuest = []
	quest = []
	action = ""
	score = 0
	loop = 5
	reset = []

	while again == True:
		for i in range(5): #repeat 5 times before asking for repeat play
			name = gModule.getName(name)
			quest = gModule.getQuest(prevQuest)
			action = gModule.getAction(quest, name)
			score = gModule.getScore(action, quest, score)
		gModule.outputResult(name, score)
		reset = gModule.goAgain(again, name, score, prevQuest)
		again = reset[0]
		score = reset[1]
		prevQuest = reset[2]


# The if __name__ == "__main__":  clause provides for 2 scenarios:
#	1. If __name__ is the executing file, the driver code is called and the program executes. 
#	2. If __name__ is the NOT executing file (e.g. when this file (and includes) have been imported), 
#	the functions are imported but the driver function does not execute. 
# (I wrote this all up cause I was all WTF? and wanted to understand, 
# the bottom line is I don't really need it for this assignment, but it's a good practice.)
if __name__ == "__main__":
	main()	#driver function for dianasGame