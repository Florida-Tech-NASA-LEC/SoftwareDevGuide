![](../images/artemis.png)
Section 8: Exceptions
=====

## Content

### [Subsection 0: Exceptions](#exceptions)
> How to recover gacefully from errors
### [Subsection 1: Exercises](#exercises)
> Exercises to hone your skills

### Exceptions

Exceptions exist to give the programmer more control over the error states of the application. Lets say we were creating a program that would perform integer division in a loop and we wanted the user to remain in the program until they wanted to exit:

```python

def integerDivision(m, n):
	try:
		return m / n
	except ZeroDivisionError:
		print "Denominator cannot be zero!"

while True:
	m = raw_input("Numerator: ")
	n = raw_input("Denominator: ")
	if m == "999" or n == "999":
		break
	print integerDivision(int(m), int(n))
```

In the example above, if a ZeroDivisionError is encountered, the application catches it and prints an error message before returning to the loop to get the values for the next calculation. Note: the ZeroDivisionError is specific to division by zero exceptions. If you want a catch-all exception handling, omit the ZeroDiisionError keyword and it will catch any and all exceptions. Sometimes you may need to handle different types of exceptions differently, however.

Exceptions aren't very complicated, but they can be useful sometimes. There is more on exceptions but I won't cover it here since its fairly easy, and you likely wont need to do much more than this with exceptions.

### Exercises

* Create a script that catchesi and handles an exception
	* Force a condition that causes an exception, such as concatenating a string and an integer together

[Solution](scripts/exception.py)

### What you should have learned:

* How to handle errors in your program gracefully

![](../images/floridatech.png)
