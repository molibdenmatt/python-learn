filename = 'programming.txt'

with open(filename, 'w') as file_object:  # w - as write. Will erase previous file
    file_object.write("I love programming!\n")
    file_object.write("And I like coffee\n")

with open(filename, 'a') as file_object:  # a - as append. Will add to exiting file
    file_object.write("I also like cats!\n")
