# zad1
def triangle(size):
    for i in range(size, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print('\r')


#triangle(10)


# zad2
def Fibonacci():
    l1 = 0
    l2 = 1
    for i in range(20):
        print(l1, end=" ")
        tmp = l1 + l2
        l1 = l2
        l2 = tmp


#Fibonacci()

# zad3
def count(num1, num2, num3, num4):
    def multiply(a, b):
        return a * b

    def add(a, b):
        return a + b

    def pow(a, b):
        return a ** b

    operation = pow(multiply(num1, add(num2, num3)), num4)
    return operation


# print(count(10, 3, 2, 4))


def lambdacount(num1, num2, num3, num4):
    multiply = lambda a, b: a * b
    add = lambda a, b: a + b
    pow = lambda a, b: a ** b

    operation = pow(multiply(num1, add(num2, num3)), num4)
    return operation


# print(lambdacount(10, 3, 2, 4))


# zad4
def caesar_cipher(text, step):
    tmp_list = []
    out_list = ''
    upper_text = text.upper()

    for letter in upper_text:
        if ord(letter) != 32:
            tmp_list.append(ord(letter) + step)
        else:
            tmp_list.append(ord(letter))

    for unicode in tmp_list:
        out_list += chr(unicode)

    return str(out_list)


#print(caesar_cipher('HELLO WORLD', 3))

























