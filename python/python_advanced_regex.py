import csv
import collections as cl
# Function to read the csv file.
def read_data(file):
    ifile = open(file)
    data = list(csv.reader(ifile))
    ifile.close()
    return(data)

# Function to write the csv file.
def write_data(data, file):
    ofile = open(file, 'w')
    writer = csv.writer(ofile, delimiter =',')                              
    writer.writerows(data)
    ofile.close()
    return


facu = read_data('/home/gondin/metis/bootcamp/dsp/python/faculty.csv')

# Crete list dictionary with the degrees.
deg_freq = {'PhD': 0, 'ScD': 0, 'MD':0, 'MPH':0, 'BSEd':0, \
        'MS':0, 'JD':0,}

#Q1 Calculate frequecy
for i in range(1,len(facu)):
    key = facu[i][1]
    key = key.replace('.','')
    key = key.replace(' ','', 1)
    if key in deg_freq.keys():
        deg_freq[key] += 1
    else:
        keys = key.split(' ')
        keys = [k  for k in keys if k!='']
        for k in keys:
            if k in deg_freq.keys():
                deg_freq[k] += 1
        deg_freq[key] = 1

#Degree frequency:
print('----')
for k, v in deg_freq.items():
    print(k, v)

#Q2 Titles:

titles = {}
for i in range(1, len(facu)):
    key = facu[i][2]
    key = key.replace(' ','',1)
    if key in titles.keys():
        titles[key] +=1
    else:
        titles[key] = 1

#Print titles frequency:
print('------')
for k, v in titles.items():
    print(k, v)                  

#Q3 emails:

emails = []
for i in range(1, len(facu)):
    emails.append( facu[i][3])
    
#Print emails list:
print('------')
for v in emails:
    print(v) 

#Q4 emails domain:

domains = []
for e in emails:
    d = e.split('@')[1]
    d = d.replace(' ', '')
    if d not in domains:
        domains.append(d)

#print domains
print('----')
for v in domains:
    print(v)



