import psycopg2 as pg
from prettytable import PrettyTable
import sys
from datetime import datetime
import string
import re

con = pg.connect(database = "airline", user = "postgres", password = "", host = "", port = "5432")

cur = con.cursor()


#Function for LogIn
def login(email, password): #Edited By Hashaa
        count = 0
	cur.execute("SELECT * FROM CUSTOMER WHERE email = %s" % email)
	rows = cur.fetchall()
	if(password == rows[0][5]):
		print("Welcome!!")
		return True
	else:
		print("password or email is incorrect. Try again.")
		count += 1
		# if they try to login 3 times and they fail, then they are sent back to main()
		if (count == 3)
                        print("Login failed 3 times. Going back to main.")
                        main()
                login()

def passwordReset():	
	new_passWord = input("Enter New Password: ")
	confirm_passWord = input("Enter Password to Confirm: ")

	if(new_passWord == confirm_passWord):
		print("Done!")
	else:
		print("ERROR: Password did not match, Try again ")
		passwordReset()

#Function for Update User Information (Delete | Modify | Add)

def deleteCard(email):
	cur.execute("SELECT CreditCard FROM CREDITCARD WHERE email = '%s'" % (email))
		
	for i in cur.fetchall():
		print (i[0])

	delete_card = raw_input ("Enter creditcard to delete: ")
	cur.execute("DELETE FROM CREDITCARD WHERE CreditCard = '%s'" % (delete_card))
	print("Card Deleted! ")

def updateAddress(email):
	cur.execute("SELECT CreditCard FROM CREDITCARD WHERE email = '%s'" % (email))
		
	for i in cur.fetchall():
		print (i[0])

	update_credit 	= raw_input ("Enter credit  to update address ")
	streetNumber   	= raw_input ("streetNumber: ")
	street  		= raw_input ("steet: ")
	zipcode 		= raw_input ("zipcode: ")


	cur.execute("SELECT streetNumber, street, zipcode FROM ADDRESS WHERE streetNumber = '%s' and street = '%s' and zipcode = '%s'" %(streetNumber,street,zipcode))
	a = cur.fetchall()
	print (a)
	if (a == []):
		cur.execute("INSERT INTO ADDRESS VALUES (%s,%s,%s)",(int(streetNumber), int(zipcode), street))
		conn.commit()
		cur.execute("INSERT INTO LIVEAT  VALUES (%s,%s,%s,%s)",(email, int(streetNumber), int(zipcode), street))
		conn.commit()
			

	cur.execute("SELECT streetNumber, street, zipcode FROM LIVEAT WHERE email = '%s'" % (email))
	needToupdate = 0 
	for i in cur.fetchall():
		print (int(streetNumber),street.strip(),int(zipcode), int(i[0]),str(i[1]).strip(),int(i[2]))
		if (int(streetNumber),street.strip(),int(zipcode)) == (int(i[0]),str(i[1]).strip(),int(i[2])):
			print ("Hello")
			needToupdate = 1


		if (needToupdate == 0):
			cur.execute("INSERT INTO LIVEAT  VALUES (%s,%s,%s,%s)",(email, int(streetNumber), int(zipcode), street))
			conn.commit()
			
		cur.execute("UPDATE  creditCard SET streetNumber = %s , zipcode = %s , street = '%s' WHERE creditcard = %s" % (int(streetNumber), int(zipcode), street, update_credit) ) 
		conn.commit()



