---
output: pdf_document
---
[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen\'s d)


```
import pandas as pd
import numpy as np
import nsfg

def CohenEffectSize(x1, x2):
    """
    This function compare the difference between two variables. 
    """

    mean1 = x1.mean()
    mean2 = x2.mean()

    s1 = x1.var()
    s2 = x2.var()

    n1 = len(x1)
    n2 = len(x2)

    s = ((n1 * s1)  + (n2 * s2)) / (n1 + n2)
    d = (mean1 - mean2) / np.sqrt(s)
    return(d)

def WeightDiff(alives, firsts, others):
    """
    This function investigates whether first babies are lighter
    or haviear than others.
    """
    d = CohenEffectSize(firsts, others)
    #Create dataframe with the results.
    results_df = {'alives_babies': [alives.mean(), alives.var()],
            'first_babies': [firsts.mean(), firsts.var()],
            'others_babies': [others.mean(), others.var()] }
    results_df = pd.DataFrame(results_df,
        index=['Mean', 'Variance'])
    print('\n Summary of the data')
    print(results_df)
    print('\nCohen\'s d: %f' % d)

    return
```
The code below use the function above to find the Cohen's d. Since
d is small (0.089), tt is quite clear that first babies are NOT 
lighter or havier than others. 

Remark: A full answer for this question required inference.
 
```
import nsfg
import numpy as np
import chap02ex as ex
import chap02soln as soln

df = nsfg.ReadFemPreg()
np.set_printoptions(precision=4)
# Considere the live cases and no NAN values.
mask = (df.outcome == 1) & ~np.isnan(df.totalwgt_lb)

alives = df.ix[mask,'totalwgt_lb']
firsts = df.ix[mask & (df.birthord == 1), 'totalwgt_lb']
others = df.ix[mask & (df.birthord != 1), 'totalwgt_lb']

print('================\n Your answer:')
ex.WeightDiff(alives, firsts, others)

```
