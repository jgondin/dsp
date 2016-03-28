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

print('\n Question 5')
#Q5
emails = []
for i in range(1, len(facu)):
    emails.append(facu[i][3])

file = '/home/gondin/metis/bootcamp/dsp/python/emails.py'
write_data(emails, file)

#print emails.
for e in emails:
    print(e)

print('\n Quetion 6')    
#Q6 
faculty_dict = cl.OrderedDict()
for row in facu[1:]:
    key = row[0].split(' ')[-1]
    if key in faculty_dict.keys():
        faculty_dict[key].append(row[1:])
    else:
        faculty_dict[key] = [row[1:]]

#print  faculty_dict
for k in faculty_dict.keys():
    print(k,': [')
    for v in faculty_dict[k]:
        print(v)
    print('          ]')

print('\n Question 7')
#Q7
professor_dict = cl.OrderedDict()
for row in facu[1:]:
    key = row[0].split(' ')
    key = '(' + key[0] + ', ' + key[-1] + ')'
    professor_dict[key] = row[1:]

for k, v in professor_dict.items():
    print(k, v)

print('\n Question 8')
prof_dict_sorted = cl.OrderedDict()
for row in facu[1:]:
    name = row[0].split(' ')
    first = name[0]
    last = name[-1]
    key = '(' + first + ', ' + last + ')'
    prof_dict_sorted[key] = row[1:]
    for l in prof_dict_sorted.keys():
        old_last = l.split(', ')[-1][:-1]
        
        if old_last > last:
            prof_dict_sorted[l], prof_dict_sorted[key] = \
                    prof_dict_sorted[key], prof_dict_sorted[l]

for k, v in prof_dict_sorted.items():
    print(k, v)

