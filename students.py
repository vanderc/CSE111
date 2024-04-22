import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    students_dict = read_dictionary('students.csv', I_NUMBER_INDEX)

    inumber = input('Please enter an I-number (xx-xxx-xxxx): ')

    inumber = inumber.replace('-', '')

    if not inumber.isdigit():
        print('Invalid character in I-number')
    else:
        if len(inumber) < 9:
            print('Invalid I-number: too few digits')
        elif len(inumber) > 9:
            print('Invalid I-number: too many digits')
        else:
            if inumber not in students_dict:
                print('No such student')
            else:
                value = students_dict[inumber]
                name = value[NAME_INDEX]
                print(name)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]

            dictionary[key] = row_list

    return dictionary

if __name__ == '__main__':
    main()