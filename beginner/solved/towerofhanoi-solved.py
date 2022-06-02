'''
Tower of Hanoi Problem

In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).

You have the following constraints:

(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk. Write a program to move the disks from the first tower to the
last using Stacks.

The problem can be easily solved using recursion.

Solution:

Recursion is defined by a large task that can be broken down and be represented by an identical but smaller sub tasks. 
We can think of this problem that way. Imagine a tower of 4 total disks, in order to move this tower to the destination tower, 
you must first move the top 3 disks to the spare tower, then move the largest disk to the destination tower, then the top 3 disks to the destination tower. 
In order to move the top 3 disks to the spare tower, we repeat the exact same process again, this is where that recursion occurs. 
You can break this behaviour down until you reach the base case of a tower of one disk (the smallest disk). 
Now substitute 4 disks for n disks, and 3 disks with n-1 disks and you have successfully solved this problem using recursion.

To solve this we use the recursive princpals which are defined as such:

1. Solve the base case of f(1)
2. Assume f(n-1) works
3. Determine the relationship between f(n) and f(n-1)

Now let's try to put this down on paper.

Define a function whose inputs are:

n: number of disks 
source: the tower the original disks are on (in ascending order)
target: the destination tower where the tower will relocate.

For the remainder of this explanation, let us assume,

source tower := tower 1 
spare tower  := tower 2
target tower := tower 3

To begin, we define the base case of n = 1, that is to say "if n == 1", we print the step. 
To visualize the base case, picture 1 disk on tower 1. To move the disk to tower 3, we simply print the step 1 (source) to 3 (target), 
which can be done by initiating the hanoi function with the parameters of hanoi(1,1,3), this will print out 1 -> 3.

Let's take a break and define the spare tower. There are a total of 3 towers, the source, the target, and the other "spare" tower. If we number the tower 1,2,3. 
We can recognize that they will always sum to 6. Therefore, in order to always identify the spare tower. We can subtract the source and target from the sum.
Therefore, before we continue we must first define the spare tower as "spare = 6 - (source + target)"

Next, we must assume this works for the f(n-1) case, that is to say, for n-1 disks. 
Picture 5 total disks on tower 1, we must first move 4 disks to tower 2 in order to move the bottom disk on tower 1 to tower 3. 
This is where the recursive behaviour of the code begins, we perform the function hanoi(n - 1, source, spare) to move n-1 disks to tower 2,
the function will restart with n-1 disks and re-run the logic until n == 1, the one disk. 
Now that the n-1 disks have been moved to the tower 2, you must move the bottom disk on tower 1 to tower 3, 
hence the line "step(source,target)". 

After the bottom disk has moved to tower 3, we must now move the 4 disks on tower 2 to tower 3, to do this we perform the function
hanoi(n-1, spare, target), which moves the n-1 disks from tower 2 to tower 3, completing the problem. 

When you first look at the code and try to wrap your head around recursion, you quickly realize that there a level of "faith" involved. 
It's like a line of dominoes, by knocking over the first domino (f(1) case), determining the relationship between the last 2 dominoes (f(n) and f(n-1)), 
and assuming that the 2nd last domino will indeed fall (f(n-1)), you just have to have faith that the function will do the rest of the work,
that the rest of the dominoes will fall by themselves...

Cheers

'''


def hanoi(n,source,target):
	if n == 1:
		step(source,target)
	else:
		spare = 6 - (source + target)
		hanoi(n - 1, source, spare)
		step(source,target)
		hanoi(n - 1, spare, target)

def step(source,target):
	print(f'{source} -> {target}')
