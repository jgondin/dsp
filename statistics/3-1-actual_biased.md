---
output: pdf_document
---
[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
"""
Answer for exercise 1 chapter 3
"""
import matplotlib.pylab as pl
import numpy as np
import chap01soln


resp = chap01soln.ReadFemResp()
np.set_printoptions(precision=4)

freq = dict(resp.numkdhh.value_counts())
n = sum(freq.values())

def pmf(n, freq):
    p = {}
            
    for k, v in freq.items():
        p[k] = v / n
                                    
    return(p)

def bias_pmf(pmf):
    p = pmf.copy()
    s = 0
                                                    
    for k, v in pmf.items():
        p[k] = v * k
        s += p[k]

    s = sum(p.values())

    for k, v in pmf.items():
        p[k]  /=  s
   
    return(p)

def mean_pmf(pmf):
    xbar = 0
    for k, v in pmf.items():
        xbar += k * v
    xbar /= sum(list(pmf.keys()))
    return(xbar)

def var_pmf(pmf):
    sigma = 0
    xbar = mean_pmf(pmf)
    
    for k, v in pmf.items():
        sigma += k * ((xbar - v)**2)

    sigma /= sum(pmf.values())
    return(sigma)

#calculate the actual, bias and unbias PMF. 

rpmf = pmf(n, freq)
rbias_pmf = bias_pmf(rpmf)


#Display results
fig = pl.figure()
pl.subplot(121)
x = np.array(list(rpmf.keys()))
h = list(rpmf.values())
pl.bar(x, h, width= 0.8)
pl.ylabel('Percentage points')
pl.xlabel('Number of children under 18')
pl.xticks(x + 0.8/2.0, x)
pl.title('Actual PMF')
print('Mean: %f' % mean_pmf(rpmf))
print('Var:  %f' % var_pmf(rpmf))

pl.subplot(122)
x = np.array(list(rbias_pmf.keys()))
h = list(rbias_pmf.values())
pl.bar(x, h, width= 0.8)
pl.ylabel('Percentage points')          
pl.xlabel('Number of children under 18')
pl.xticks(x + 0.8/2.0, x)
pl.title('Bias PMF')
print('Mean: %f' % mean_pmf(rbias_pmf))
print('Var:  %f' % var_pmf(rbias_pmf))


pl.show()
```