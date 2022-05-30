'''
Mortgage Problem (Multi-part)

Part 1

Dave has decided to take out a 30-year fixed rate mortgage of $500,000
with Guido’s Mortgage, Stock Investment, and Bitcoin trading
corporation.  The interest rate is 5% and the monthly payment is
$2684.11. How much does Dave have to pay in total ?

The answer you should get is 966,279.6.

Part 2

Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

When you run the new program, it should report a total payment of `929,965.62` over 342 months.

Part 3

Modify the program so that extra payment information can be more generally handled.
Make it so that the user can set these variables:

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

Make the program look at these variables and calculate the total paid appropriately.

How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first
five years have already been paid?

Part 4

Modify the program to print out a table showing the month, total paid so far, and the remaining principal.
The output should look something like this:

```bash
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total paid 880074.1
Months 310
```

Part 5

While you’re at it, fix the program to correct for the overpayment that occurs in the last month.

'''

#Part 1
def mortgage_p1():
	outstanding = 500000
	monthly_pay = 2684.11
	rate = 0.05/12
	period = 30*12
	total_paid = 0.0
	for i in range(period):
		outstanding = outstanding * (1+rate) - monthly_pay
		total_paid = total_paid + monthly_pay
	print(f"Dave paid a total of {total_paid:.2f}")

#Part 2
def mortgage_p2():
	outstanding = 500000
	monthly_pay = 2684.11
	rate = 0.05/12
	n = 0 
	total_paid = 0.0
	for i in range(12):
		n += 1
		outstanding = outstanding * (1 + rate) - (monthly_pay + 1000)
		total_paid = total_paid + monthly_pay + 1000
	while outstanding > 0:
		n += 1
		outstanding = outstanding * (1 + rate) - monthly_pay
		total_paid = total_paid + monthly_pay
	print(f"Dave paid {total_paid:.2f} over {n} months.")

#Part 3-5
def mortgage_p3():

	extra_payment = float(input("Extra monthly amount?"))
	extra_payment_start_month = int(input("When do you start the extra payment (month)?"))
	extra_payment_end_month = int(input("When do you stop the extra payment (month)?"))
	outstanding = 500000
	monthly_pay = 2684.11
	rate = 0.05/12
	n = 0
	total_paid = 0

	while outstanding > monthly_pay:
		n += 1
		if (n >= extra_payment_start_month) and (n <= extra_payment_end_month):
			monthly_pay = 2684.11 + extra_payment
		else:
			monthly_pay = 2684.11
		outstanding = outstanding * (1 + rate) - monthly_pay
		total_paid = total_paid + monthly_pay
		print(f"{n}. \t {total_paid:.2f} \t {outstanding:.2f}")

	outstanding = outstanding * (1 + rate)
	n += 1
	total_paid = total_paid + (outstanding)
	print(f"{n}. \t {total_paid:.2f} \t 0")
	print("Dave paid","{:.2f}".format(total_paid),"over",n,"months.")

mortgage_p3()