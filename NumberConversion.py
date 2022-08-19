# int() is a built-in function that converts decimal to binary
# int() take two arguments the decimal number and the base number of binary
def binary_to_decimal(a):
    return int(a, 2)


a = input('Enter a binary number to convert to decimal: ')
print(binary_to_decimal(a))


# bin() is a built-in function that takes its argument and converts it to binary
def decimal_to_binary(b):
    return bin(b).replace("0b", "")


b = int(input('\n\nEnter a decimal number to convert to binary: '))
print(decimal_to_binary(b))


# oct() is  built in function that takes an argument from decimal to octal
def decimal_to_octal(c):
    if c > 0:
        return oct(c).replace('0o', '')
    else:
        exit()


# Whatever you don't find familiar is an inbuilt function used to convert
c = int(input('\n\nEnter the decimal number to convert to octal: '))
print(decimal_to_octal(c))


def octal_to_decimal(d):
    return int(d, 8)


d = input('\n\nEnter octal number to convert to decimal: ')
print(octal_to_decimal(d))


# At this point you kind of know the flow, built-in functions do the conversion
def decimal_to_hexadecimal(e):
    return hex(e).replace('0x', '')


e = int(input('\n\nEnter decimal number tobe converted to hexadecimal: '))
print(decimal_to_hexadecimal(e))


def hexadecimal_to_decimal(f):
    return int(f, 16)


f = input('\n\nEnter hexadecimal number to be converted to decimal number: ')
print(hexadecimal_to_decimal(f))


def binary_to_hexadecimal(g):
    return hex(int(g, 2)).replace('0x', '')


g = input('\n\nEnter binary to be converted to hexadecimal: ')
print(binary_to_hexadecimal(g))


def binary_to_octal(h):
    h = int(h, 2)
    h = oct(h).replace('0o', '')
    return h


h = input('\n\nEnter binary number to be converted: ')
print(binary_to_octal(h))


def hexadecimal_to_binary(i):
    i = int(i, 16)
    i = bin(i).replace('0b', '')
    return i


i = input('\n\nEnter the hexadecimal to be converted to binary: ')
print(hexadecimal_to_binary(i))


def octal_to_hexadecimal(j):
    j = int(j, 8)
    j = hex(j).replace('0x', '')
    return j


j = input('\n\nEnter octal number to be converted to hexadecimal: ')
print(octal_to_hexadecimal(j))


def octal_to_binary(k):
    k = int(k, 8)
    k = bin(k).replace('0b', '')
    return k


k = input('\n\nEnter octal number to be converted to binary: ')
print(octal_to_binary(k))


def hexadecimal_to_octal(l):
    l = int(l, 16)
    l= oct(l).replace('0o', '')
    return l


l = input('\n\nEnter hexadecimal to be converted to octal: ')
print(hexadecimal_to_octal(l))

print("\n\nThanks for playing")
