import psycopg2 as pg
from prettytable import PrettyTable
import sys
from datetime import datetime
import string
import re
import random
import networkx as nx

print("~~~~ Welcome to IIT Flight Reservation System ~~~~~")
con = pg.connect(database = "airline", user = "postgres", password = "", host = "", port = "")

cur = con.cursor()

#Function for undirected flights
def undirectedFlight():
        print("You are at:"+nx.center(g))
        print("Where do you wanna go?")
        place = raw_input("FL1,FL2,FL3,FL4,FL5")
        seeAll = raw_input("Or see all Distances, type:'all'")
        g = nx.Graph()
        g.name = "FlightPath"
        #These are flight samples
        ###
        g.add_node("FlightCenter")
        g.add_node("FlightLocation1")
        g.add_node("FlightLocation2")
        g.add_node("FlightLocation3")
        g.add_node("FlightLocation4")
        g.add_node("FlightLocation5")
        ###
        #These are edges
        ###
        g.add_edge("FlightLocation1","FlightLocation3")
        g.add_edge("FlightCenter","FlightLocation1")
        g.add_edge("FlightCenter","FlightLocation5")
        g.add_edge("FlightLocation5","FlightLocation2")
        g.add_edge("FlightLocation5","FlightLocation4")
        ###
        #Return the distance from Center
        ###
        if(place == "FL1"):
                return g.degree("FlightLocation1")
        elif(place == "FL2"):
                return g.degree("FlightLocation2")
        elif(place == "FL3"):
                return g.degree("FlightLocation3")
        elif(place == "FL4"):
                return g.degree("FlightLocation4")
        elif(place == "FL5"):
                return g.degree("FlightLocation5")
        elif(seeAll == "all"):
                return g.degree()
        ###
#Function for LogIn
def login(email, password):
	cur.execute("SELECT * FROM CUSTOMER WHERE email = '%s' " % email)
	rows = cur.fetchall()
	if(password == rows[0][5]):
		print("Welcome!!")
		return True
	else:
		print("password or email is incorrect. Try again.")
		main()

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

	delete_card = raw_input ("Enter creditcard to delete ")
	cur.execute("DELETE FROM CREDITCARD WHERE CreditCard = '%s'" % (delete_card))
	print("Card Deleted! ")

def updateAddress(email):
	cur.execute("SELECT CreditCard FROM CREDITCARD WHERE email = '%s'" % (email))
		
	for i in cur.fetchall():
		print (i[0])

	update_credit 	= raw_input ("Enter credit to Update: ")
	street_num  	= raw_input ("streetNumber: ")
	street_name  	= raw_input ("steet: ")
	zip_code 		= raw_input ("zipcode: ")


	cur.execute("SELECT streetNumber, street, zipcode FROM ADDRESS WHERE streetNumber = '%s' and street = '%s' and zipcode = '%s'" %(street_num,street_name,zip_code))
	a = cur.fetchall()
	print (a)
	if (a == []):
		cur.execute("INSERT INTO ADDRESS VALUES (%s,%s,%s)",(int(street_num), int(zip_code), street_name))
		con.commit()
		cur.execute("INSERT INTO LIVEAT  VALUES (%s,%s,%s,%s)",(email, int(street_num), int(zip_code), street_name))
		con.commit()
			

	cur.execute("SELECT streetNumber, street, zipcode FROM LIVEAT WHERE email = '%s'" % (email))
	needToupdate = 0 
	for i in cur.fetchall():
		print (int(street_num),street_name.strip(),int(zip_code), int(i[0]),str(i[1]).strip(),int(i[2]))
		if (int(street_num),street_name.strip(),int(zip_code)) == (int(i[0]),str(i[1]).strip(),int(i[2])):
			needToupdate = 1


		if (needToupdate == 0):
			cur.execute("INSERT INTO LIVEAT  VALUES (%s,%s,%s,%s)",(email, int(street_num), int(zip_code), street_name))
			con.commit()
			

		cur.execute("UPDATE  creditCard SET streetNumber = %s , zipcode = %s , street = '%s' WHERE creditcard = %s" % (int(street_num), int(zip_code), street_name, update_credit) ) 
		con.commit()



