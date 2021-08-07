#!/usr/bin/env python

"""
call_profit.py

Author: Sean-Michael Woerner
08/06/2021

Program that calculates profit, loss, breakeven point, and other data facts of buying a call option on the stock market.
"""

#Imports
from os import system, name 
import math 
import numpy as np
import matplotlib.pyplot as plt


####################################################################################	
#Globals
####################################################################################
portfolio_count = 0
portfolio_list = [] #list of lists

####################################################################################	
#Methods
####################################################################################	
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def boot():
    clear()
    print("\n")
    print("*************************************************")
    print("*              CALL OPTION STUFF                *")
    print("*        author: Sean-Michael Woerner           *")
    print("*************************************************")


def menu():
	print("\nMAIN MENU\n---------\n(1) Calculate profit, loss, and break-even point of a call\n---------------------------------\n(0) Exit Program\n")
	
# Get data of User's call and save for later use
def call_info():
	clear()
	print("Please enter the following: <strike price> <amount of calls purchased> <price per call>")
	data = input()
	
	temp = data.split()
	strike = float(temp[0])
	call_amount = float(temp[1])
	call_price = float(temp[2])
	breakeven = float(strike) + float(call_price)
	breakeven_format = "{:.2f}".format(breakeven) 
	
	#put data of the call into a list that can be appended to the portfolio list
	call_data = [strike, call_amount, call_price, breakeven]
	premium = float(100 * (call_price * call_amount))
	premium_format = "{:.2f}".format(premium)  
	

	print("\n**************************************************************")
	print("CALL DATA")
	print("------------------")
	print("Break-Even price: $"+str(breakeven_format))
	print("Premium paid: $"+str(premium_format))
	
	print("|*********************************|")
	print("|      POTENTIAL PROFIT           |")
	print("|*********************************|")
	print("| Final Price   |    Profit       |")
	print("|*********************************|")

	for x in range(35):
	
		# Increment each iteration by 10% (the first iteration by just 1 % to get past breakeven)
		if x == 0:
			final_price = breakeven * 1.01 
		else:
			final_price *= 1.1
		# Calculate profit and then format price for printing 	
		profit = (final_price - strike - call_price)*(call_amount*100)
		profit_format = "{:.2f}".format(profit)  
		final_price_format = "{:.2f}".format(final_price)  
		print("| $"+str(final_price_format)+"        |    $"+str(profit_format))
	
	print(input("\nPress ENTER to return..."))
	clear()
	
	
####################################################################################	
# MAIN
####################################################################################
boot()
while True:	
	menu()
	choice = input()
	
	if choice == '1':
		call_info()
	if choice == '0':
		exit()

	#clear()
	
	


