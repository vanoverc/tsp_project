import sys

class City:
    def _init_(self):
        self.name = None
        self.xCoord = None
        self.yCoord = None

def readInput(fileName, cities):
    inputFile = open(fileName, "r")
    newCity = 1    # Indicates the City attribute to store the input line
    currentCity = City()    # City object to hold the current City being read from file
    # Loop through each line in the file
    for line in inputFile:
	# Remove the newline character
	line = line[0:-1]
	# Store the line the appropriate City attribute
	if newCity == 1:
	    currentCity.name = line
	    newCity = newCity + 1	# Increment input attribute value
	elif newCity == 2:
	    currentCity.xCoord = line
	    newCity = newCity + 1	# Increment input attribute value
	else:
	    currentCity.yCoord = line
	    newCity = 1
	    someCity = City()     # New City object to hold the values read from file 
	    someCity.name = currentCity.name
	    someCity.xCoord = currentCity.xCoord
	    someCity.yCoord = currentCity.yCoord
	    cities.append(someCity)    # Add the city to cities array
    inputFile.close()

someCities = []
readInput(sys.argv[1], someCities)

# Test to confirm input read properly
#for nextCity in someCities:
#    print(nextCity.name)
#    print(nextCity.xCoord)
#    print(nextCity.yCoord)


