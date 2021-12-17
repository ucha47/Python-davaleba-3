f = open('myfiles/data.txt', 'w')
f.write(f'\n {24}, {39}, {-90}')
f.close()

f = open('myfiles/data.txt', 'r')
print(f.read())