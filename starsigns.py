# Prompt the user to enter a month, continue while input is not valid 
while True:
	month = raw_input("Enter a month: ");
	# Convert to lowercase and capitalize first letter
	month = month.lower().capitalize();
	# Depending on the month set a different max value and break out of loop
	if month == "February":
		max = 29;
		break;
	elif month in ["April", "June", "September", "November"]:
		max = 30;
		break;
	elif month in ["January", "March", "May", "July", "August", "October", "December"]:
		max = 31;
		break;
	else:
		print("Please enter a valid month");
# Prompt the user to enter a date for the month, continue while input is either not valid or not in the range 
while True:
	date = raw_input("Enter a number between 1 and {} : ".format(max));
	try:
		# Cast to an integer
		date = int(date);
		# Check that number is between 1 and max, if so break out of loop 
		if date < 1:
			print("Please enter a number greater than zero");
		elif date > max:
			print("Please enter a number no greater than {}".format(max));
		else:
			break;
	except:
		print("Please enter a number");
# Print the full date
print("%(date)d %(month)s " % {"date": date, "month": month});

# Dictionary for each star sign and the dates it falls between
starsigns = {
"Aries": ("March 21", "April 19"), 
"Taurus": ("April 20", "May 20"), 
"Gemini": ("May 21", "June 20"), 
"Cancer": ("June 21", "July 22"),
"Leo": ("July 23", "August 22"),
"Virgo": ("August 23", "September 22"),
"Libra": ("September 23", "October 22"),
"Scorpio": ("October 23", "November 21"), 
"Sagittarius": ("November 22", "December 21"),
"Capricorn": ("December 22", "January 19"),
"Aquarius": ("January 20", "February 18"),
"Pisces": ("February 19", "March 20")
};

# Index variable to store the current index while iterating
index = 0;
# Loop through each value in the dictionary
for v in list(starsigns.values()):
	# Each value has a start and end date so join them together into a list and then split them to seperate string
	values = ', '.join(v).split(',');
	# If the first value starts with the month input then get the final two characters which are the date
	if values[0].strip().startswith(month):
		num = int(values[0][-2:]);
		# If it is greater than or equal to the date input then print the star sign for the current index
		if date >= num:
			print(list(starsigns)[index]);
	# If the second value starts with the month input then get the final two characters which are the date 
	elif values[1].strip().startswith(month):
		num = int(values[1][-2:]);
		# If it is less than or equal to the date input then print out the star sign for the current index
		if date <= num:
			print(list(starsigns)[index]);
	# Increment index
	index = index + 1;			
			