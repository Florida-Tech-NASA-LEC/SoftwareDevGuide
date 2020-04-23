![](../images/artemis.png)
Section 4: Dictionaries
=====

## Content

### [Subsection 0: Dictionaries](#dictionaries)
> Basics of the dictionary data type
### [Subsection 1: Exercises](#exercises)
> Exercises to hone your skills

### Dictionaries

Dictionaries are a datatype that provide the developer with the ability to access a value given a key. Each entry in a dictionary is called a key-value pair. FOr example, consider a dictionary of names and email addresses.

> email = {"Bob Mercer":"bmercer@xyz.net", "Enrique Galaras":"egalaras@xyz.net"}

We can access the email by the user's name.

> print email["Bob Mercer"]
>
> bmercer@xyz.net

Dictionaries can be used to create a quick database. We can even nest dictionaries within dictionaries. Consider:

```python
 database = {
 	"Bob": {
		"email": "bmercer@xyz.net",
		"phone": "1(321)425-0393"
	},
	"Enrique": {
		"email": egalaras@xyz.net",
		"phone": "1(321)591-4615"
	}
 }
```

Dictionaries are unordered, so we cannot access keys or values by index. We must use the key to access the value.

> print database["Bob"]["email"]
>
> bmercer@xyz.net

#### Exercises

* Create a dictionary database of your team structure.
	* You should be able to access team member names (values) by keys

[Solution](scripts/dict.py)

#### What you should have learned:

* How to manage dictionaries

![](../images/floridatech.png)
