# Initialization of Lists
list1 = []
list2 = []
list3 = []
list4 = []
# Infinite loop until a valid integer is entered for the number of subjects
while True:
    ask = input('Press 1 to encode the text.\nPress 2 to decode the text. ')
    if ask.isdigit():
        ask = int(ask)
    else:
        print(f'''{ask} is not an integer, try one more time! ''')
        continue
    # Encoding
    if ask == 1:
        # Read content from 'main.txt'
        file = open('main.txt', 'r')
        content = file.read()
        # Store its contents in a list. Convert the list into a “String” data type.
        for i in content:
            list1.append(i)
        my_str = ''.join(list1)
        # Convert each character to its hexadecimal representation
        for letter in my_str:
            list2.append(format(ord(letter), '0x'))
        file.close()
        # Write the hexadecimal representation to 'hexstring.txt'
        file = open('hexstring.txt', 'w')
        file.write(' '.join(list2))
        file.close()
        print(f'''The file main.txt is encoded successfully in a new file hexstring.txt ''')
        continue
    # Decoding
    elif ask == 2:
        # Read content from 'hexstring.txt'
        file = open('hexstring.txt', 'r')
        content1 = file.read()
        list3 = content1.split()
        # Convert each hexadecimal representation to its character
        for letter1 in list3:
            # Convert to decimal
            dec = int(letter1, base=16)
            # Convert to its character
            list4.append(chr(dec))
        file.close()
        # Write the decoded content to 'final.txt'
        file = open('final.txt', 'w')
        file.write(''.join(list4))
        file.close()
        print(f'''The file hexstring.txt is decoded successfully in a new file final.txt ''')
        # User Prompt for Program Termination
        finish = input('Do you want to finish the programm? ')
        if 'ye' in finish.lower():
            break
        elif 'no' in finish.lower():
            continue
        else:
            print('What do you mean????')

    else:
        print('Enter 1 or 2!!!!!')
