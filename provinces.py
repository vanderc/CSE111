def main():
    # Read contents of provinces.txt and put into a list
    provinces_list = read_list('provinces.txt')

    # print entire list
    print(provinces_list)

    # remove first element of list
    provinces_list.pop(0)

    # remove las element
    provinces_list.pop()

    # replace AB with ALberta
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'

    # call list.count to count number of Albertas in list
    count = provinces_list.count('Alberta')

    print()
    print(f'Alberta occurs {count} times in the modified list')


def read_list(filename):

    # create an empty list that will store the line of text from text_file
    text_list = []

    # open the text file for reading and store a reference to the opened file
    with open(filename, 'rt') as text_file:

        # read the contents of the text file one line at a time
        for line in text_file:

            # remove white space, if there is any, from the beginning and end of the line.
            clean_line = line .strip()

            # append the clean line of text onto the end of the list
            text_list.append(clean_line)
    
    # return the list that contains the lines of text
    return text_list

if __name__ == '__main__':
    main()
