'''
Dollar Bill Problem

Suppose the following:
One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago.
Each day thereafter, you go out and double the number of bills.
>How long does it take for the stack of bills to exceed the height of the tower?
>How many bills are in the stack
>What is the final height of the stack

Solution:
We will create a function that takes the input of the bill thickness from the user (in mm) and the height of any given building/tower/object (in m).
The function initiates a while loop the enumerates a counter (variable: day) and doubles the stack of the bills every loop. The while loop will break once the
stack of the bills exceed the height of the tower, then prints the answer to the user.

'''

dollar_bill_thickness = float(input('What is your bill\'s thickness in mm'))*0.001 #in meters (mm * m/mm)
tower_height = float(input('What is the height of the tower in meters')) #in meters

def dollar_to_tower(thk,h):
	day = 1 #start on day 1
	bill_height = thk #takes the input and sets it as bill_height
	while bill_height < h: #while loop that ends when bill_height exceeds height of the tower, h
		bill_height = bill_height*2
		day = day + 1
	print('It would take',day,'days for the stack of bill of',thk*1000,'mm thickness to exceed a',h,'m tower.')
	print('There are',bill_height/thk,'bills in the stack')
	print('The final height of the stack is',bill_height)

dollar_to_tower(dollar_bill_thickness,tower_height)