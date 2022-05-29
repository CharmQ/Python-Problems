'''
Bounce Problem

A rubber ball is dropped from a height of 100 meters and each time it
hits the ground, it bounces back up to 3/5 the height it fell. Write
a program that prints a table showing the height of the first 10 bounces.

As an additional challenge, round all answers to 4 decimal places using "%0.2f" % (num,)
'''

def bounce_problem(bounce_factor, height):
    print("Bounce\tHeight")
    for i in range (10):
        height *= bounce_factor
        print(i+1, "\t{arg:.4f}".format(arg=height))

bounce_problem(0.6, 100)
