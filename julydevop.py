"""Python Write a python script with the above name which does the following:


	
initialises a list which contains the FIRST NAME of all 21 people in this cohort
	using the .append() function add me to the list
	print the 5th person in the list (this is a trick question, what is special about the way Python indexes?)
	print the number of Chris in the cohort

Once you have a solution, remember to push it to github.
"""

fname = ["Tobi", "Jacob", "Josh", "Chris", "Chris", "Sam", "Tembi", "Arsalan", "Wasim", "Ed", "John", "Dom", "Jack", "Amanda",
         "Clifford", "Mohamed", "Javas", "Ryan", "Jason", "Bradley", "Steven"]

print("First Name: ", fname)

fname.append("Luke")
print("New List: ", fname)

print("5th name in list(index 4 as count from 0):", fname[4])

chris = fname.count("Chris")
print("Chris appears", chris, "times.")
