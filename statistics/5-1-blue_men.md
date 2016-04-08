---
output: pdf_document
---
[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
"""
Answer for exercise 1 chapter 5.
"""
from scipy.stats import norm

mu = 178.0
sigma = 7.7

#convert 5'10" and 6'1" to cm
 
b0_height = ((5 * 12) + 10) * 2.54
b1_height = ((6 * 12) + 1) * 2.54

dist = norm(loc=mu, scale=sigma)

p0 = dist.cdf(b0_height)
p1 = dist.cdf(b1_height)

percent = 100 * (p1 - p0)
# Print result.
print('Percent of USA male population height between')
print('5\'10\"-6\'1\" %  (b0_height, b1_height, percent ))
```
