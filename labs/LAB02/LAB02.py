def zad1():
    # zainicjuj krotkę z kilkoma ocenami (parzysta liczba ocen, niech jakieś oceny
    # się powtarzają)
    tuple = (4, 3, 2, 5, 3, 5)
    print(tuple)

    # wypisz sumę ocen (funkcja sum())
    print("Suma: " + str(sum(tuple)))

    # wypisz średnią ocen
    print("Średnia ocen: " + str(sum(tuple) / len(tuple)))

    # sprawdź medianę ocen
    sortedList = sorted(tuple)

    if len(tuple) % 2 == 0:
        mid = len(tuple) // 2
        median = (tuple[mid - 1] + tuple[mid]) / 2
        print("Mediana: " + str(median))
    else:
        midElem = len(tuple) / 2
        print("Mediana: " + str(midElem))

    # sprawdź najwyższą (max()) i najniższą (min()) ocenę
    print("Min: " + str(min(tuple)))
    print("Max: " + str(max(tuple)))

    # wykonaj rzutowanie (castowanie) krotki na set. Wyświetl zawartość nowej
    # kolekcji.
    set1 = set(tuple)
    print("set: " + str(set1))


def zad2():
    # Stwórz słowniki
    student1 = {'index': 1000, 'name': 'Bob', 'surname': 'Kovalsky'}
    student2 = {'index': 1001, 'name': 'Michal', 'surname': 'Nowak'}
    student3 = {'index': 1002, 'name': 'Jan', 'surname': 'Kowalski'}

    # Stwórz trzeciego studenta o dowolnych danych.
    student_list = [student1, student2, student3]

    # Stwórz listę, do której umieścisz wszystkich studentów
    # Przy pomocy print() i input() zrób proste menu w terminalu, w którym będzie
    # można wybrać opcje:

    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    index = input("Podaj index: ")

    newStudent = {'index': index, 'name': name, 'surname': surname}

    # a) dodaj studenta
    student_list.append(newStudent)

    print(student_list)

    # usuń studenta
    last_element_of_list = len(student_list) - 1

    del student_list[last_element_of_list]

    print(student_list)

    print(" ")
    # sprawdź studentów
    for element in student_list:
        print(element.values())

    # d) wyświetl informacje o konkretnym studencie,
    searched_student = input("Wprowadz index studenta ktorego chesz wyszukac: ")

    if int(searched_student) > len(student_list) or int(searched_student) < 0:
        print("dupa")
    else:
        print(student_list[int(searched_student)])


def zad3():
    marks = []

    input_marks = input("Podaj kilka ocen: ")

    marks_list = input_marks.split()

    for mark in marks_list:
        marks.append(int(mark))

    if any(int(x) < 2 or int(x) > 5 for x in marks):
        print("Niedozwolona ocena")
    else:
        print(marks)
        avg = sum(marks) / len(marks)
        print(avg)
        if any(int(x) == 2 for x in marks):
            print("Lista zawiera ocene 2")
