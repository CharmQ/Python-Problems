'''
Dollar Bill Problem

Suppose the following:
One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago.
Each day thereafter, you go out and double the number of bills.
>How long does it take for the stack of bills to exceed the height of the tower?
>How many bills are in the stack
>What is the final height of the stack

Solution:
We first determine the height (thickness) of the dollar bill, then determine the height of the chicago tower.

'''

dollar_bill_thickness = float(input('What is your bill\'s thickness in mm'))*0.001 #in meters (mm * m/mm)
tower_height = float(input('What is the height of the tower in meters')) #in meters

def dollar_to_tower(thk,h):
	day = 1
	bill_height = thk
	while bill_height < h:
		bill_height = bill_height*2
		day = day + 1
	print('It would take',day,'days for the stack of bill of',thk*1000,'mm thickness to exceed a',h,'m tower.')
	print('There are',bill_height/thk,'bills in the stack')
	print('The final height of the stack is',bill_height)

dollar_to_tower(dollar_bill_thickness,tower_height) # comment added by the ZUK