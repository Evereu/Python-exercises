import os


def zad1():
    directory = "my_folder1"

    num_list = []
    suma = 0

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".txt"):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r') as my_file:
                    for line in my_file:
                        num_list.append(int(line))

    for num in num_list:
        suma += num

    print(suma)


zad1()
