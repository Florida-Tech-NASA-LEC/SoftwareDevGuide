![](../images/artemis.png)
Section 5: Conditionals and Loops
=====

## Content

### [Subsection 0: Conditionals](#conditionals)
> Basic decision making
### [Subsection 1: Loops](#loops)
> How to run the same code n times
### [Subsection 2: Exercises](#exercises)
> Exercises to hone your skills

### Conditionals

Conditionals are truely what make a program smart. In order to have some sort of decision making, we need conditionals. If x happens, do y. If z is not this, then do this. For those of you who have done any sort of programming before, this should come easy.

Up to this point, you really havent had to indent too much. The biggest complaint of Python stems from errors those new to Python receive: indentation errors. Essencially, all blocks must be indented the same way. For instance, some people indent with two spaces. Some people use four spaces. For me, I use tab. If you mix these indentation styles in the same script, you get indentation errors.

Conditionals rely on block indentation. Here is an example of this:

```python
name = "Joshua Connolly"
if "Josh" in name:
	print "Close enough!"
else:
	print "Not even close!"
```

See how any code that goes inside the if/else is indented? That is how Python determines if something belongs to that block.

One nice thing about Python conditionals is the "if this in that" structure, similar to the example above. As you can see, you can have the conditional pass on less stringent conditions. Or you could do like this:

```python
name = "Josh"
if name == "Joshua Connolly":
	print "Way too formal!"
elif name == "Josh C"
	print "Last initial? Really?"
else:
	print "Yep, thats my name!"
```

Notice in the example above the elif statement. In Python, else if is elif. They had to be special.

### Loops

Loops are where programs begin to take on a lot of awesome functionality, and also get complicated very quickly. It is important to think about the functionality of the program before you start creating nested loops with break statements, returns, and other function calls. It gets messy very quickly.

#### While loops

While loops are the simplest loop there is. While some condition is being met, do some action UNTIL that condition is no longer met. So what happens if the condition is never met? That is what we call an infinite loop. Sometimes we want an infinite loop though! What if we were building a server and we wanted it to listen for connections foreever? An infinite loop would be appropriate!

```python
while(True):
	print "infinite loop!"
```

But its rare we want to make an infinite loop. Here is an example of a more legitimate use of a while loop:

```python
textFile = open('file.txt', 'r')	# Open a text file
data = textFile.read(1024)		# Read 1024 bytes of data
while(data):				# Loop until no more data
	socket.send(data)		# Send the data across the network
	data = textFile.read(1024)	# Get the nexy 1024 bytes of data
```

This example is a little more advanced than previous examples, but it certainly illustrates the point. The loop continues until there is no more data left in the file that was read in.

#### For loops

For loops are just fancy while loops. Change my mind. But seriously, here is what I mean:

For loop example:
```python
for x in range(0, 10):
	print x
```

While loop acting like a for loop
```python
x = 0
while(x < 10):
	print x
	x += 1
```

But in Python, for loops are a little cooler. For instance, we can do this:

```python
ports = [21, 25, 80, 443, 1337]
for port in ports:
	print port
```

In the example above instead of using an index to iterate over the values of an array like we would in C or C++, we can use the list itself as the value and Python just KNOWS how many values to print. How wild is that?

#### Break and continue

Normally, you'd design your loops to exit whenever the contition you set for them is encountered, however, sometimes things are not so simple. I've been told it is bad coding practice to use break statements to exit from loops, however, I disagree. That is literally their intended purpose, and sometimes you need to break from the loop without finishing the rest of the iterations. Consider a sorting algorithm:

```python
# Implement a sorting algorithm that stops sorting through the gross food after it finds the tacos!
foods = ["Broccoli", "Kale", "Brussel Sprouts", "Sardines", "Tacos", "Eggplant"]

for food in foods:
	if food == "Tacos":
		print "horray, Tacos!"
		break
	print "Yuck, " + food + "."
```

If you run the code above, you'll notice that it never prints out any message with eggplant in it. Thats because the loop exits before it finishes iterating through the list. Dodged that bullet (the eggplant)!

Continue statements are similar to break statements except they don't break out of the loop completely, but instead end the current iteration of the loop and begin at the next iteration without executing any remaining code in that block. Lets look at a similar example:

```python
# Search for tacos!
foods = ["Broccoli", "Kale", "Brussel Sprouts", "Sardines", "Tacos", "Eggplant"]

for food in foods:
        if food == "Tacos":
                print "horray, Tacos!"
        print "Yuck, " + food + "."
```

The example above is flawed, because there is no continue statement after we find the tacos. This results in a print statement of "horray, Tacos!" followed by a "Yuck, Tacos.", and I definitely do not agree with that. This program needs to be patched! So by putting in a continue statement, we will allow the loop to coninue to run (to hopefully find more tacos in the list) while skipping the rest of the code in the loop.

```python
# Search for tacos! version 2.0 (No more yuck for tacos!)
foods = ["Broccoli", "Kale", "Brussel Sprouts", "Sardines", "Tacos", "Eggplant"]

for food in foods:
        if food == "Tacos":
                print "horray, Tacos!"
		continue
        print "Yuck, " + food + "."
```

### Exercises

* Create a program that has a list of subteams for your team
* Loop over all of the subteams, printing the name of the team + " is cool!"
* If "software" subteam is encountered, print " is VERY cool!"

[Solution](scripts/loop.py)

### What you should have learned:

* How to create conditions to dictate control flow
* How to iterate over items or number of loops

![](../images/floridatech.png)
