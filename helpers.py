import math

def printf(dirs): # prints the content of a directory formatted in 3 columns
    print(len(dirs))
    columns = math.ceil(len(dirs)/3) #gets the number of files and directories in every column

    fcolumn = dirs[0:columns] #the content in the first column
    max_f = get_max_len(fcolumn) #the max length of a file or directory from the first column. Used for formatting the spaces between columns

    scolumn = dirs[columns:columns*2] #the content in the second column
    max_s = get_max_len(scolumn) #the max length of a file or directory from the second column

    tcolumn = dirs[columns*2:] #the content in the third column

    while len(fcolumn) != 0:
        if len(fcolumn) == 1 and len(scolumn) == 0 and len(tcolumn) == 0: #
            first = fcolumn.pop(0)
            print(first)

        elif len(fcolumn) >= 1 and len(scolumn) >= 1 and len(tcolumn) == 0:
            first = fcolumn.pop(0)
            second = scolumn.pop(0)
            print("{!s} {!s}".format(first + " " * (max_f - len(first) + 4), second))

        else:
            first = fcolumn.pop(0)
            second = scolumn.pop(0)
            third = tcolumn.pop(0)
            print("{!s} {!s} {!s}".format(first + " " * (max_f - len(first) + 4), second + " " * (max_s - len(second) + 4), third))

def get_max_len(column):#returns the length of the longest string from a list
    return len(max(column, key=len))

def redirection(args):
    if '>' == args[-2]:
        filename = args.pop()
        open_file = open (filename, "w+") #creates a file or overwrites if it exists already
        args.pop() # remove > from the args
        return args, open_file #returns the arguments and opened file

    elif ">>" == args[-2]:
        filename = args.pop()
        open_file = open (filename, "a+") #creates a file or appends if it exists already
        args.pop() # remove >> from the args
        return args, open_file #returns the arguments and opened file

    return args, None #if there is no redirection, return the arguments and None as file to write to
        
