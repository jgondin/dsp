---
output: pdf_document
---
# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Differences between lists and tuples:

- Lists are mutable, tuples are imnutable.
- Lists and tuples have different methods/Attibutes(e.g. append and copy)

Similaris between lists and tuples:

- Lists and tuples store collection of "objects".
- The opereter "+" works similar with tuple + tuples, and list + list.
- A list may have a tuple as an element, and so does a tuple.
- Tuple and list may have theirs elements accessed using "[]".

Only the tuple works as keys for dictionaries since it is inmutable. Neither a list nor a dictionary can do so.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Similarities:

- Both store a collection os elements.
- Both are mutable.
- Both accept "in" for seach.

Diffencies:

- Sets are unorted, lists are not.
- Sets have unique elements, lists do not.
- Sets have different methods (e.g. union and intersection).
- The operators  &, ^, | works on sets, not on lists.
- ``x in s'' and ``x in l'' different time complexity. 
in an [average case](https://wiki.python.org/moin/TimeComplexity) 
O(len(s)) and O(len(n)), respecvely.   
- Iteration over a list is faster than over a set.

 
---

###Q3. Lambda Function

Describe Pythons `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is a oparetor use to define a anonymous function, i.e. a function withouth a name.

Example 1:  
```
from scipy.misc import derivative   
f = lambda x: x**2
df = lambda x: derivative(f, x)  
```
Example 2:
````
y_sq = list(map(lambda x: x**2, [-1,0,2,3]))  
```
Example 3:
```  
odds = list(filter(lambda x: x%2!=0, range(1,15)))	
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

"List comprehensions" is a alternative for lambda, map, and filter.
It is a way to create sofisticated list very fast.

```
#Examples:
#list of odds numbers   
odds = list(filter(lambda x: (x%2!=0), range(0,100))) 
#list with multiples of 7     
mult_7 = list(map(lambda x: 7*x, range(15)) )   
#list of prime numbers  
mult = lambda i: set(range(2*i,100,i))  
no_prime = set()  
for i in range(2,100):  
     no_prime = no_prime.union(mult(i))  

prime = list(filter(lambda p: p not in no_prime, range(2, 100)))  

# with list comprehension
#odds numbers  
odds_new = [x for x in range(15) if (x%2!=0)]  

#multiples of 7  
mult_7_new = [7*x for x in range(15)]  

# prime numbers from 0 to 100   
no_prime = set([np for i in range(2,100) for np in range(i*2, 100,i)]) 
prime = [p for p in range(2,100) if p not in no_prime]  
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'

answer
>> dela = 937 days.
```
b.  
```
date_start = '12312013'  
date_stop =  '05282015'  
```

>> 1076 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





