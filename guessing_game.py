#Created by: Michael Taylor
#Created on: October 2, 2017
#Created for ICS3U
#This program is a number guessing game 

import ui

CORRECT_ANSWER = 5

def check_answer_button(sender):
	#checks if user input equals CORRECT_ANSWER
	
	user_guess = int(view['user_guess_input'].text)
	
	if user_guess == CORRECT_ANSWER:
		view['output_text'].text = 'Correct!'
	else:
		view['output_text'].text = 'Incorrect!'

view = ui.load_view()
view.present('sheet')
