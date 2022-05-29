'''
Bounce Problem

A rubber ball is dropped from a height of 100 meters and each time it
hits the ground, it bounces back up to 3/5 the height it fell. Write
a program that prints a table showing the height of the first 10 bounces.

As an additional challenge, round all answers to 4 decimal places using "%0.2f" % (num,)
'''

def drop():
	h = float(input("What is the height of the ball?")) #in meters
	n = int(input("How many bounces will it do?")) #number of bounces
	for i in range(1,n+1):
		h = h*0.6
		h_format = "{:.2f}".format(h)
		print(i,".", "\t",h_format)

drop()



