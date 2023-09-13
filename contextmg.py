with open('try.txt', 'r') as f:
    content = f.readline()
    print(content)


with open('newfile.txt', 'w') as file:
    data = file.write("Hello. I'm learning context manager")