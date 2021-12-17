f = open("myfiles/data1.txt", "w")
for i in range(0, 100):
    f.write(f'\n {i}')
f.close()

f = open('myfiles/data1.txt', 'r')
print(f.read())
