'''

Creat your character (name) Problem

Create a program that asks a user for a first name and last name (separately), the program should then display some sort of welcome message to that user's full name. This is an exercise of handling basic string manipulation.

for example:

bash
% What is your first name? 
% >>> John
% What is your last name?
% >>> Doe

% Welcome to hell, John Doe, we hope you enjoy your stay!

Furthermore, the program should be able to handle unclean inputs that have whitespaces or wrong capitalizations:

for example:

bash
% What is your first name?
% >>> [tab space]jOhN [space]
What is your last name?
% >>> [space] dOE [space]

% Welcome to hell, John Doe, we hope you enjoy your stay!

'''

def name():
	first_name = input('What is your first name?')
	last_name = input('What is your last name?')
	print('Welcome to hell,', first_name.strip().capitalize(), last_name.strip().capitalize(),', we hope you enjoy your stay.')

name()