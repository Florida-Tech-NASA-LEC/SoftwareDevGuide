![](../images/artemis.png)
Section 3: Strings
=====

## Content

### [Subsection 0: Strings](#strings)
> How to work with strings in Python
### [Subsection 1: Exercises](#exercises)
> Exercises to hone your skills

### Strings

Strings are very similar to tuples in that they are immutable. You'll notice that you can assign a value to a string, and then reassign a different value to the same string. Isn't that proving strings are mutable? Well, no. Whats meant by immutability is that you can't index inside of the string and change a value.

> exampleString = "ThisIsAString"

Strings are sliceable just like tuples and lists.

#### String Methods

Below are some important functions for handling strings that you may encounter with your senior design project.

##### join

Join is useful when you're trying to catonate a list or tuple of strings together. See the example below:

> car = ["Ford", "Ranger"]<br>
> makeModel = " ".join(car)<br>
> print makeModel
> 
> Ford Ranger

We can see how we are joining the two elements together with a space between them.

##### replace

Since strings are immutable, we need a function that will take a string and look for all instances of a character or word and replace that with whatever we desire. How can we do this if strings are immutable? Python is creating a new string from the old string. It looks like this:

> msg = "Hello World!"<br>
> newmsg = msg.replace("Hello", "Goodbye")<br>
> print newmsg
>
> Goodbye World!

We can see how the first operand of the replace function is the string we wish to replace, and the second operand is the string we wish to repalce it with.

##### split

Split is useful when you have several words in a string that you want to split into elements of an array. Sometimes you do this to isolate a specific word. Lets leapfrog off the previous example. What if you wanted to print only one of the words in the string "Goodbye world"?

> wordList = newmsg.split(" ")
> print wordList[0]
>
> Goodbye

First, we split the newmsg string by a space. Next, we print the list created by the split and only select index 0, which is "Goodbye"

### Exercises

* Given the following string, replace every word "woodchuck" with "NASA"
	* myString = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
* Now, split the string and join all instances of "NASA" together with a space between each instance

[Solution](scripts/string.py)

### What you should have learned:

* How to work with strings
* How to replace certain characters or words in a string
* How to split strings to isolate specific parts

![](../images/floridatech.png)
