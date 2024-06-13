reader = open('hello.txt', 'r')
content = reader.read()
print(content)
reader.close()


reader = open('hello.txt', 'r')
content = reader.readlines()
print(content)
reader.close()

for line in content:
    print(line)



reader = open('hello.txt', 'r')
content = reader.read()
print(content)
reader.close()

for line in range(1,3):
    print(line)

reader = open('hello.txt', 'r')

for i in range(3):
    line = reader.readline()
    if not line:
        break
    print(line.strip())

reader.close()


writer = open('write.js', 'w')
content = writer.write("Hello, I just wrote this with write method.")
print(content)
writer.close()