def addCard(email):
	print("Input Payment Information: ")

	email_id = email
	card_num = int(input("Enter Card Number: "))
	sec_num = int(input("Enter 3 digit CVV: "))
	card_type = input("Enter Card Type: ")
	exp_date = input("Enter Expiration Date (mm/yy): ")

	print("Input Address Information: ")

	street_num = input("Enter Street Number: ")
	street_name = input("Enter Street Name: ")
	zip_code = input ("Enter Zip Code: ")

	cur = con.cursor()
	exp_date = datetime.strptime(str(exp_date),'%m/%y')
	cur.execute("INSERT INTO ADDRESS    VALUES (%s,%s,%s)",(int(street_num), int(zip_code), street_name))
	cur.execute("INSERT INTO CREDITCARD VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(card_num,sec_num,card_type,exp_date,street_num, zip_code, street_name, email_id))
	con.commit()
	print("CreditCard is successfully added")

def addAddress(email):
	print("Input Address Information: ")

	email_id = email
	street_num = input("Enter Street Number: ")
	street_name = input("Enter Street Name: ")
	zip_code = input ("Enter Zip Code: ")

	#Adding all the input to the database
	cur = con.cursor()

	cur.execute("INSERT INTO ADDRESS    VALUES (%s,%s,%s)",(int(street_num), int(zip_code), street_name))
	cur.execute("INSERT INTO LIVEAT 	VALUES (%s,%s,%s,%s)",(email_id, int(street_num), int(zip_code), street_name))
	print ("Address is successfully added")
	con.commit()
	main()

#Functions for Flight Search and Booking
def searchFlight(email, password):
	print("Select from the following option: ")

	departure = input("Departure Airport: ")
	arrive	  =	input("Arrival Airport: ")
	classAir  = input("seats: economy or first: ")
	return_Fly = input("Round Trip [ Y | N ]: ")
	cur = con.cursor()

	# print("Searching for Flights...")
	# print("Search Results: \n Flight from ", departure, "to ", arrive)
	
	# table = PrettyTable(['Date', 'Airline Code', 'Flight Number',
	# 					 'Departure Airport', 'Arrival Airport',
	# 					 'Departure Time', 'Arrival Time', 'Price'])

	# cur.execute("SELECT dateoffilght,airlinecode,flight_number,iata,arrives_fromiata,departuretime,arrivaltime,amount FROM FLIGHT NATURAL JOIN price WHERE iata = '%s' and arrives_fromiata = '%s' and class = '%s'" % (departure,arrive,classAir))

	# #3print (cur.fetchall())
	# for i in cur.fetchall():
	# 	table.add_row ([str(i[0]),i[1].strip(),i[2],i[3],i[4],str(i[5]),str(i[6]),i[7]])

	# print(table)

	if(return_Fly == 'Y'):
		print("Searching for Flights...")
		print("Search Results: \n Flight from ", departure, "to ", arrive)

		table = PrettyTable(['Date', 'Airline Code', 'Flight Number',
						 'Departure Airport', 'Arrival Airport',
						 'Departure Time', 'Arrival Time', 'Price'])

		cur.execute("SELECT dateoffilght,airlinecode,flight_number,iata,arrives_fromiata,departuretime,arrivaltime,amount FROM FLIGHT NATURAL JOIN price WHERE iata = '%s' and arrives_fromiata = '%s' and class = '%s'" % (departure,arrive,classAir))
		for i in cur.fetchall():
			table.add_row ([str(i[0]),i[1].strip(),i[2],i[3],i[4],str(i[5]),str(i[6]),i[7]])

		print(table)

	elif(return_Fly == 'N'):
		print("Searching for Flights...")
		print("Search Results: \n Flight from ", departure, "to ", arrive)
	
		table = PrettyTable(['Date', 'Airline Code', 'Flight Number',
						 'Departure Airport', 'Arrival Airport',
						 'Departure Time', 'Arrival Time', 'Price'])

		cur.execute("SELECT dateoffilght,airlinecode,flight_number,iata,arrives_fromiata,departuretime,arrivaltime,amount FROM FLIGHT NATURAL JOIN price WHERE iata = '%s' and arrives_fromiata = '%s' and class = '%s'" % (departure,arrive,classAir))

		
		for i in cur.fetchall():
			table.add_row ([str(i[0]),i[1].strip(),i[2],i[3],i[4],str(i[5]),str(i[6]),i[7]])

		print(table)

	u_in = input("Do you wish to Go back to Main Menu[ Y | N ]: ")
	if(u_in == 'Y'):
		login(email, password)
	else:
		print("Quiting...")
		exit(0)

def book(email, password):
	booking_email = email.split("@")
	book_ID = booking_email[0] + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))

	round_trip = input ("Round Trip [ Y | N ]: ")
	round_trip = None

	round_trip = 1 if (round_trip == 'one way') else 1

	for b in range(round_trip):
		print (b)
		flight 			= input ("Enter Flight Number: ")
		classFlight 	= input ("Enter Class [ economy | first ]: ")
		dateoffilght 	= input ("Enter Date(mm/dd/yy): ")
	
		flight 		 = flight.split(" ")
		dateoffilght = datetime.strptime(str(dateoffilght),'%m/%d/%Y')

		cur.execute("SELECT CreditCard FROM CREDITCARD WHERE email = '%s'" % (email))
		for i in cur.fetchall():
			print (i[0])


		if (b == 0):
			creditcardUSE = input ("Select CreditCard to use:  ")
			cur.execute("INSERT INTO BOOKING VALUES (%s,%s,%s)", (book_ID,email,creditcardUSE))
			con.commit()
				
			#cur.execute("INSERT INTO INCLUDES VALUES (%s,%s,%s,%s,%s)", (book_ID,classFlight,flight[1],flight[0],dateoffilght.date()))
		
			con.commit()
	

	print("Your Booking was successfully processed: \n Your Confirmation Code ", book_ID," paid from ", creditcardUSE)


	u_in = input("Do you wish to Go back to Main Menu[ Y | N ]: ")
	if(u_in == 'Y'):
		login(email, password)
	else:
		print("Quiting...")
		exit(0)