def addCard(email):	#Edit By Hashaa
	cur.execute("SELECT CreditCard FROM CREDITCARD WHERE email = '%s'" % (email))
		
	for i in cur.fetchall():
		print (i[0])

	print("Input Payment Information: ")

	card_num = int(input("Enter Card Number: "))
	sec_num = int(input("Enter 3 digit CVV: "))
	card_type = input("Enter Card Type: ")
	exp_date = input("Enter Expiration Date (mm/yy): ")

        cur.execute("INSERT INTO CREDITCARD VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(card_num,sec_num,card_type,exp_date,street_num, zip_code, street_name, email_id))
	
	print("Card Added!")
        conn.commit()

def addAddress(email): # Edit By Hashaa
	print("Input Address Information: ")

	street_num = input("Enter Street Number: ")
	street_name = input("Enter Street Name: ")
	zip_code = input ("Enter Zip Code: ")
                    
        cur.execute("INSERT INTO ADDRESS VALUES (%s,%s,%s)",(int(street_num), int(zip_code), street_name))
        cur.execute("INSERT INTO LIVEAT VALUES (%s,%s,%s,%s)",(email_id, int(street_num), int(zip_code), street_name))
        
        print("Address Added!")
        conn.commit()

#Functions for Flight Search and Booking
def searchFlight(): #Edit by Hashaa, but going with the first one!
        cur = con.cursor()
        
	user_fly = input ("Select from the following option: ")
	return_fly = input("Round Trip [ Y | N ]: ")
	
	# location
        origin = input("Origin: ")
        destination = input("Destination: ")
        # time
        departing_time = input("Departing: ")
        if(return_fly == 'Y'):
                returning_time = input("Returning: ")
        else:
                returning_time = 0
        # advanced options
        classAir  = input("Preferred class: economy or first: ")
        # num_con = input("Enter the number of connections: ") ? Not sure what to do with this because it is in the project description
        
        # show the flights that are available
        print("Searching for Flights...")
        print("Search Results: \n Flight from ", departure, "to ", arrive)

        table = PrettyTable(['Date', 'Airline Code', 'Flight Number'
                                         'Origin Airport', 'Destination Airport'
                                         'Departing Time', 'Returning Time', 'Price'])
        # show the economy flight options
        if (classAir is "economy"):
                cur.execute("SELECT airline_code, flight_number, flight_date, origin, dest, departing_time, returning_time, econ_capacity, econ_price FROM FLIGHT WHERE origin = '%s' and dest = '%s' and class = '%s'and DATE BETWEEN '%s' and '%s'" % (origin, destination, departing_time, returning_time))
        # show the first class flight options
        else:
                cur.execute("SELECT airline_code, flight_number, flight_date, origin, dest, departing_time, returning_time, fc_capacity, fc_price FROM FLIGHT WHERE origin = '%s' and dest = '%s' and class = '%s'and DATE BETWEEN '%s' and '%s'" % (origin, destination, departing_time, returning_time))

        for i in cur.fetchall():
                table.add_row ([str(i[0]),i[1].strip(),i[2],i[3],i[4],str(i[5]),str(i[6]),i[7]])

        print(table)
	
	u_in = input("Do you wish to Go back to Main Menu[ Y | N ]: ")
	if (u_in == 'Y'):
		main()
	else:
		print("Quiting...")
		exit(0)

def book(email):              
        print("Select your ticket: ")

        # the user will search for a flight which will print out all the available flights so here we just book the flight
        # book the flight
        cur.execute("INSERT INTO BOOKING VALUES (%s,%s)", classAir, paymentCard)

def bookingReview(email): # Edit By Hashaa
        cur.execute("SELECT * FROM BOOKING WHERE email = '%s'" % (email))

	# print the flight information
        print("Reviewing flight...")

       table = PrettyTable(['Class', 'Payment Card'])
        
	for i in cur.fetchall():
		print (i[0])
        
	# payment method
	print("Which credit card would you like to use? ")
	# display all the credit cards on the account
        cur.execute("SELECT * FROM CREDIT CARD WHERE email = '%s'" % (email))

        table = PrettyTable(['Card Number', 'Section Number', 'Card Type', 'Expiration Date', 'Payment Address'])

        # FIXME: I don't know how to print out the information from the table right
	for i in cur.fetchall():
		print (i[0])
	

def bookingCancel(email): # Edit by Hashaa
	cur.execute("SELECT * FROM BOOKING WHERE email = '%s'" % (email))
		
	for i in cur.fetchall():
		print (i[0])

	booked_flight = raw_input ("Enter booked flight to cancel: ")
	cur.execute("DELETE FROM BOOKING WHERE id = '%s'" % (booked_flight))
	print("Flight Cancelled! ")


#Function for Registration of New User
def createAccount():
	f_name = input("Enter First Name: ")
	l_name = input("Enter Last Name: ")
	email_id = input("Enter Email: ")
	passWord = input("Enter Password: ")

	addCard(email_id)
        addAddress(email_id)

	#Adding all the input to the database
	cur = con.cursor()
	exp_date = datetime.strptime(str(exp_date),'%m/%y')
	cur.execute("INSERT INTO CUSTOMER   VALUES (%s,%s,%s,%s,%s,%s)", (f_name,'H',l_name,email_id,'ORD',passWord))
	#second address
	#if (secondAddress == "yes"):
					#cur.execute("INSERT INTO ADDRESS    VALUES (%s,%s,%s)",(int(self.streetNumber2), int(self.zipcode2), self.street2))

	print ("Registration is successfully Done")
	conn.commit()

#Main function to recursively call when stuck in error.
def main():
	user = ""
	print("~~~~ Welcome to IIT Flight Reservation System ~~~~~")
	print("Make a selection from the following option: ")
	print("[ L ] Login ")
	print("[ R ] Register New User")
	print("[ F ] Flight Search ")
	print("[ I ] Information about Us")
	print("[ Q ] Quit ")

	user = input("Enter Option: ")
	if(user == 'R'):
				#def for Register
				print("Registration Window: ")
				print("Following the Steps: ")
				createAccount()

	elif(user == 'L'):
		print("Login Window: \n")
		email = input("Enter Email_ID : ")
		password = input("Enter Password: ")

		log = login(email, password)
		
		while True:

			print("Select from the following option: ")
			print("[ E ] Edit Account Information (Add | Delete | Modify)")
			print("[ B ] Book Flight ")
			print("[ R ] Review Flight Booking ")
			print("[ C ] Cancel Flight Booking ")
			print("[ L ] Log Out")

			u_input = input("Enter Option: ")

			

			if(u_input == 'E' or 'e'):

				#Print Edit Information Options
				print("Select from the following option: ")
				print("[ D ] Delete Credit Card ")
				print("[ U ] Update address Information")
				print("[ C ] Add new credit card ")
				print("[ A ] Add new address")
				print("[ M ] Main Menu")

				user_edit = input("Enter Option: ")
				if (user_edit == 'D' or 'd'):
					deleteCard(email)

				elif (user_edit == 'U' or 'u'):
					updateAddress(email)
				
				elif (user_edit == 'C' or 'c'):
					addCard(email)

				elif (user_edit == 'A' or 'a'):
					addAddress(email)

				elif (user_edit == 'M' or 'm'):
					main()

				else: 
					print("ERROR: Invalid Character. Try again. ")
					main()

			elif (u_input == 'S' or 's'):
				searchFlight()

			elif (u_input == 'B' or 'b'):
				book()

			elif (u_input == 'R' or 'r'):
				bookingReview()

			elif (u_input == 'C' or 'c'):
				bookingCancel()

			elif (u_input == 'L' or 'l'):
				print("successfully Logged Out ")
				exit(0)

			else: 
				print("ERROR: Invalid Character. Try again. ")
				main()

	elif(user == 'F'):
	#def for Flight Search
		print("Flight Search Window: ")
		searchFlight()

	elif(user == 'I'):
		print("CS425: Introduction to Database Administration.")
		print("Project By: Jay Patel | Hashaa Otgontulga | Jorell Socorro \n")
		u_in = input("Do you wish to Go back to Main Menu[ Y | N ]: ")
		if(u_in == 'Y'):
			main()
		else:
			exit(0)


	elif(user == 'Q'):
		print("Quiting..")
		#Quit

	else:
		print("ERROR: Invalid Character. Try again. ")
		main()


	con.close()



main()
