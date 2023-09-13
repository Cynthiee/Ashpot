import csv

data = ['name','age', 'sex'] 
with open('delimit.csv', 'w') as file:
    write_n = csv.writer(file)
    write_n.writerow(data)




# m_csv = open('new_csv', 'r')
# read_csv = csv.reader(m_csv)

# for i in read_csv:
#     print(i)