def bookingCancel(email, password):
	print("Works!")

def bookingReview(email, password):
	print("Works!")

#Function for Registration of New User
def createAccount():
	f_name = input("Enter First Name: ")
	l_name = input("Enter Last Name: ")
	email_id = input("Enter Email: ")
	passWord = input("Enter Password: ")

	print("Input Payment Information: ")

	card_num = int(input("Enter Card Number: "))
	sec_num = int(input("Enter 3 digit CVV: "))
	card_type = input("Enter Card Type: ")
	exp_date = input("Enter Expiration Date (mm/yy): ")

	print("Input Address Information: ")

	street_num = input("Enter Street Number: ")
	street_name = input("Enter Street Name: ")
	zip_code = input ("Enter Zip Code: ")

	#Adding all the input to the database
	cur = con.cursor()
	exp_date = datetime.strptime(str(exp_date),'%m/%y')
	cur.execute("INSERT INTO CUSTOMER   VALUES (%s,%s,%s,%s,%s,%s)", (f_name,'H',l_name,email_id,'ORD',passWord))
	cur.execute("INSERT INTO ADDRESS    VALUES (%s,%s,%s)",(int(street_num), int(zip_code), street_name))
	cur.execute("INSERT INTO CREDITCARD VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(card_num,sec_num,card_type,exp_date,street_num, zip_code, street_name, email_id))
	cur.execute("INSERT INTO LIVEAT 	VALUES (%s,%s,%s,%s)",(email_id, int(street_num), int(zip_code), street_name))
	print ("Registration is successfully Done")
	con.commit()
	main()

#Main function to recursively call when stuck in error.
def main():
	user = ""
	
	print("Make a selection from the following option: ")
	print("[ L ] Login ")
	print("[ R ] Register New User")
	print("[ F ] Flight Search ")
	print("[ I ] Information about Us")
	#New###
	print("[ G ] Go fly")
	#New###
        print("[ Q ] Quit ")
	user = input("Enter Option: ")
	if(user == 'R'):
				#def for Register
				print("Registration Window: ")
				print("Following the Steps: ")
				createAccount()
#NEW###
	elif(user == 'G'):
                #User Travel Distance
                print("Where do you want to go??")
                undirectedFlight()
#NEW###
	elif(user == 'L'):
		print("Login Window: \n")
		email = input("Enter Email_ID : ")
		password = input("Enter Password: ")

		log = login(email, password)

		while True:

			print("Select from the following option: ")
			print("[ E ] Edit Account Information (Add | Delete | Modify)")
			print("[ S ] Search Flights ")
			print("[ B ] Book Flight ")
			print("[ R ] Review Flight Booking ")
			print("[ C ] Cancel Flight Booking ")
			print("[ L ] Log Out")

			u_input = input("Enter Option: ")

			

			if(u_input == 'E'):

				#Print Edit Information Options
				print("Select from the following option: ")
				print("[ D ] Delete Credit Card ")
				print("[ U ] Update address Information")
				print("[ C ] Add new credit card ")
				print("[ A ] Add new address")
				print("[ M ] Main Menu")

				user_edit = input("Enter Option: ")
				if (user_edit == 'D'):
					deleteCard(email)

				elif (user_edit == 'U'):
					updateAddress(email)
				
				elif (user_edit == 'C'):
					addCard(email)

				elif (user_edit == 'A'):
					addAddress(email)

				elif (user_edit == 'M'):
					main()

				else: 
					print("ERROR: Invalid Character. Try again. ")
					main()

			elif (u_input == 'S'):
				searchFlight(email, password)

			elif (u_input == 'B'):
				book(email, password)

			elif (u_input == 'R'):
				bookingReview(email, password)

			elif (u_input == 'C'):
				bookingCancel(email, password)

			elif (u_input == 'L'):
				print("successfully Logged Out ")
				exit(0)

			else: 
				print("ERROR: Invalid Character. Try again. ")
				main()


	elif(user == 'F'):
	#def for Flight Search
		print("Flight Search Window: ")
		searchFlight(email, password)

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













































