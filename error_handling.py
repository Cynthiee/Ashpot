# Try and Except/ file handling

# try:
#     foods = ['rice', 'beans', 'garri']
#     print(foods[4])
# except:
#     print('Item with the index number does not exist.')


# def add(x, y):
#     if y == 0:
#         raise ZeroDivisionError("Value not divisible")
#     return x/y

# sum = add(3,0)
# print(sum)


# import sys
# try:
#     file = open('try.txt', 'r')
#     print(file.readline())
#     file.close()

# except FileNotFoundError:
#     print('File does not exit')
# finally:
#     sys.exit()


# try:
#     value = int(input('Enter a number: '))
#     division = 200/value
#     print(division)
# except ZeroDivisionError as e:
#     # print("Value not divisible")
#     print(str(e))

# except ValueError:
#     print("Cannot divide a number with strings")
    

try:
    file = open('try.txt', 'r')
except FileNotFoundError:
    print('File does not exist')
except Exception as e:
    print(str(e))
else:
    print('File was opened successfully')
finally:
    file.close()