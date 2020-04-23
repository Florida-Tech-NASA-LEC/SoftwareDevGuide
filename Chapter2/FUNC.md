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

#### Exercises


[Solution](loop.py)

#### What you should have learned:


![](../images/floridatech.png)
