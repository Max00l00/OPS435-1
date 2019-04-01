#!/usr/bin/env python3

# Store one IPv4 address
class IPAddress:
    # You probably want to construct it as a string, but you may want to store it as the four octets separately:
    def __init__(self, address):
    	self.address = str(address).split('.')
        
    # Is this address from a private subnet? e.g. starting with 192.168. or 10.
    def isPrivate(self):
    	if self.address[0] == '192.168.' or '10.':
    		return True
    	else:
    		return False

# Store information about a person, perhaps someone you'll be adding as a user to a system:
class Person:
	def __init__(self, name):
		self.name = str(name)
		self.userlist = []

	def add_user(self):
		self.userlist.append(self.name)
		return self.userlist   

# Store information about different models from a specific manufacturer. Perhaps how many seats they have and how much fuel they use and the price range:
# Doesn't have to be BMW, pick any car or bike manufacturer:
class BMWModel:
	def __init__(self, model):
		self.model = str(model)
		self.info = {}
		self.info[model] = self.model

	def add_seats(self, seats, number):
		self.info[seats] = int(number)
		return self.info

	def add_fuel(self, fuel, number):
		self.info[fuel] = int(number)
		return self.info

# Store information about a specific car that someone owns.
# Spend some time thinking why this class is different than the one above, and whether it has to be different:
class Car:
	def __init__(self, manufacturer, model, owner):
		self.manufacturer = str(manufacturer)
		self.model = str(model)
		self.owner = str(owner)
	def info(self):
		result = 'Manufacturer: '
		result += self.manufacturer
		result += '\n'
		result += 'Model:',self.model
		result += '\n'
		result += 'Car Owner:',self.owner
		return result