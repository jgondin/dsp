# Hint:  use Google to find python function

####a) 
import datetime as dt
date_start = dt.datetime.strptime('01-02-2013', '%m-%d-%Y')  
date_stop = dt.datetime.strptime('07-28-2015', '%m-%d-%Y')   

delta = date_stop - date_start
print(' %d days' % delta.days)

####b)  
date_start = dt.datetime.strptime('12312013', '%m%d%Y')  
date_stop = dt.datetime.strptime('05282015', '%m%d%Y')  
delta = date_stop - date_start
print(' %d days' % delta.days)

####c)  
date_start = dt.datetime.strptime('15-Jan-1994', '%d-%b-%Y')    
date_stop = dt.datetime.strptime('14-Jul-2015', '%d-%b-%Y') 

delta = date_stop - date_start

print(' %d days' % delta.days)

 
