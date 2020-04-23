![](../images/artemis.png)
Section 6: Functions
=====

## Content

### [Subsection 0: Functions](#functions)
> Abstraction at its finest
### [Subsection 1: Exercises](#exercises)
> Exercises to hone your skills

### Functions

Ever felt like you were writing the same code multiple times? You could most definitely just write that once as a function. Programmers are inherently lazy. We rely on technology for many things, and we want everything to be efficient. It only makes sense that functions exist so that we don't have to rewrite code multiple times! Creating functions has several benefits: 1. reduced code length. This makes it easier to read and make changes to. 2. Centralized point of failture. We all make mistakes. If you wrote the same code over and over and had to go back and change each time you wrote that code, it would be painful. Instead, if you had written it as a function, you would only have to change things in one place. 3. Abstraction. Wouldn't it be nice if you could just call a function like print average(list) and it just gave you the average?

```python
def avg(vals):
	total = 0
	for val in vals:
		total += val
	return total/len(vals)

myGrades = [92, 96, 88, 97]
print avg(myGrades)
```

#### Scoping

Scoping is an important concept that new programmers encounter first when writing functions for the first time. Many of you already know about scoping, but it can be a frustrating enough problem so I want to reiterate. Consider the following two functions.

```python
def func_a():
	var_a = 'a'

def func_b():
	var_b = 'b'
```

Variable var_a is said to be scoped to func_a. That is, it is local to func_a. If you were to try to use var_a outside of func_a, or inside of func_b, you would receive an out of scope error, typically telling you that a variable does not exist. There are two ways to handle the out of scope error. 1. Make the variable global, or 2. the more preferred method, pass the variable as an argument to the function in which you are wanting to use it.

#### Recursion

Recursion seems like a difficult concept, but its really just a different way to loop over a set of data. In a recursive function, we have a base case, and a recursive case. The recursive case makes an adjustment to the data being passed as an argument, and then passes it to itself by calling itself. A base case is where the recursion ends. Consider the following classic example of recursion: factorial.

```python

def fact(n):
	if n == 1:
		return n
	else:
		return n*fact(n-1) 

```

The way recursion works is based on a stack data type where function calls are placed in a stack and wait for a return value.
Let n = 3

| n | function | return value |
|---|----------|--------------|
| 3 | fact(3)  | 3\*fact(2)   |
| 2 | fact(2)  | 2\*fact(1)   |
| 1 | fact(1)  | 1	      |

As we can see, the first time the recursive function call hits a base case is when n = 1. Now, the functions can return back to the previous function call in the stack. We know fact(1) = 1, therefore fact(2) = 2\*1. Since fact(2) = 2, we know that fact(3) = 3\*fact(2) = 3\*2. And finally, fact(3) = 6.

### Exercises

* Write a function that takes an integer parameter and checks to see if the parameter is less than 10.
* If the parameter is less than 10, it alerts the user with a print statement

[Solution](scripts/func.py)

### What you should have learned:

* How and why to write functions
* How recursion works
* How to scope variables with respect to functions

![](../images/floridatech.png)
