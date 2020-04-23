![](../images/artemis.png)
Section 7: Classes
=====

## Content

### [Subsection 0: Classes](#classes)
> Abstraction at its finest
### [Subsection 1: Exercises](#exercises)
> Exercises to hone your skills

### Classes

Classes are useful for encapsulating a set of operations into a neat package called an object. Lets use a vehicle class for our example. Every vehicle has a set of attributes such as color, year, make, and model. They also have functionality. vehicles can be turned on, drive, and turn off.

```python
class Vehicle:
	running = False
	
	def turnOn(self):
		self.running = True

	def drive(self):
		if self.running:
			print "Vroom!"
		else:
			print "You have to turn the car on first!"

	def turnOff(self):
		self.running = False

camero = Vehicle()
camero.turnOn()
camero.drive()
camero.turnOff()
```

After writing the class we instantiate a vehicle object with the line "camero = Vehicle()", and then use the class functions with the "." operator. But what about the color? Color is very important for a vehicle! This brings me to my next concept: setters and getters.

Setters and getters are functions that allow us to access variables that are scoped to the class. Remember, we can't access variables that aren't in scope! Thats where setters and getters come in. Lets write some:

```python
class Vehicle:
	running = False
	
	def turnOn(self):
		self.running = True

	def drive(self):
		if self.running:
			print "Vroom!"
		else:
			print "You have to turn the car on first!"

	def turnOff(self):
		self.running = False
	
	#### Setters ####
	def setColor(self, color):
		self.color = color

	def setYear(self, year):
		self.year = year

	def setMake(self, make):
		self.make = make

	def setModel(self, model):
		self.model = model
	
	#### Getters ####
	def getColor(self):
		return self.color

	def getYear(self):
		return str(self.year)

	def getMake(self):
		return self.make

	def getModel(self):
		return self.model

# Set up the object
camero = Vehicle()
camero.setColor("Black")
camero.setYear(2013)
camero.setMake("Chevrolet")
camero.setModel("Camero")

# Print the object attributes
print "Make: " + camero.getMake()
print "Model: " + camero.getModel()
print "Year: " + camero.getYear()
print "Color: " + camero.getColor()
```

We can see in the example above how to implement setters and getters. But whats with all the "self" keywords? Self is Python's way of referencing class variables or functions instead of parameter or local functions. Its a scoping thing! It enables us to access variables from outside the funtion that is owned by the class.

So why do I need a class? Well, what if we had multiple vehicles that had different attributes?

```python
import vehicles

camero = Vehicle()
corvette = Vehicle()
camero.turnOn()
camero.drive()
corvette.drive()
```

Obviously we can't drive the corvette without first turning it on! This is how objects are useful. We may have multiple instances (known as objects) of a class that have different attributes or states.

So when you were creating a vehicle object, wasn't it annoying to have to use all those setters to set everything? We can use a function called a constructor to do all the work for us!

```python
class Vehicle:

	def __init__(self, make, model, year, color):
		self.make = make
		self.model = model
		self.year = year
		self.color = color

	#### Getters ####
        def getColor(self):
                return self.color

        def getYear(self):
                return str(self.year)

        def getMake(self):
                return self.make

        def getModel(self):
                return self.model

camero = Vehicle("Chevrolet", "Camero", 2013, "Black")
print camero.getMake()
print camero.getModel()
```

Using the __init__ function, we can create a constructor that takes care of initializing the instantiated object. 

#### Superclasses

Python has an inheritance functionality called "superclasses" in which you can extend the functionality of a class. Take for example: We have a vehicle class now, but what if we wanted to be more specific? We could have a truck class that has attributes only true of trucks, and still use our vehicle class for all other cases.


```python
import vehicle

class Truck(Vehicle):
	def getBedSize(self):
		return "6 foot"

truck = Truck()
print truck.getBedSize()
truck.turnOn()
truck.drive()
```

As you can see, we can still use all of the functions declared in the vehicle class since the truck class inherited them, and have our own unique functions that further fine grain the details on what it means to be a truck!

### Exercises

* Create a class of mammals
	* Make several attributes such as number of legs, habitat, and whether they give life birth
* Create a superclass of animals to extend the attributes (i.e. whale, echidna, or dog)

[Solution](scripts/class.py)

### What you should have learned:

* How to construct classes
* How to extend classes with superclasses

![](../images/floridatech.png)
