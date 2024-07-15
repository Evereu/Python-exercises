import csv
import random


def anonymization(text, step):
    tmp_list = []
    out_list = ''
    text = text

    for letter in text:
        tmp_list.append(ord(letter) + step)

    for unicode in tmp_list:
        out_list += chr(unicode)

    return str(out_list)


def zad3():
    output_rows = []

    with open('departament.csv') as my_csv:
        csv_reader = csv.reader(my_csv, delimiter=';')

        for row in csv_reader:
            rowwww = []
            for item in row[:-1]:
                length = random.randint(1, 20)
                if '@' in item:
                    at = item.split("@")
                    rowwww.append(str(anonymization(at[0], length) + '@' + at[1]))
                else:
                    rowwww.append(str(anonymization(item, length)))
            rowwww.append(row[-1])

            output_rows.append(';'.join(rowwww))

        for row in output_rows:
            print(row)


zad3()
